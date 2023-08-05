"""Manage Line and Cell magic parameters."""

from enum import Enum

from ppextensions.pputils.utils.exceptions import InvalidParameterType, MissingArgument


class WidgetType(Enum):
    """
    Widget Types.
    """
    TEXTBOX = "textbox"
    DROPDOWN = "dropdown"
    READ = "read"


class ParameterArgs:
    """
    Manage Line and Cell magic parameters.
    """

    def __init__(self, args):
        self.args = args

    def widget_type(self):
        """
            Get Widget type.
        """
        try:
            return WidgetType(getattr(self.args, 'type'))
        except ValueError:
            raise InvalidParameterType("Invalid parameter type. Only textbox or dropdown are supported.")

    def get(self, key):
        """
            Get parameter value.
        """
        if hasattr(self.args, key):
            param_value = getattr(self.args, key)
        else:
            raise MissingArgument(key)

        return param_value

    def hasattr(self, key):
        """
            Checks if paramter is present.
        """
        return hasattr(self.args, key)

    def get_list(self, key):
        """
            Get list of parameters.
        """
        return self.get(key).split(":::")
