name = 'Me'
age = 92
qaimah = [1, 2, 3]
qamous = {"A":1, "B":2, "C":3}

type(name)   #=> <class 'str'>
type(age)    #=> <class 'int'>
type(qaimah) #=> <class 'list'>
type(qamous) #=> <class 'dict'>

# class name must have capitol letter
class Planet:

  # initializer (init function) that runs when we create a new instance
  # similiar to a constructor method in JavaScript
  def __init__(self):
    # self is like "this" in JavaScript
    self.name = "Hoth"
    self.radius = 200000
    self.gravity = 5.5
    self.system = "Hoth System"

  # a class function takes in 'self' as a variable:
  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'

# new instance of the Planet object is invoked by calling it like "Planet()"
hoth = Planet()

print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')

# calling a class function
print(hoth.orbit())

# now let's create an object where we require the instance variables upon creation
# of a new class instance
class Kaoukab:
  # class attributes go here:
  shape = 'all kaouakibu are spherical'

  # This is a class method:
  @classmethod
  def commons(cls): # 'cls' referrs to the class
    return f'I think that it\'s true to say that:{cls.shape}'

  # https://www.youtube.com/watch?v=LwFnF9XoEfM&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=18
  # Static methods doen't have access to 'delf' or the class itself...
  # it only has access to the parameters we pass into it individually
  @staticmethod
  def spin(speed = "2000 miles per hour"):
    return f'the planet spins at {speed}'

  def __init__(self, name, radius, gravity, system):
    # self is like "this" in JavaScript
    self.name = name        # instance attribute or instance method
    self.radius = radius    # instance attribute or instance method
    self.gravity = gravity  # instance attribute or instance method
    self.system = system    # instance attribute or instance method

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'
    
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
