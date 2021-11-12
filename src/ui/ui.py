from services.operations import Operations
from services.calculator import Calculator

class UI:
    def __init__(self):
        pass

    def start():
        print("")
        print("***LASKINSOVELLUS***")
        print("lopeta valitsemalla q ja Enter \n")

        while True:
            number1 = input("Anna ensimmäinen luku: ")
            if number1 == "q":
                quit()
            while True:
                select = input("Anna funktio: \n + summa \n - erotus \n * tulo \n / jako \n e toinen potenssi \n sq neliöjuuri:\n" )
                if select not in ["+","-","*","/","e","sq"]:
                    print("Väärä valinta...yritä uudelleen")
                    continue    
                if select in ["+","-","*","/"]:     
                    number2 = input("Anna toinen luku: ")             
                    result=Calculator.count_two_operands(number1,select,number2)  
                    break
                else:
                    result=Calculator.count_one_operands(number1,select) 
                    break
            print("")
            if select in ["+","-","*","/"]:                          
                print("TULOS: " + str(number1) + " " + str(select) + " " + str(number2) + " = " +str(result)+"\n")
            else:
                print("TULOS: " + str(number1) + " " + str(select) + " = " +str(result)+"\n")  
