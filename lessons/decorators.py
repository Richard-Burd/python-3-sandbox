class Planet:

  # class attribute
  shape = 'round'

  # instance method
  def __init__(self, name, radius, gravity, system):
      self.name = name
      self.radius = radius
      self.gravity = gravity
      self.system = system

  # instance method
  def orbit(self):
      return f'{self.name} is orbiting in the {self.system}'

  # This "@staticmethod" is a decorator, it extends the behavior of a function without modifying the function itself.
  # They are use extensively in frameworks like Django.
  @staticmethod
  def spin(speed = '2000 miles per hour'):
      return f'The planet spins and spins at {speed}'

  # This "@classmethod" is a decorator, it extends the behavior of a function without modifying the function itself.
  # They are use extensively in frameworks like Django.
  @classmethod
  def commons(cls):
      return f'All planets are {cls.shape} because of gravity'

####################################################
# Let's do some other stuff outside a class object #
####################################################

def cough_discount(function):
  def function_wrapper():
    # code before function runs
    print('*cough*')
    function()

    # code after function
    print('*couuugh*')

  return function_wrapper

# This "@classmethod" is a decorator, it extend the behavior of a function without modifying the function itself.
# They are use extensively in frameworks like Django.
# Here's a use case outside of a class object.
@cough_discount
def question():
  print('can you give me a discount for that!?')

question()
