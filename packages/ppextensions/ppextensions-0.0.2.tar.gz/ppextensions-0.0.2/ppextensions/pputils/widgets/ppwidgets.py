"""IPyWidgets for PPExtensions."""

from ppextensions.pputils.utils.exceptions import ParameterNotDefined

from .widgets import ParameterBox
from .widgetsfactory import WidgetsFactory


class ParameterWidgets:
    """
        Widget to drive user driven parameters.
    """

    def __init__(self, shell):
        super(ParameterWidgets, self).__init__()
        self._shell = shell
        # exec (shell, "from pputils.widgets.widgets import ParameterBox", shell.user_ns)
        # exec (shell, "_para_box = ParameterBox()", shell.user_ns)
        self._para_box = ParameterBox()
        self._enabled = False
        self._child = {}
        self._data = {}
        self._enable_()

    def _enable_(self):
        self._enabled = True
        self._para_box.display()

    def text(self, name, default_value, label='', observer=None):
        """
        Gives a text box for a parameter to be used in notebook.
        :param name: name of the parameter
        :param default_value: default value for the parameter.
        :param label: Is a placeholder to be used later.
        :return:
        """
        if not self._enabled:
            self._enable_()

        child = WidgetsFactory.get_text(
            value=default_value,
            description=name,
        )
        self._child[name] = child
        self._para_box.add_child(child)
        self._register_observer_(child, observer)
        self._set_values_(name, default_value)

    def dropdown(self, name, default_value, sequence, label='', observer=None):
        """
        Gives a dropdown for a parameter to be used in notebook.
        :param name: name of the parameter
        :param default_value: default value for the parameter.
        :param sequence: sequence of values for dropdown.
        :param label: is a placeholder to be used later.
        :return:
        """
        if not self._enabled:
            self._enable_()

        child = WidgetsFactory.get_dropdown(
            value=default_value,
            description=name,
            options=sequence,
        )
        self._child[name] = child
        self._para_box.add_child(child)
        self._register_observer_(child, observer)
        self._set_values_(name, default_value)

    def _register_observer_(self, child, observer=None):
        child.observe(self._update_shell_value_, names='value')
        if observer:
            child.observe(observer, names='value')

    def _update_shell_value_(self, event):
        # print("Changing value")
        # print(event)
        self._set_values_(event['owner'].description, event['new'])

    def disable_widgets(self):
        """
        Disables all widgets so user won't be able to change any values.
        :return:
        """
        for name in self._child:
            self._child[name].disabled = True

    def enable_widgets(self):
        """
        Enables all widgets so user will be able to change values.
        :return:
        """
        for name in self._child:
            self._child[name].disabled = False

    def _set_values_(self, name, value):
        self._data[name] = value
        self._shell.user_ns[name] = value

    def get(self, name):
        """
        Gives the value of the parameter set/changed.
        :param name: parameter name.
        :return: parameter value
        """
        if name in self._data:
            return self._data[name]
        else:
            raise ParameterNotDefined(name)
