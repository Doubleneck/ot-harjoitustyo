from services.operations import Operations
print("****************************************************************************************************************************")
print("LASKINSOVELLUS DEMO")
print("")
while True:
    print("")
    number1 = input("Anna ensimmäinen luku (q lopettaa):")
    if number1 =="q":
        quit()
    while True:
        print("")  
        select = input("Valitse funktio: \n  + summa \n  - erotus \n  * tulo \n  / osamäärä \n  e toinen potenssi \n  sq neliöjuuri\n")
        if select not in ["+","-","*","/","e","sq"]:
            print("Virheellinen valinta...yritä uudelleen")
            continue
        if select == "q":
            quit()             
        if select in ["+","-","*","/"]:  
            number2 = input("Anna toinen luku:(q lopettaa)")
            if number2 =="q":
                quit()
            if select =="+":
                result = Operations.sum_func(number1,number2)  
            if select =="-":
                result = Operations.sub_func(number1,number2) 
            if select =="*":
                result = Operations.mul_func(number1,number2) 
            if select =="/":
                result = Operations.div_func(number1,number2) 
            if select =="e":
                result = Operations.exp_func(number1,number2) 
            if select =="sq":
                result = Operations.sqrt_func(number1,number2)                              
        else:
            if select == "e":
                result == Operations.exp_func(number1)
            if select == "sq":
                result == Operations.sqrt_func(number1)    
        if select in ["+","-","*","/"]:
            print("TULOS:"+ str(number1)+" "+str(select)+" "+str(number2)+" = "+str(result) + "\n" )    
            break
        else:
            print("TULOS:"+ str(number1)+" "+str(select)+" = "+str(result) + "\n") 
            break