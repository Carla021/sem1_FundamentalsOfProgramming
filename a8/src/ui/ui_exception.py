class UIException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self._msg)