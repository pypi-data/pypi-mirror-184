# -*- coding: utf-8 -*-
"""
Test the object that handles the nested sampling evidence and prior volumes.
"""
from unittest.mock import create_autospec
import numpy as np
import pytest

from nessai.evidence import (
    _NSIntegralState,
    logsubexp,
)


@pytest.fixture()
def nlive():
    return 100


@pytest.fixture()
def ns_state():
    return create_autospec(_NSIntegralState)


def test_logsubexp_negative():
    """
    Test behaviour of logsubexp for x < y
    """
    with pytest.raises(Exception):
        logsubexp(1, 2)


def test_increment(nlive):
    """Test the basic functionality of incrementing the evidence estimate"""
    state = _NSIntegralState(nlive)
    state.increment(-10)

    assert state.logw == (-1 / nlive)
    assert state.logZ != -np.inf
    np.testing.assert_equal(state.logLs, [-np.inf, -10])


def test_log_evidence(ns_state):
    """Assert the log-evidence property returns the correct value"""
    expected = 1.0
    ns_state.logZ = expected
    out = _NSIntegralState.log_evidence.__get__(ns_state)
    assert out == expected


def test_log_evidence_error(ns_state, nlive):
    """Assert the log-evidence error property returns the correct value"""
    expected = np.sqrt(10 / nlive)
    ns_state.info = [1, 5, 10]
    ns_state.nlive = nlive
    out = _NSIntegralState.log_evidence_error.__get__(ns_state)
    assert out == expected


def test_finalise(nlive):
    """Test the check that finalise returns an improved logZ"""
    state = _NSIntegralState(nlive)
    state.increment(-10)
    pre = state.logZ
    state.finalise()
    assert state.logZ != -np.inf
    assert pre != state.logZ


def test_info(nlive):
    """Test to check the information increases as expected"""
    state = _NSIntegralState(nlive)
    state.increment(-10)
    assert state.info == [0.0]
    state.increment(-5)
    assert state.info[1] > 0


def test_track_gradients(nlive):
    """
    Test to make sure gradients are not computed when tracking is disabled
    """
    state = _NSIntegralState(nlive, track_gradients=False)
    state.increment(-10)
    state.increment(-5)
    assert len(state.gradients) == 1


def test_variable_nlive(nlive):
    """
    Test to make sure that the using a different nlive changes the update
    values.
    """
    state = _NSIntegralState(nlive)
    state.increment(-10, nlive=50)
    assert state.logw == (-1 / 50)


def test_plot(nlive):
    """Test the plotting function"""
    state = _NSIntegralState(nlive)
    state.increment(-10)
    state.increment(-5)
    fig = state.plot()
    assert fig is not None


def test_plot_w_filename(nlive, tmpdir):
    """Test the plotting function with a filename specified"""
    filename = str(tmpdir.mkdir("test"))
    state = _NSIntegralState(nlive)
    state.increment(-10)
    state.increment(-5)
    fig = state.plot(filename=filename)
    assert fig is None
