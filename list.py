# make a list to hold items
shopping_list = []

def show_help():
  # print instructions on how to use app
  print("What should we puck up at the store?")
  print("""
  Enter 'DONE' to stop adding items.
  Enter 'HELP to show this help.
  Enter 'SHOW' to see your current list.
  """)

def show_list():
# print list
  print("Here is your list:")

  for item in shopping_list:
    print(item)

def add_to_list(new_item):
   # add new items to list
  shopping_list.append(new_item)
  print("Added {}. List now had {} items".format(new_item, len(shopping_list)))

show_help()

while True:
  # ask for new items
  new_item = input("> ")

  # be able to quit app
  if new_item == 'DONE':
    break
  elif new_item =='HELP':
    show_help()
    continue
  elif new_item =='SHOW':
    show_list()
    continue
  add_to_list(new_item)
show_list()
