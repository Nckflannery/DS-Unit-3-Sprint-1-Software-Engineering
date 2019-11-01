'''
A module to generate random product and print a summary of them
'''
from acme import Product
from random import randint, uniform, choice
adj_name = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun_name = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_items=30):
    '''
    Generates (default thirty) random products
    '''
    list = []
    for i in range(0, num_items):
        rand_id = randint(1000000, 9999999)
        rand_price = randint(5, 100)
        rand_weight = randint(5, 100)
        rand_flam = uniform(0, 2.5)
        name = f'{choice(adj_name)} {choice(noun_name)}'
        a = Product(name, identifier=rand_id, price=rand_price,
                    weight=rand_weight, flammability=rand_flam)
        list.append(a.attributes)
    return list


def inventory_report(products):
    '''
    Gives report of product list including:
    Unique Names
    Average Price
    Average Weight
    Average Flammability
    '''
    a = products
    a.sort()
    name_list = []
    weight_list = []
    price_list = []
    flam_list = []

    for i in range(0, len(a)):
        name_list.append(a[i][1])
        weight_list.append(a[i][2])
        price_list.append(a[i][3])
        flam_list.append(a[i][4])
    name_list.sort()

    unique = 30
    for i in range(1, len(name_list)):
        if name_list[i] == name_list[i-1]:
            unique -= 1
    avg_price = sum(price_list)/len(price_list)
    avg_weight = sum(weight_list)/len(weight_list)
    avg_flam = sum(flam_list)/len(flam_list)
    print(f'Unique product names: {unique}')
    print(f'Average price: ${avg_price:,.02f}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flam}')


if __name__ == '__main__':
    inventory_report(generate_products())
