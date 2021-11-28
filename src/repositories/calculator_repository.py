class CalculatorRepository:
    def __init__(self, connection):
        self._connection = connection

    def stats(self):
        '''statistiikka'''
        cursor = self._connection.cursor()
        res_all=cursor.execute("select count(*) from operations ").fetchone()[0]
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
            return (res_all,res_add,res_sub,res_div,res_mul,res_sqrt,res_exp)                         

#            add=format(int(resultadd)*100/int(resultall),".1f")
#            sub=format(int(resultsub)*100/int(resultall),".1f")
#            div=format(int(resultdiv)*100/int(resultall),".1f")
#            mul=format(int(resultmul)*100/int(resultall),".1f")
#            sqrt=format(int(resultsqrt)*100/int(resultall),".1f")
#            exp=format(int(resultexp)*100/int(resultall),".1f")
#            print("***********LASKUTILASTOT************")
#            print ("operaatiota '+' laskettu " + str(resultadd) +
#                   " kertaa, "+ str(add) + "% kaikista")
#            print ("operaatiota '-' laskettu " + str(resultsub) +
#                   " kertaa, "+ str(sub) + "% kaikista")
#            print ("operaatiota '/' laskettu " + str(resultdiv) +
#                   " kertaa, "+ str(div) + "% kaikista")
#            print ("operaatiota '*' laskettu " + str(resultmul) +
#                   " kertaa, "+ str(mul) + "% kaikista")
#            print ("operaatiota 'sqrt' laskettu " + str(resultsqrt) +
#                   " kertaa, "+ str(sqrt) + "% kaikista")
#            print ("operaatiota 'exp' laskettu " + str(resultexp) +
#                   " kertaa, "+ str(exp) + "% kaikista")
        else:
            return 0
            #print ("Ei laskettuja laskutoimituksia")

    def add_operation(self,operator:str):
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO operations
         (operation)
            VALUES
          (?)
            """,(operator,))
        self._connection.commit()
