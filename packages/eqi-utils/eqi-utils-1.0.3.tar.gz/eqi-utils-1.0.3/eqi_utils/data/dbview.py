import cx_Oracle
import pandas as pd

from eqi_utils.config import keys
from eqi_utils.config.config import EQI_CONFIG


def _oracle_connection():
    username = EQI_CONFIG.get_mandatory(keys.DB_USER)
    password = EQI_CONFIG.get_optional(keys.DB_PASSWORD, None)
    if password is None:
        password = input('Please input db password')
    db_name = EQI_CONFIG.get_optional(keys.DB_NAME, 'RESLIVESRV')
    return cx_Oracle.connect(username, password, db_name)


def load_to_df(query):
    """
    Load dataframe from the result of a SQL query
    :param query: SQL query
    :return: Pandas DataFrame containing the SQL query result
    """
    connection = _oracle_connection()
    with connection:
        df = pd.read_sql_query(query, connection)
    return df
