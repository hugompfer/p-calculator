# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:03:08 2020

@author: Hugo
"""

import options
import operators as op

operatorsByChoice = {
    "1": op.multiply, 
    "2": op.div,
    "3": op.sum,
    "4": op.sub
}
 
choice = "-1"

while(choice != "0"):
    print(options.GetOptions())
    choice = input("> ")
    
    if(choice in operatorsByChoice):
        num1 = float(input("1º número > "))
        num2 = float(input("2º número >  "))
        print("Resultado = ", operatorsByChoice[choice](num1, num2), "\n")
        
    elif (choice == "0"):
        continue;
        
    else:
        print("\nOpção inválida.") 



