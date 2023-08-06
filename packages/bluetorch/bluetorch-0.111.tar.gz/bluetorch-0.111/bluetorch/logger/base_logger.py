import numpy as np
import os
from datetime import datetime
# import torch
# import torch.nn.functional as F


class BaseLogger(object):
    def __init__(self, job, paths):
        self.config = job
        self.options = job.options
        self.params = job.params
        self.mode = job.mode
        self.dataset = job.dataset
        self.analysis = job.analysis
        self.epochs = job.options.epochs
        self.current_epoch = 0

        if job.exp_name is None:
            self.experiment_name = ''
        else:
            self.experiment_name = job.exp_name

        self.log_dir = paths['logs']
        self.checkpoint_path = self.get_checkpoint_path()
        # log_dir = os.path.join('logs', args.name + '_' + datetime.now().strftime('%b%d_%H%M'))

        # self.batch_size = job.options.batch_size
        # self.log_path = os.path.join(self.save_dir, '{}.log'.format(args.name))
        # self.epoch = args.start_epoch
        # Current iteration in epoch (i.e., # examples seen in the current epoch)
        self.iter = 0
        # Current iteration overall (i.e., total # of examples seen)
        # self.global_step = round_down((self.epoch - 1) * dataset_len, args.batch_size)
        # self.iter_start_time = None
        # self.epoch_start_time = None

    # def _log_scalars(self, scalar_dict, print_to_stdout=True):
    #     """Log all values in a dict as scalars to TensorBoard."""
    #     for k, v in scalar_dict.items():
    #         if print_to_stdout:
    #             self.write('[{}: {:.3g}]'.format(k, v))
    #         k = k.replace('_', '/')  # Group in TensorBoard by phase
    #         self.summary_writer.add_scalar(k, v, self.global_step)

    # def write(self, message, print_to_stdout=True):
    #     """Write a message to the log. If print_to_stdout is True, also print to stdout."""
    #     with open(self.log_path, 'a') as log_file:
    #         log_file.write(message + '\n')
    #     if print_to_stdout:
    #         print(message)

    def get_name(self):
        """Provide a unique name for the model"""
        raise NotImplementedError

    def get_checkpoint_path(self):
        """Model checkpoint_path"""
        # mode is ['debug', 'val', 'test']
        #FLAT Structure, does not include epoch info
        return '{}/{}/checkpoints/{}'.format(self.log_dir, self.mode, self.get_name())

    def logs_named_path(self):
        raise NotImplementedError

    def start_iter(self):
        """Log info for start of an iteration."""
        raise NotImplementedError

    def end_iter(self):
        """Log info for end of an iteration."""
        raise NotImplementedError

    def start_epoch(self):
        """Log info for start of an epoch."""
        raise NotImplementedError

    def end_epoch(self, metrics, curves):
        """Log info for end of an epoch. Save model parameters and update learning rate."""
        raise NotImplementedError
