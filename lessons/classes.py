# 'space' is the folder name, 'planet' is the name of the class file.
# this is enabled by the "__init___.py" file in the space directory
from space.planet import Planet

# importing specific functions in the 'calc' file.
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')

print(naboo.shape)
print(Planet.shape)

print(f'default: {naboo.spin()}')
print(f'custom: {naboo.spin("100 mph")}')
print(f'custom: {Planet.spin("100 mph")}')

print(naboo.commons())
