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
=========
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

Aufgabe 2:
==========
Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.

In the above example:

    mxmxvkd contains dairy.
    sqjhc contains fish.
    fvjkl contains soy.

Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. 
(There should not be any spaces in your canonical dangerous ingredient list.) 
In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Algo:
-----
#task 2 - cleanup zutaten-allergen dir
# a) suche in AlergenByZutat nach Einträgen mit eine AlergenenListe mit Länge 1 -> Allergen_1
# b) suche in AlergenByZutat nach Einträgen mit einer AlergenenListe mit Länge > 1, die Durchschnitt mit Allergen_1 haben
# -> entfernte alle Allergen_1 einträge aus den Findings
# Abbruch, wenn in b) nichts mehr gefunden werden kann

'''
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

for a in allergen_set:
    zutaten = zutaten_set.copy()
    # Ermittle alle möglichen Zutaten aller foods die a enthaletn (könnten)
    for z,food_allergene in foods:
        if a in food_allergene:
            zutaten = zutaten.intersection(z)
    # die Differenzmenge dieser Zutaten kann jetzt NICHT mehr a enthalten -> streiche deshalb a raus
    andereZutaten = zutaten_set.difference(zutaten)
    for andereZutat in andereZutaten:
        AlergenByZutat[andereZutat].discard(a)

# menge der Zutaten, die keine Allergene entalten
ZutatenOhneAlergene = [z for z in zutaten_set if len(AlergenByZutat[z]) == 0]
# Wie oft befinden sich Zutaten in den Foods die ohne Alergene sind?
l1 = sum([len(set(zutaten).intersection(ZutatenOhneAlergene)) for (zutaten,_) in foods])
print("Task 1: (summe aller Zutaten ohne allergen in foods):", l1)

#task 2 - cleanup zutaten-allergen dir
# a) suche in AlergenByZutat nach Einträgen mit eine AlergenenListe mit Länge 1 -> Allergen_1
# b) suche in AlergenByZutat nach Einträgen mit einer AlergenenListe mit Länge > 1, die Durchschnitt mit Allergen_1 haben
# -> entfernte alle Allergen_1 einträge aus den Findings
# Abbruch, wenn in b) nichts mehr gefunden werden kann
weiter = True
while weiter:
    weiter = False
    # Menge von Alergen, für die gilt: len(ZutatenOhneAlergene)==1
    a_set = set()
    for a  in AlergenByZutat.values():
        if len(a) == 1:
            a_set = a_set.union(a)

    # finde zutaten die a und weitere Alergen enthalten
    z_list = [z for (z,a) in AlergenByZutat.items() if len(a.union(a_set))!=0 and len(a)>1]
    if z_list:
        weiter = True
        #lösche alle a_set
        for z in z_list:
            AlergenByZutat[z] = AlergenByZutat[z] - a_set
print("Task2")
# suche nun zutaten-allergen-Pärchen, mit len(Allergen)>0 (ist nicht leer)
l2 = [(z,a_item) for (z,a) in AlergenByZutat.items() if len(a)>0 for a_item in a]
# sortiere die Liste nach dem Allergen (dem zweiten Element des Tupels)
l2.sort(key=lambda tup: tup[1])
# Ausgabe der nach Alergen sorierten Zutaten(Komma getrennt)
print(",".join([z for (z,_) in l2]))