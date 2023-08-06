import copy
import torch.nn as nn
import numpy as np
from .experiment_util import grid_2_jobs
from .experiment_util import grid_2_jobs_v2

class BaseExperiment:
    """
    Base experiment class
    """
    def __init__(self, config):
        self.config = config
        self.exp_name = config.exp_name
        self.description = config.description
        self.question = config.question

        self.model = config.model
        self.dataset = config.dataset
        self.mode = config.mode

        self.options = config.options
        self.params = config.params
        # self.logger = logging.getLogger(self.__class__.__name__)

    def get_jobs(self):
        jobs = grid_2_jobs_v2(copy.deepcopy(self.config))
        for job in jobs:
            job.analysis = False
        return jobs


class BaseAnalysis(BaseExperiment):
    """
    Base analysis class
    Special that it saves things to analysis dir
    Only loads models, does not train them
    """
    def __init__(self, config):
        super(BaseAnalysis, self).__init__(config)

        # self.logger = logging.getLogger(self.__class__.__name__)

    def get_jobs(self):
        jobs = grid_2_jobs_v2(copy.deepcopy(self.config))
        for job in jobs:
            job.analysis = True
            assert job.options.epochs == 0
        return jobs
