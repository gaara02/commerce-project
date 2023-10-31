#!/usr/bin/env python3

#Ce code permet de generer aleatoirement de donnees
import random


nom = ["Moussa","Aliou", "cheikh", "Mamadou","Fallou", "Amadou"]
Age = [12,15,13,16,67]



for i in range(3) :
    val1 = random.choice(nom)
    val2 = random.choice(Age)
   
    print("{} : {}".format(val1, val2))