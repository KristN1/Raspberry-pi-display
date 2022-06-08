from array import array


class Action(object):
    def __init__(self, action_type: str, data: list = None):
        self.action_type = action_type
        self.data = data