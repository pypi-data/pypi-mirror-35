class HatcherException(Exception):
    pass


class MissingFilenameError(HatcherException):
    pass


class MissingPlatformError(HatcherException):
    pass


class ChecksumMismatchError(HatcherException):
    pass


class InvalidBundle(HatcherException):
    """ Raised when a bundle file is invalid."""


class TargetFileExists(HatcherException):
    """ Raised when trying to save a file to an existing path."""


class InvalidRuntime(HatcherException):
    pass


class InvalidEgg(HatcherException):
    pass
