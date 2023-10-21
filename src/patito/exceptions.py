"""Module containing all custom exceptions raised by patito."""

class ValidationError(Exception):
    """Exception raised when dataframe does not match schema."""
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class ErrorWrapper(Exception):
    """Wrapper for specific column validation error."""
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class WrongColumnsError(TypeError):
    """Validation exception for column name mismatches."""


class MissingColumnsError(WrongColumnsError):
    """Exception for when a dataframe is missing one or more columns."""


class SuperflousColumnsError(WrongColumnsError):
    """Exception for when a dataframe has one ore more non-specified columns."""


class MissingValuesError(ValueError):
    """Exception for when a dataframe has non-nullable columns with nulls."""


class ColumnDTypeError(TypeError):
    """Exception for when a dataframe has one or more columns with wrong dtypes."""


class RowValueError(ValueError):
    """Exception for when a dataframe has a row with a impermissible value."""


class RowDoesNotExist(RuntimeError):
    """Exception for when a single row was expected, but none were returned."""


class MultipleRowsReturned(RuntimeError):
    """Exception for when a single row was expected, but several were returned."""
