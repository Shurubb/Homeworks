#Homework_2
with open('recipes.txt', encoding='utf-8') as f:
    read = f.read().split('\n\n')
    cook_book = {}
    keys = ['ingredient_name', 'quantity', 'measure']
    for dish in read:
        dish = dish.split('\n')
        cook_book[dish[0]] = [dict(zip(keys, dish.split(' | '))) for dish in dish[2:]]
#print(cook_book)


def get_shop_list_by_dishes(dishes, person_count=1):
    shop_list = {}
    for menu in dishes:
        for cook in cook_book[menu]:
            quantity = float(cook['quantity']) * person_count
            measure = cook['measure']
            if cook['ingredient_name'] in shop_list.keys():
                quantity += shop_list[cook['ingredient_name']]['quantity']
            composition = {
                'measure': measure,
                'quantity': quantity
                }
            shop_list[cook['ingredient_name']] = composition

    return shop_list

shop = get_shop_list_by_dishes(['Шаурма', 'Омлет'], 2)
print(shop)