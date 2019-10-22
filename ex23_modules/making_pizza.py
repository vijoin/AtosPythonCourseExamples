import pizza
#from pizza import make_pizza
#from pizza import *

pizza.make_pizza(12, 'pepperoni', 'choclo', 'anana' )
pizza.make_pizza(15, *pizza.STANDAR)

make_my_pizza = pizza.make_pizza

make_my_pizza(18, 'banana', 'durazno', 'frutilla', 'chocolate')