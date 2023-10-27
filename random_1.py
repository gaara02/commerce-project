#!/usr/bin/env python3
import random


nom = ["Moussa","Aliou", "cheikh", "Mamadou","Fallou", "Amadou"]
Age = [12,15,13,16,67]

valeurs_utilisees = []

for i in range(3) :
    val1 = random.choice(nom)
    val2 = random.choice(Age)
    while val1 in valeurs_utilisees :
        val1 = random.choice(nom)
    valeurs_utilisees.append(val1)
    print("{} : {}".format(val1, val2))