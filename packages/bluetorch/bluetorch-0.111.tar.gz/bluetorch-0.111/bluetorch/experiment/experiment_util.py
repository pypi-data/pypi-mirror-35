import copy
import argparse
import itertools

def grid_2_jobs(config):
    # Config needs to have an options and params
    jobs = []
    option_keys = []
    option_vals = []
    for (key, vals) in config.options._get_kwargs():
        option_keys.append(key)
        option_vals.append(vals)

    param_keys = []
    param_vals = []
    for (key, vals) in config.params._get_kwargs():
        param_keys.append(key)
        param_vals.append(vals)


    f = list(itertools.product(*option_vals, *param_vals))

    num_opts = len(option_keys)
    all_keys = list(itertools.chain(option_keys, param_keys))

    for setting in f:
        job = argparse.Namespace()
        job.options = argparse.Namespace()
        job.params = argparse.Namespace()
        job_options = vars(job.options)
        job_params = vars(job.params)

        for i, (key, value) in enumerate(zip(all_keys, setting)):
            if i < num_opts:
                job_options[key] = value
            else:
                job_params[key] = value
        jobs.append(copy.deepcopy(job))

    return jobs

def grid_2_jobs_v2(config):
    # Config needs to have an options and params
    jobs = []
    config_keys = []
    config_vals = []
    for (key, vals) in config._get_kwargs():
        if type(vals) in list([type([]), type(set())]):
            config_keys.append(key)
            config_vals.append(vals)
        elif type(vals) == type(argparse.Namespace()):
            pass
        else:
            config_keys.append(key)
            config_vals.append({vals})


    option_keys = []
    option_vals = []
    for (key, vals) in config.options._get_kwargs():
        option_keys.append(key)
        if type(vals) in list([type([]), type(set())]):
            option_vals.append(vals)
        else:
            option_vals.append({vals})

    param_keys = []
    param_vals = []
    for (key, vals) in config.params._get_kwargs():
        param_keys.append(key)
        if type(vals) in list([type([]), type(set())]):
            param_vals.append(vals)
        else:
            param_vals.append({vals})



    f = list(itertools.product(*config_vals, *option_vals, *param_vals))

    num_config_keys = len(config_keys)
    num_opts_keys = len(option_keys)
    num_para_keys = len(param_keys)

    all_keys = list(itertools.chain(config_keys, option_keys, param_keys))
    for setting in f:
        job = argparse.Namespace()
        job_dict = vars(job)
        job.options = argparse.Namespace()
        job.params = argparse.Namespace()
        job_options = vars(job.options)
        job_params = vars(job.params)

        for i, (key, value) in enumerate(zip(all_keys, setting)):
            if i < num_config_keys:
                job_dict[key] = value
            elif i < num_opts_keys+num_config_keys:
                job_options[key] = value
            else:
                job_params[key] = value
        jobs.append(copy.deepcopy(job))
    return jobs