import os
import logging
from collections import OrderedDict
from typing import Union, List
import operator

from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

from smac.configspace import Configuration
from smac.runhistory.runhistory import RunHistory
from smac.utils.validate import Validator

from cave.feature_analysis.feature_analysis import FeatureAnalysis
from cave.plot.cdf import plot_cdf
from cave.plot.configurator_footprint import ConfiguratorFootprintPlotter
from cave.plot.parallel_coordinates import ParallelCoordinatesPlotter
from cave.reader.configurator_run import ConfiguratorRun
from cave.utils.helpers import get_cost_dict_for_config, get_timeout, combine_runhistories, NotApplicableError, MissingInstancesError
from cave.utils.timing import timing
from cave.plot.cost_over_time import CostOverTime

__author__ = "Joshua Marben"
__copyright__ = "Copyright 2017, ML4AAD"
__license__ = "3-clause BSD"
__maintainer__ = "Joshua Marben"
__email__ = "joshua.marben@neptun.uni-freiburg.de"


class Analyzer(object):
    """
    This class serves as an interface to all the individual analyzing and
    plotting components. The plotter object is responsible for the actual
    plotting of things, but should not be invoked via the facade (which is
    constructed for cmdline-usage).
    """

    def __init__(self,
                 default,
                 incumbent,
                 scenario,
                 output_dir,
                 pimp_max_samples,
                 fanova_pairwise=True,
                 rng=None):
        """
        Parameters
        ----------
        default, incumbent: Configuration
            default and overall incumbent
        scenario: Scenario
            the scenario object
        output_dir: string
            output_dir-directory
        pimp_max_sample: int
            to configure pimp-run
        fanova_pairwise: bool
            whether to do pairwise importance
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)
        self.rng = rng
        if not self.rng:
            self.logger.info("No randomstate passed. Generate deterministic random state.")
            self.rng = np.random.RandomState(42)

        # Important objects for analysis
        self.scenario = scenario
        self.default = default
        self.incumbent = incumbent
        self.evaluators = []
        self.output_dir = output_dir

        # Save parameter importances evaluated as dictionaries
        # {method : {parameter : importance}}
        self.param_imp = OrderedDict()
        self.feat_importance = None  # Used to store dictionary for feat_imp

        self.pimp_max_samples = pimp_max_samples
        self.fanova_pairwise = fanova_pairwise

