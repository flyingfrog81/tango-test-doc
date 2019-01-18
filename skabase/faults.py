"""General SKA Tango Device Exceptions."""


class SKABaseError(Exception):
    """Base class for all SKA Tango Device exceptions."""
    pass


class GroupDefinitionsError(SKABaseError):
    """Raise if error parsing or creating groups from GroupDefinitions."""
    pass