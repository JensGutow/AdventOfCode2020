'''
https://adventofcode.com/2020/day/21

--- Day 21: Allergen Assessment ---

You start by compiling a list of foods (your puzzle input), one food per line. 
Each line includes that food's ingredients list followed by some or all of the allergens the food contains.
Each allergen is found in exactly one ingredient. 
Each ingredient contains zero or one allergen. Allergens aren't always marked; 
when they're listed (as in (contains nuts, shellfish) after an ingredients list), 
the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. 
However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: 
    maybe they forgot to label it, or maybe it was labeled in a language you don't know.
For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)

The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. 
While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.
The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. 
In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. 
Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.
Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?

===========================================
Text Analyse
===========================================

Puzzle Input:
    mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
    trh fvjkl sbzzf mxmxvkd (contains dairy)
    sqjhc fvjkl (contains soy)
    sqjhc mxmxvkd sbzzf (contains fish)

------------------------------------------------------------
Foods	Ingiedients					Allergene
------------------------------------------------------------
0		mxmxvkd kfcds sqjhc nhms 	dairy fish
1		trh fvjkl sbzzf mxmxvkd 	dairy
2		sqjhc fvjkl 				soy
3		sqjhc mxmxvkd sbzzf 		fish
------------------------------------------------------------
	
- Foods besteht aus einer Liste von Food(s)
- Food besteht aus einer Liste von Ingredient(s) und einer Liste von Allergen(en)
- ein Ingriedient hat ein oder kein Allergen
- ein Allergen ist genau in einer Ingiedient
- Allergen list kann unvollständig (für das food) sein
	
Aufgabe_1:
	Finde heraus, welche Ingiedients haben KEINE Allergene und wie oft kommen diese in der Eingabeliste vor
	(Im Beispiel: kfcds, nhms, sbzzf, or trh -> enthalten kein Allergen)
		Das sind 4 Allergene, sbzzf kommt 2 mal, alle anderen 1 mal in der Eingabeliste vor -> Summe = 5

Mögliche Hilfsmitel:
    Dictionary	IngiedientByAllergen[alergen] 		
        alergen -> set of ingredients (leer oder eins)
        
    Dictionary 	AllergenByIngredient[ingredient]	???
        ingredient -> set of allergenen

Ideen:
    1) Wenn von 2 Foods der Durchshcnitt der Indredients leer ist 
        -> dann muss auch der Durchschnitt der Allergen leer sein
    
    Dh. Durchschintt der Zutaten ist leer (für Food k und j)
        dann können alle Indredients von K nicht in J sein (und umgekhert)
        z.b. Food 0: Indredients: mxmxvkd kfcds sqjhc nhms 

    Für ein Allergen a:
        Z ist die Menge aller Zutaten
        Z(a) = der Durchschnitt aller Zutaten von Foods die Allergene a haben
            -> nur diese können a enthalten
        Die Differenzmenge Z_not(a) = Z - Z(a) -> KANN NICHT a enthalten

    Algo:
        A : Menge aller Allergene
        für zutat in Z
        AlergenByZutat[zutat] = A
        for a in A:
            ermittle Z(a)
            Z_not = Z - Z(a)
            for z in Z_not:
                entferne Allergen a aus AlergenByZutat[zutat]
'''
import time
from collections import defaultdict, Counter

def get_puzzle(file_name):
    p = []
    zutaten = None
    allergene = None
    with open(file_name) as f:
        for zeile in f:
            zeile = zeile.replace(",","")
            zutaten, allergene = zeile.strip().split("(")
            zutaten = zutaten.strip().split(" ")
            allergene = allergene.strip().replace("contains ", "").replace(")","").split(" ")
            p.append((zutaten, allergene))
    return p

foods = get_puzzle("tag_21.txt")
zutaten_set = {zutat for (zutaten, _) in foods for zutat in zutaten}
allergen_set = {allergen for (_, allergene) in foods for allergen in allergene}

AlergenByZutat = {zutat:allergen_set.copy() for zutat in zutaten_set}

def print_alergene_by_zutat():
    for z, a in AlergenByZutat.items():
        print(z,a)

# print("start")
# print_alergene_by_zutat()
# print()

for a in allergen_set:
    zutaten = zutaten_set.copy()
    # Ermittle alle möglichen Zutaten aller foods die a enthaletn (könnten)
    for z,food_allergene in foods:
        if a in food_allergene:
            zutaten = zutaten.intersection(z)
    # die Differenzmenge dieser Zutaten kann jetzt NICHT mehr a enthateln -> streiche deshalb a raus
    andereZutaten = zutaten_set.difference(zutaten)
    for andereZutat in andereZutaten:
        AlergenByZutat[andereZutat].discard(a)

# print("end")
# print_alergene_by_zutat()

# menge der Zutaten, die keine Allergene entalten
ZutatenOhneAlergene = [z for z in zutaten_set if len(AlergenByZutat[z]) == 0]
#print("\nzutaten ohne allergene:", ZutatenOhneAlergene)
# Zähle, wie oft diese Zutaten in  der Eingabeliste vorkommen
l1 = sum([len(set(zutaten).intersection(ZutatenOhneAlergene)) for (zutaten,_) in foods  ])
print("summe aller Zutaten ohne allergen in foods:", l1)






    


# print("Zutaten (alle):", zutaten_set)
# print("Allergnee (alle):", allergen_set)

