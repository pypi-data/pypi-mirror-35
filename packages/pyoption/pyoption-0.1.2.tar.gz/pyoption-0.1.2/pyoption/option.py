class Some(object):
    """Represents a non-null result"""
    def __init__(self, value):
        self.value = value

    def unwrap(self):
        """Returns the result value or raisesn an error if None"""
        if self.value is not None:
            return self.value
        raise RuntimeError('Value is None')

    def unwrap_or(self, default_value):
        """Returns a default value if None"""
        return self.value or default_value

    def unwrap_or_else(self, callback):
        """Compute the return value of a callback if None"""
        return self.value or callback()

    def expect(self, error_message):
        """Returns the result value or raises an error if None"""
        if self.value is not None:
            return self.value
        raise RuntimeError(error_message)

    def is_some(self):
        return not self.is_none()

    def is_none(self):
        return self.value is None
