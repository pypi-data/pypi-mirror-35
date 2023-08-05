"""Base class for all connections. Each connection will implement this class."""

import abc


class BaseConnection:
    def __init__(self, connection):
        self.connection = connection

    def __del__(self):
        try:
            if self.connection:
                self.connection.close()
        except BaseException:
            pass

    @abc.abstractmethod
    def execute(self, sql, displaylimit, progress_bar=False):
        """
        Executes sql.
        :param progress_bar:
        :param sql:
        :return:
        """
