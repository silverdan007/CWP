contacts = {
    "name": "number"
}
print(contacts)

print("contact manager")
status = True
while status:
    entry = input("""
      Type new to enter a new contact \n
      type search to enter a contact \n
      type edit to edit a contact \n
      type del to delete a contact \n
      type quit to end
      
    """).lower()
    if entry == "quit":
        print("Program terminated")
        status = False
    elif entry == "new":
        name = input("enter name").upper()
        number = input("enter number")
        contacts[name] = number
        print(f"added succesfully {contacts}")
    elif entry == "edit":
        print(contacts)
        name = input("enter name you will like to edit").lower()
        if name in contacts:
            number = input("enter a number")
            n_name = input("enter new name")
            contacts[n_name] = contacts.pop(name)
            contacts[n_name] = number
            print("contact updated")
            print(contacts)
        else:
            print("unavailable contact")
    elif entry == "del":
        if entry in contacts:
            del contacts[entry]
            print("contact deleted")
            print(contacts)
        else:
            print("unavailable contact")
    else:
        print("invalid entry")

