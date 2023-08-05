"""Printing log messages from PPExtensions to Notebook."""

from IPython.display import display

from .widgetsfactory import WidgetsFactory


class UserMessages:
    """
    Printing log messages from PPExtensions to Notebook.
    """

    def __init__(self):
        self._init_html_()

    def _init_html_(self):
        self.html = WidgetsFactory.get_html(
            value=''
        )
        display(self.html)

    def info(self, message, new_line=False):
        """
        Print INFO logging to Notebook.
        """
        if new_line:
            self._init_html_()
        self.html.value = '<font color="34495E">{}</front>'.format(message.replace("\n", "<br/>"))

    def warning(self, message, new_line=False):
        """
        Print WARNING logging to Notebook.
        """
        if new_line:
            self._init_html_()
        self.html.value = '<font color="orange">{}</front>'.format(message.replace("\n", "<br/>"))

    def error(self, message, new_line=False):
        """
        Print Error logging to Notebook.
        """
        if new_line:
            self._init_html_()
        self.html.value = '<font color="red">{}</front>'.format(message.replace("\n", "<br/>"))
