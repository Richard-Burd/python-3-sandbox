class Tab:

  # this should be an external module, but for now it's in here
  menu = {
    'wine': 5,
    'beer': 3,
    'soft_drink': 2,
    'chicken': 10,
    'beef': 15,
    'veggie': 12,
    'desert': 6
  }

  # we need an init function (i.e. a constructor function in JavaScript)
  def __init__(self): # self is the same as 'this' in JavaScript
    self.total = 0
    self.items = []

  def add(self, item):

    # append is a method to add an element to a list (i.e. an array)
    self.items.append(item)

    # this adds the value from the commensurate key in the menu above
    self.total += self.menu[item]

  def print_bill(self, tax, service):
    tax = ( tax/100 ) * self.total
    service = ( service/100 ) * self.total
    total = self.total + tax + service

    for item in self.items:
        print(f'{item:20} £{self.menu[item]}')

    #------------------------.2f <= this outputs the number to two decemal places: 0.01
    #-------------:20 <= this makes the output 20 characters aligned to the right
    print(f'{"Tax":20} £{tax:.2f}')
    print(f'{"Service charge":20} £{service:.2f}')
    print(f'{"Total":20} £{total:.2f}')

# enter these commands in bash to use the program; $ python3
# >>> from bar_tab import Tab
# >>> table2 = Tab()
# >>> table2.add('wine')
# >>> table2.add('beef')
# >>> table2.print_bill(10, 10)
# wine                 £5
# beef                 £15
# Tax                  £2.00
# Service charge       £2.00
# Total                £24.00
