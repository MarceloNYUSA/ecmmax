import psycopg2.extras
import os


class PostgresqlDB(object):

    def __init__(self):
        self.db_connection_string=os.environ['db_url']
        self._db_connection = None
        self._db_cur = None

    def __open_connection(self):
        self._db_connection = psycopg2.connect(self.db_connection_string)
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        ret_val=dict
        try:
            self.__open_connection()
            self._db_cur.execute(query, params)
            desc=self._db_cur.description
            ret_val = [dict(zip([col[0] for col in desc], row))
            for row in self._db_cur.fetchall()]
        except psycopg2.ProgrammingError as perr:
            print(perr)
        except (Exception, psycopg2.DatabaseError) as err:
                err
        finally:
            self.__del()
            return ret_val
 

    def update(self, query, params):

        result=None
        try:
            self.__open_connection()
            result=self._db_cur.execute(query, params)
            self._db_connection.commit()
        except psycopg2.ProgrammingError as perr:
            print(perr)
        except (Exception, psycopg2.DatabaseError) as err:
                err
        finally:
            self.__del()
            
        return result

    def __del(self):
        self._db_connection.close()




