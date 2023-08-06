import abc


class Switcher(object, metaclass=abc.ABCMeta):
    """An abstract base class for creating a switcher (i.e. a Pythonic switch statement)
    """
    @abc.abstractmethod
    def handle_action(self, action):
        raise NotImplementedError('user must define handle_action to use this base class')
