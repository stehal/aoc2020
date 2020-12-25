from collections import defaultdict
import copy

allergenmap = defaultdict(list)

ingredientmap = defaultdict(list)

allingredients = set()
allallergens = set()

ingredients_allergens = []

for s in open("input"):
    ingredientstring, allergenstring =s.split("(contains")
    ingredientset = {i for i in ingredientstring.strip().split(" ")}
    for allergen in allergenstring.strip().replace(")", "").replace(',','').split():
        allergenmap[allergen].append(ingredientset)
    allingredients = allingredients.union(ingredientset)
    allergenset = {a for a in allergenstring.strip().replace(")", "").replace(',','').split()}
    allallergens = allallergens.union(allergenset)
    ingredients_allergens.append([ingredientset, allergenset])
    

ia = copy.deepcopy(ingredients_allergens)

def removeall(ingredient, allergen):
     for p in ingredients_allergens:
        if ingredient in p[0]:
            p[0].remove(ingredient)
        if allergen in p[1]:
            p[1].remove(allergen)

def removeingredients(ingredient):
     for listofsets in allergenmap.values():
         for iset in listofsets:
             if ingredient in iset:
                 iset.remove(ingredient)
     
ingredientwithallergen = set()
allergenwithingredient = set()
awi = {}

while True:
    numberfound = len(ingredientwithallergen)
    for allergen in allallergens:
        if len(allergenmap[allergen]) > 0:
            possible_ingredients = set.intersection(*allergenmap[allergen])
            if len(possible_ingredients) == 1:
                ingredient = possible_ingredients.pop()
                ingredientwithallergen.add(ingredient)
                allergenwithingredient.add(allergen)
                awi[allergen] = ingredient
                removeingredients(ingredient)

    for allergen in allergenwithingredient:
        if allergen in allergenmap.keys():
            allergenmap.pop(allergen)
        if allergen in allallergens:
            allallergens.remove(allergen)
        
   
    if len(ingredientwithallergen) == numberfound:
        break

noallergens = allingredients.difference(ingredientwithallergen)
count = 0
for pair in ia:
    count += len(noallergens.intersection(pair[0]))
print("part 1", count)

sortedallogens = sorted(awi.keys())
listi = []
for k in sortedallogens:
    listi.append(awi[k])

print("part 2",','.join(listi))
    

