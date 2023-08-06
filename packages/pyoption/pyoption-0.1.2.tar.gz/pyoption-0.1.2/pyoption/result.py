class Ok(object):
    """Represents a successful result"""
    def __init__(self, value):
        self.value = value

    def unwrap(self):
        """Returns the result value"""
        return self.value

    def expect(self, error_message):
        """Returns the result value"""
        return self.value

    def unwrap_err(self, error_message):
        """Raises an error using the result value as message"""
        raise RuntimeError(self.value)

    def expect_err(self, error_message):
        """Raises an error using the result value and prepending the given message"""
        raise RuntimeError('%s: %s' % (error_message, self.value))

    def is_ok(self):
        return True

    def is_err(self):
        return False


class Err(object):
    """Represents an error"""
    def __init__(self, error_message):
        self.error_message = error_message

    def unwrap(self):
        """Raise an error using the given message"""
        raise RuntimeError(self.error_message)

    def expect(self, message):
        """Raise an error prepending the given message to the error message"""
        raise RuntimeError('%s: %s' % (message, self.error_message))

    def unwrap_err(self, message):
        """Returns the yielded error message"""
        return self.error_message

    def expect_err(self, message):
        """Returns the yielded error message"""
        return self.error_message

    def is_ok(self):
        return False

    def is_err(self):
        return True

def Result(left_value, right_value):
    """Shortcut to define Ok or Err object"""
    if left_value is None:
        return Err(right_value)
    return Ok(left_value)