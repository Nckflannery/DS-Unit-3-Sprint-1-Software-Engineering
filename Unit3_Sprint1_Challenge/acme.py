'''
Class to represent Acme Products
'''
from random import randint


class Product:
    '''
    A general class for all acme products
    '''

    def __init__(self, name: str, price=10, weight=20, flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
        self.attributes = identifier, name, weight, price, flammability

    def stealability(self):
        stealable = self.price/self.weight
        if stealable < 0.5:
            return 'Not so stealable...'
        elif (stealable >= 0.5) and (stealable < 1):
            return 'Kinda stealable.'
        else:
            return 'Very stealable'

    def explode(self):
        boom = self.flammability * self.weight
        if boom < 10:
            return 'Fizzle'
        elif (boom >= 10) and (boom < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''
    A Boxing Glove subclass
    '''

    def __init__(self, weight=10):
        super().__init__(weight)
        self.weight = 10

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
