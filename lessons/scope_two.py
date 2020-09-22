my_name = "Dog"

def parent_scope():
  my_name = "Mom"
  print(f"I see {my_name} in the parent scope.")
  def child_scope():
    my_name = "Kid"
    print(f"I see {my_name} in the child scope.")
    def pet_scope():
      global my_name
      print(f"I see {my_name} in the pet scope.")
    # call the child function:
    pet_scope()
  # call the child function:
  child_scope()
# call the parent function:
parent_scope()
