class TimeLibError(Exception):
    """Generic error for timelib."""

    def __init__(self, message='Something bad occurred in library'):
        super().__init__(message)


class NotFoundError(TimeLibError):
    """Raised when requested object doesn't exist."""


class DifferentPlanError(NotFoundError):
    """Raised when related planned tasks from different plans."""


class InvalidActionError(TimeLibError):
    """Raises when action cannot be performed."""


class StorageError(TimeLibError):
    """Raises from internal storage exceptions."""

    def __init__(self, message='Storage exception occurred'):
        super().__init__(message)


class TimeLibWarning(Warning):
    """Generic warning for timelib."""


class ActionAlreadyPerformedWarning(TimeLibWarning):
    """Warned when action already performed."""


class ForeignRelatedTaskWarning(TimeLibWarning):
    """Warned when user is not member of related task."""
