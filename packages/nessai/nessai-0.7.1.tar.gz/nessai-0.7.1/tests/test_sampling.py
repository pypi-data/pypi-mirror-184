# -*- coding: utf-8 -*-
"""
Integration tests for running the sampler with different configurations.
"""
import logging
import os
import torch
import pytest
import numpy as np
from unittest.mock import patch

from nessai.flowsampler import FlowSampler
from nessai.livepoint import numpy_array_to_live_points
from nessai.model import Model


torch.set_num_threads(1)


@pytest.mark.slow_integration_test
def test_sampling_with_rescale(model, flow_config, tmpdir):
    """
    Test sampling with rescaling. Checks that flow is trained.
    """
    output = str(tmpdir.mkdir("w_rescale"))
    fp = FlowSampler(
        model,
        output=output,
        resume=False,
        nlive=100,
        plot=False,
        flow_config=flow_config,
        training_frequency=10,
        maximum_uninformed=9,
        rescale_parameters=True,
        seed=1234,
        max_iteration=11,
        poolsize=10,
    )
    fp.run()
    assert fp.ns.proposal.flow.weights_file is not None
    assert fp.ns.proposal.training_count == 1


@pytest.mark.slow_integration_test
def test_sampling_with_inversion(model, flow_config, tmpdir):
    """
    Test sampling with inversion. Checks that flow is trained.
    """
    output = str(tmpdir.mkdir("w_rescale"))
    fp = FlowSampler(
        model,
        output=output,
        resume=False,
        nlive=100,
        plot=False,
        flow_config=flow_config,
        training_frequency=10,
        maximum_uninformed=9,
        rescale_parameters=True,
        seed=1234,
        max_iteration=11,
        poolsize=10,
        boundary_inversion=True,
        update_bounds=True,
    )
    fp.run()
    assert fp.ns.proposal.boundary_inversion == ["x", "y"]
    assert fp.ns.proposal.flow.weights_file is not None
    assert fp.ns.proposal.training_count == 1


@pytest.mark.slow_integration_test
def test_sampling_without_rescale(model, flow_config, tmpdir):
    """
    Test sampling without rescaling. Checks that flow is trained.
    """
    output = str(tmpdir.mkdir("wo_rescale"))
    fp = FlowSampler(
        model,
        output=output,
        resume=False,
        nlive=100,
        plot=False,
        flow_config=flow_config,
        training_frequency=10,
        maximum_uninformed=9,
        rescale_parameters=False,
        seed=1234,
        max_iteration=11,
        poolsize=10,
    )
    fp.run()
    assert fp.ns.proposal.flow.weights_file is not None
    assert fp.ns.proposal.training_count == 1


@pytest.mark.slow_integration_test
def test_sampling_with_maf(model, flow_config, tmpdir):
    """
    Test sampling with MAF. Checks that flow is trained but does not
    check convergence.
    """
    flow_config["model_config"]["ftype"] = "maf"
    output = str(tmpdir.mkdir("maf"))
    fp = FlowSampler(
        model,
        output=output,
        resume=False,
        nlive=100,
        plot=False,
        flow_config=flow_config,
        training_frequency=10,
        maximum_uninformed=9,
        rescale_parameters=True,
        seed=1234,
        max_iteration=11,
        poolsize=10,
    )
    fp.run()
    assert fp.ns.proposal.flow.weights_file is not None
    assert fp.ns.proposal.training_count == 1


@pytest.mark.slow_integration_test
@pytest.mark.parametrize("analytic", [False, True])
def test_sampling_uninformed(model, flow_config, tmpdir, analytic):
    """
    Test running the sampler with the two uninformed proposal methods.
    """
    output = str(tmpdir.mkdir("uninformed"))
    fp = FlowSampler(
        model,
        output=output,
        resume=False,
        nlive=100,
        plot=False,
        flow_config=flow_config,
        training_frequency=None,
        maximum_uninformed=10,
        rescale_parameters=True,
        seed=1234,
        max_iteration=11,
        poolsize=10,
        analytic_proposal=analytic,
    )
    fp.run()


@pytest.mark.slow_integration_test
def test_sampling_with_n_pool(model, flow_config, tmpdir, mp_context):
    """
    Test running the sampler with multiprocessing.
    """
    output = str(tmpdir.mkdir("pool"))
    with patch("multiprocessing.Pool", mp_context.Pool):
        fp = FlowSampler(
            model,
            output=output,
            resume=False,
            nlive=100,
            plot=False,
            flow_config=flow_config,
            training_frequency=10,
            maximum_uninformed=9,
            rescale_parameters=True,
            seed=1234,
            max_iteration=11,
            poolsize=10,
            pytorch_threads=2,
            n_pool=2,
        )
    fp.run()
    assert fp.ns.proposal.flow.weights_file is not None
    assert fp.ns.proposal.training_count == 1
    assert os.path.exists(os.path.join(output, "result.json"))


@pytest.mark.slow_integration_test
def test_sampling_resume(model, flow_config, tmpdir):
    """
    Test resuming the sampler.
    """
    output = str(tmpdir.mkdir("resume"))
    fp = FlowSampler(
        model,
        output=output,
        resume=True,
        nlive=100,
        plot=False,
        flow_config=flow_config,
        training_frequency=10,
        maximum_uninformed=9,
        rescale_parameters=True,
        checkpoint_on_iteration=True,
        checkpoint_frequency=5,
        seed=1234,
        max_iteration=11,
        poolsize=10,
    )
    fp.run()
    assert os.path.exists(os.path.join(output, "nested_sampler_resume.pkl"))

    fp = FlowSampler(
        model,
        output=output,
        resume=True,
        flow_config=flow_config,
    )
    assert fp.ns.iteration == 11
    fp.ns.max_iteration = 21
    fp.run()
    assert fp.ns.iteration == 21
    assert os.path.exists(
        os.path.join(output, "nested_sampler_resume.pkl.old")
    )


@pytest.mark.slow_integration_test
def test_sampling_resume_w_pool(model, flow_config, tmpdir, mp_context):
    """
    Test resuming the sampler with a pool.
    """
    output = str(tmpdir.mkdir("resume"))
    with patch("multiprocessing.Pool", mp_context.Pool):
        fp = FlowSampler(
            model,
            output=output,
            resume=True,
            nlive=100,
            plot=False,
            flow_config=flow_config,
            training_frequency=10,
            maximum_uninformed=9,
            rescale_parameters=True,
            checkpoint_on_iteration=True,
            checkpoint_frequency=5,
            seed=1234,
            max_iteration=11,
            poolsize=10,
            n_pool=1,
        )
    assert fp.ns.model.n_pool == 1
    fp.run()
    assert os.path.exists(os.path.join(output, "nested_sampler_resume.pkl"))
    # Make sure the pool is already closed
    model.close_pool()

    with patch("multiprocessing.Pool", mp_context.Pool):
        fp = FlowSampler(
            model,
            output=output,
            resume=True,
            flow_config=flow_config,
            n_pool=1,
        )
    assert fp.ns.model.n_pool == 1
    assert fp.ns.iteration == 11
    fp.ns.max_iteration = 21
    fp.run()
    assert fp.ns.iteration == 21
    assert os.path.exists(
        os.path.join(output, "nested_sampler_resume.pkl.old")
    )


@pytest.mark.slow_integration_test
def test_sampling_resume_no_max_uninformed(model, flow_config, tmpdir):
    """
    Test resuming the sampler when there is no maximum iteration for
    the uinformed sampling.

    This test makes sure the correct proposal is loaded after resuming
    and re-initialising the sampler.
    """
    output = str(tmpdir.mkdir("resume"))
    fp = FlowSampler(
        model,
        output=output,
        resume=True,
        nlive=100,
        plot=False,
        flow_config=flow_config,
        training_frequency=10,
        maximum_uninformed=9,
        rescale_parameters=True,
        seed=1234,
        max_iteration=11,
        checkpoint_on_iteration=True,
        checkpoint_frequency=5,
        poolsize=10,
    )
    fp.run()
    assert os.path.exists(os.path.join(output, "nested_sampler_resume.pkl"))

    fp = FlowSampler(
        model, output=output, resume=True, flow_config=flow_config
    )
    assert fp.ns.iteration == 11
    fp.ns.maximum_uninformed = np.inf
    fp.ns.initialise()
    assert fp.ns.proposal is fp.ns._flow_proposal
    fp.ns.max_iteration = 21
    fp.run()
    assert fp.ns.iteration == 21
    assert os.path.exists(
        os.path.join(output, "nested_sampler_resume.pkl.old")
    )


@pytest.mark.slow_integration_test
def test_sampling_with_infinite_prior_bounds(tmpdir):
    """
    Make sure the sampler runs when sampling a parameter with infinite prior \
        bounds.
    """
    from scipy.stats import norm

    output = str(tmpdir.mkdir("infinite_bounds"))

    class TestModel(Model):

        names = ["x", "y"]
        bounds = {"x": [0, 1], "y": [-np.inf, np.inf]}
        reparameterisations = {"x": "default", "y": None}

        def new_point(self, N=1):
            x = np.concatenate(
                [np.random.rand(N, 1), np.random.randn(N, 1)], axis=1
            )
            return numpy_array_to_live_points(x, self.names)

        def log_prior(self, x):
            log_p = np.log(self.in_bounds(x))
            log_p += norm.logpdf(x["y"])
            return log_p

        def log_likelihood(self, x):
            log_l = np.zeros(x.size)
            for n in self.names:
                log_l += norm.logpdf(x[n])
            return log_l

    fs = FlowSampler(
        TestModel(), output=output, nlive=500, plot=False, proposal_plots=False
    )
    fs.run(plot=False)
    assert fs.ns.condition <= 0.1


@pytest.mark.slow_integration_test
def test_constant_volume_mode(model, tmpdir):
    """Test sampling in constant volume mode"""
    output = str(tmpdir.mkdir("test"))
    fs = FlowSampler(
        model,
        output=output,
        nlive=500,
        plot=False,
        proposal_plots=False,
        constant_volume_mode=True,
    )
    fs.run(plot=False)


@pytest.mark.slow_integration_test
def test_prior_sampling(model, tmpdir):
    """Test prior sampling"""
    output = str(tmpdir.mkdir("prior_sampling"))
    fs = FlowSampler(
        model,
        output=output,
        nlive=100,
        plot=False,
        prior_sampling=True,
    )
    fs.run(plot=False)

    assert len(fs.nested_samples) == 100
    assert np.isfinite(fs.logZ)


@pytest.mark.slow_integration_test
def test_sampling_resume_finalised(model, tmp_path):
    """Test resuming the sampler after it finishes sampling"""
    output = tmp_path / "output"
    output.mkdir()
    fs = FlowSampler(
        model,
        output=output,
        nlive=100,
        plot=False,
    )
    fs.run(save=False, plot=False)
    assert os.path.exists(fs.ns.resume_file)

    fs = FlowSampler(
        model,
        output=output,
        nlive=100,
        plot=False,
    )

    fs.run(save=False, plot=False)


@pytest.mark.slow_integration_test
def test_debug_log_level(model, tmpdir):
    """Test running with debug log-level."""
    logger = logging.getLogger("nessai")
    original_level = logger.level
    logger.setLevel("DEBUG")
    output = str(tmpdir.mkdir("debug_logging"))
    fs = FlowSampler(
        model,
        output=output,
        nlive=100,
        plot=False,
    )
    fs.run(plot=False)
    logger.setLevel(original_level)
