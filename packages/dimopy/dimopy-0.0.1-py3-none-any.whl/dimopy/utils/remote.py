import pymysql
from clickhouse_driver import Client
from pandas import DataFrame, read_sql


class ClickHouseDri(object):
    """
        连接clickhouse, 执行sql查询语句
    """

    def __init__(self,
                 host: str = "localhost",
                 port: int = 19101,
                 database: str = "db",
                 user: str = "default",
                 password: str = "123123"):
        self.client = Client(host=host, port=port, database=database, user=user, password=password)

    def execute(self, sql):
        try:
            res = self.client.execute(sql)
        except Exception as error_message:
            raise Exception(error_message)
        else:
            df = DataFrame(res)
            return df
        finally:
            self.client.disconnect()


class MySQLDri(object):
    """
        连接mysql, 执行sql查询语句
    """
    def __init__(self,
                 host: str = "localhost",
                 port: int = 3306,
                 database: str = "db",
                 user: str = "default",
                 password: str = "123123"):
        self.client = pymysql.connect(host=host, port=port, database=database, user=user, password=password)

    def execute(self, sql):
        try:
            df = read_sql(sql, con=self.client)
        except Exception as error_message:
            raise Exception(error_message)
        else:
            return df
        finally:
            self.client.close()