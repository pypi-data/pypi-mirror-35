"""Get IPyWidgets."""
from ipywidgets import VBox, Output, Button, HTML, HBox, Dropdown, Checkbox, ToggleButtons, Text, Textarea, Tab, Password


class WidgetsFactory:

    @staticmethod
    def get_vbox(**kwargs):
        """
        Get VBox Widget.
        """
        return VBox(**kwargs)

    @staticmethod
    def get_output(**kwargs):
        """
            Get Output.
        """
        return Output(**kwargs)

    @staticmethod
    def get_button(**kwargs):
        """
            Get Button.
        """
        return Button(**kwargs)

    @staticmethod
    def get_html(value, **kwargs):
        """
            Get HTML.
        """
        return HTML(value, **kwargs)

    @staticmethod
    def get_hbox(**kwargs):
        """
            Get HBox Widget.
        """
        return HBox(**kwargs)

    @staticmethod
    def get_dropdown(**kwargs):
        """
            Get Dropdown Widget.
        """
        return Dropdown(**kwargs)

    @staticmethod
    def get_checkbox(**kwargs):
        """
            Get Checkbox Widget.
        """
        return Checkbox(**kwargs)

    @staticmethod
    def get_toggle_buttons(**kwargs):
        """
            Get Toggle Buttons.
        """
        return ToggleButtons(**kwargs)

    @staticmethod
    def get_text(**kwargs):
        """
            Get Text.
        """
        return Text(**kwargs)

    @staticmethod
    def get_password(**kwargs):
        """
            Get Password Widget.
        """
        return Password(**kwargs)

    @staticmethod
    def get_text_area(**kwargs):
        """
            Get Text Area.
        """
        return Textarea(**kwargs)

    @staticmethod
    def get_tab(**kwargs):
        """
            Get Tab.
        """
        return Tab(**kwargs)
