#from database_connection import get_database_connection

class CalculatorRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        list=[]
        result=cursor.execute("select * from operations").fetchall()
        for r in result:
            list.append(r[0])     
        return list

    def stats(self):
        '''statistiikka'''
        cursor = self._connection.cursor()
        resultall=cursor.execute("select count(*) from operations ").fetchone()[0]
        if resultall != 0:
            resultadd=cursor.execute("select count(*) from operations where operation='+'").fetchone()[0]
            resultsub=cursor.execute("select count(*) from operations where operation='-'").fetchone()[0]
            resultdiv=cursor.execute("select count(*) from operations where operation='/'").fetchone()[0]
            resultmul=cursor.execute("select count(*) from operations where operation='*'").fetchone()[0]
            resultsqrt=cursor.execute("select count(*) from operations where operation='sqrt'").fetchone()[0]
            resultexp=cursor.execute("select count(*) from operations where operation='exp'").fetchone()[0]
            add=format(int(resultadd)*100/int(resultall),".1f")
            sub=format(int(resultsub)*100/int(resultall),".1f")
            div=format(int(resultdiv)*100/int(resultall),".1f")
            mul=format(int(resultmul)*100/int(resultall),".1f")
            sqrt=format(int(resultsqrt)*100/int(resultall),".1f")
            exp=format(int(resultexp)*100/int(resultall),".1f")
            print("***********LASKUTILASTOT************")
            print ("operaatiota '+' laskettu " + str(resultadd) + " kertaa, "+ str(add) + "% kaikista")
            print ("operaatiota '-' laskettu " + str(resultsub) + " kertaa, "+ str(sub) + "% kaikista")
            print ("operaatiota '/' laskettu " + str(resultdiv) + " kertaa, "+ str(div) + "% kaikista")
            print ("operaatiota '*' laskettu " + str(resultmul) + " kertaa, "+ str(mul) + "% kaikista")
            print ("operaatiota 'sqrt' laskettu " + str(resultsqrt) + " kertaa, "+ str(sqrt) + "% kaikista")
            print ("operaatiota 'exp' laskettu " + str(resultexp) + " kertaa, "+ str(exp) + "% kaikista")
        else:
            print ("Ei laskettuja laskutoimituksia")

    def add_operation(self,operator:str):
        cursor = self._connection.cursor()     
        cursor.execute("""
            INSERT INTO operations
         (operation)
            VALUES
          (?)
            """,(operator,))
        self._connection.commit()
#calculator_repository = CalculatorRepository(get_database_connection())
#operations =  calculator_repository.findall()           
