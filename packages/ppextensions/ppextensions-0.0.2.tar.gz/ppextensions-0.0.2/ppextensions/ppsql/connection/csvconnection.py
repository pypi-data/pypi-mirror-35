"""This class enables working with CSV files. Implements BaseConnection."""

import re
import pandas as pd

from IPython import get_ipython

from ppextensions.ppsql.connection.basesql import BaseConnection
from ppextensions.pputils.utils.exceptions import InvalidParameterType


class CSVConnection(BaseConnection):
    first_run = True
    dflist = []

    def __init__(self):
        super(CSVConnection, self).__init__('')

    def execute(self, sql):
        return self._execute_csv_data_(str(sql))

    def _execute_csv_data_(self, query):
        """ Parse the sql query csv fields Returns the required csv results for persisted dataframe.
        """
        ipython = get_ipython()
        if self.first_run:
            ipython.magic("reload_ext sql")
        self.first_run = False
        try:
            filename = re.split("from", query, 1, flags=re.IGNORECASE)[1].split()[0]
            df_name = filename.replace("/", "_").replace(" ", "_").replace(".", "_").replace(":", "_").replace("-", "")
        except BaseException:
            raise InvalidParameterType("Problem in select query. Type the correct query and try again")
        if df_name in self.dflist:
            query = query.replace(filename, df_name)
            result = ipython.magic("sql {}".format(query))
        else:
            query = query.replace(filename, df_name)
            try:
                if filename.endswith('.tsv'):
                    exec('{}= pd.read_csv(\'{}\',sep=\'\\t\')'.format(df_name, filename))
                else:
                    exec('{}= pd.read_csv(\'{}\')'.format(df_name, filename))
            except IOError:
                raise IOError('File %s does not exist. Please type correct file name and try again' % (filename))
            ipython.magic("sql sqlite://")
            ipython.magic("sql persist {}".format(df_name))
            self.dflist.append(df_name)
            result = ipython.magic("sql {}".format(query))
        return result
