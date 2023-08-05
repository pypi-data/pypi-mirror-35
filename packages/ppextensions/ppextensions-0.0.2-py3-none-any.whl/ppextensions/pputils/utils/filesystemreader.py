"""Reading and Managing PPExtensions Configuration."""

import os


class FileSystemReaderWriter:
    """
    Credits: Thanks to 'SPARKMAGIC' for FileSystemReader.
    """

    def __init__(self, path):
        assert path is not None
        self.path = os.path.expanduser(path)

    def ensure_path_exists(self):
        """
        Ensure PPExtensions path exists in user's home.
        """
        FileSystemReaderWriter._ensure_path_exists(self.path)

    def ensure_file_exists(self):
        """
        Ensure PPExtensions configuration file exists.
        """
        self._ensure_path_exists(os.path.dirname(self.path))
        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def read_lines(self):
        """
        Read PPExtensions Configuration.
        """
        if os.path.isfile(self.path):
            with open(self.path, "r+") as config_file:
                return config_file.readlines()
        else:
            return ""

    def overwrite_with_line(self, line):
        """
        Write additional configuration to PPExtensions.
        """
        with open(self.path, "w+") as f:
            f.writelines(line)

    @staticmethod
    def _ensure_path_exists(path):
        """
        Creates a path to PPExtensions configuration.
        """
        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise
