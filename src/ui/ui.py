from services.calculator import Calculator

class UI:
    def __init__(self):
        pass

    def start():
        calculator = Calculator()
        print("")
        print("***LASKINSOVELLUS***")
        print("lopeta valitsemalla q ja Enter \n")

        while True:
            number = input("Anna ensimmäinen luku:\n ")
            if number == "q":
                quit()
            calculator.set_operand1(number)
            while True:
                select = input("\nAnna funktio: \n + summa \n - erotus \n" +
                               " * tulo \n / jako \n e toinen potenssi \n sq neliöjuuri:\n")
                if select not in ["+","-","*","/","e","sq"]:
                    print("\nVäärä valinta...yritä uudelleen\n")
                    continue
                if select in ["+","-","*","/"]:
                    number2 = input("\nAnna toinen luku:\n ")
                    result=calculator.count_two_operands(select,number2)
                else:
                    result=calculator.count_one_operands(select)
                break
            print("")
            if select in ["+","-","*","/"]:
                print("TULOS: " + str(number) + " " + str(select) + " " +
                      str(number2) + " = " +str(result)+"\n")
            else:
                print("TULOS: " + str(number) + " " + str(select) + " = " +str(result)+"\n")
