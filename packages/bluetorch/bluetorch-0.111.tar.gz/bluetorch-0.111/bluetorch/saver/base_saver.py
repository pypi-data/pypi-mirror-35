

class BaseSaver(object):
    """Class to save and load model ckpts."""
    def __init__(self):
        super(BaseSaver, self).__init__()

    def save_checkpoint(self, model, logger):
        """
        Save the Model and whatever else
        is necessary
        :return: Nothin
        """
        raise NotImplementedError

    def load_checkpoint(self, model, logger):
        """
        Forward pass logic

        :return: model and logger
        """
        raise NotImplementedError