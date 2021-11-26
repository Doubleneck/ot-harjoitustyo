from database_connection import get_database_connection

class CalculatorRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        list=[]
        result=cursor.execute("select * from operations").fetchall()
        for i in range(0, len(result)) :
            list.append(result[i])     
        return list

    def stats_plus(self):
        '''antaa plussien määrän'''
        cursor = self._connection.cursor()
        resultall=cursor.execute("select count(*) from operations ").fetchone()
        resultplus=cursor.execute("select count(*) from operations where operation='+'").fetchone()
        jakaja=resultplus[0]
        #print(jakaja)
        jaettava=resultall[0]
        return resultplus
         

    def add_operation(self,operator:str):
        cursor = self._connection.cursor()     
        cursor.execute("""
            INSERT INTO operations
         (operation)
            VALUES
          (?)
            """,operator)
        self._connection.commit()
#calculator_repository = CalculatorRepository(get_database_connection())
#operations =  calculator_repository.findall()           
