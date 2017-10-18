#make list to hold items
shopping_list = []
#print instructions on how to use app
print("What should we pick up at the store")
print("Enter 'DONE' to stop adding items")

while True:
    new_item = input("> ")

    #quit app
    if new_item == "DONE":
        break

    #ask for new items
    shopping_list.append(new_item)
#add new items to list
#print out list
print("Here is your list:")
for item in shopping_list:
    print(item)
