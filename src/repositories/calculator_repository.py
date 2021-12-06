class CalculatorRepository:
    """ Tietokantatallennuksesta vastaava luokka."""

    def __init__(self, connection):
        self._connection = connection

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from operations")

    def stats(self):
        '''statistiikka'''
        cursor = self._connection.cursor()
        res_all=cursor.execute("select count(*) from operations ").fetchone()[0]
        res = (0,0,0,0,0,0,0)
        if res_all != 0:
            res_add=cursor.execute("select count(*) from operations "
                                     " where operation='+'").fetchone()[0]
            res_sub=cursor.execute("select count(*) from operations "
                                     "where operation='-'").fetchone()[0]
            res_div=cursor.execute("select count(*) from operations "
                                     "where operation='/'").fetchone()[0]
            res_mul=cursor.execute("select count(*) from operations "
                                    "where operation='*'").fetchone()[0]
            res_sqrt=cursor.execute("select count(*) from operations where "
                                      "operation='sqrt'").fetchone()[0]
            res_exp=cursor.execute("select count(*) from operations "
                                     "where operation='exp'").fetchone()[0]
            res = (res_all,res_add,res_sub,res_div,res_mul,res_sqrt,res_exp)
        return res

    def add_operation(self,operator:str):
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO operations
         (operation)
            VALUES
          (?)
            """,(operator,))
        self._connection.commit()
