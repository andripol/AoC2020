from collections import defaultdict
import collections

lines = [i for i in open('21.txt').readlines()]
food = [[j for j in i.split(' (contains ')[0].split(' ')] for i in lines]
allergens = [[j.strip(', ') for j in i.split(' (contains ')[1].strip(')\n').split(' ')] for i in lines]

allergens_d = {}
for idx in range(len(allergens)):
    for j in allergens[idx]:
        if j not in allergens_d:
            allergens_d[j] = set(food[idx])
        else:
            extra_ingredients = set(food[idx])
            allergens_d[j] = extra_ingredients.intersection(allergens_d[j])

foods_with_allergen = set()
for i in allergens_d.values():
    foods_with_allergen.update([j for j in i])

food_set = set()
for i in food:
    food_set.update([j for j in i])

foods_without_allergen = food_set.difference(foods_with_allergen)

count = 0
for f in foods_without_allergen:
    count += sum([i.count(f) for i in food])
print('Sol 1: ', count)

#part 2
for idx in range(len(food)):
    filtered_food_list = list(filter(lambda x: x not in foods_without_allergen, food[idx]))
    food[idx].clear()
    food[idx] = filtered_food_list

combined_foods_allergens = {}
while len(combined_foods_allergens) < len(allergens_d):
    for allergen in allergens_d:
        if len(allergens_d[allergen]) == 1:
            combined_foods_allergens[allergen] = next(iter(allergens_d[allergen]))
        else:
            values = allergens_d[allergen]
            for v in values:
                if v in combined_foods_allergens.values():
                    allergens_d[allergen].remove(v)
                    break

ordered_d = collections.OrderedDict(sorted(combined_foods_allergens.items()))
final_allergens = ordered_d.keys()
final_ingr = ordered_d.values()

print('Sol 2: ', ",".join([i for i in final_ingr]))
