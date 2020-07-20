# import
from classes import Planet, Kaoukab

# new instance of the Kaoukab object is invoked by calling it like "Planet()"
naboo = Kaoukab('Naboo', 200000, 5.5, 'Naboo System')

print(f'Name: {naboo.name}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit())
print(Kaoukab.shape) # same as "naboo.shape" b.c. each instance has the same value

# in order to use a class method, you have to call it "()" on the class name:
print(Kaoukab.commons())

print(naboo.spin('a very high speed'))  # same value using static method
print(Kaoukab.spin('a very high speed'))# same value using static method
