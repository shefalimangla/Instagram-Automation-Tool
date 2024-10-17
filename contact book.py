contact=[]
number=[]
import re

def add_contact():
    print("CONTACT BOOK")
    n=int(input("Enter the number of contact to be stored:"))
    for i in range (n):
        name=input("Enter the contact name:\n")
        contact.append(name)
        while True:
            phone = input("Enter the number of the contact: ")
            phone_pattern = re.compile( r"^[7-9]\d{9}$")  # Assuming Indian phone numbers, modify the regex as per your country's format

            if re.match(phone_pattern, phone):
                contact.append(phone)
                print("Contact added successfully")
                break
            else:
                print("Enter a 10-digit mobile number starting with 7, 8, or 9.")
def delete_contact():
    confirm=""
    con = input("Enter the contact name you want to delete: ")
    con_lower = con.lower()  # Convert user input to lowercase
    confirm = input("Are you sure you want to remove the contact? (Y/N): ")
    if confirm.lower() == 'y':
        if con in contact:
            contact.remove(con)
        print("Contact removed successfully")
        # else:
        #     print("Contact not found")
    elif confirm.lower() == 'n':
        pass
def search_contact():
    search = input("Enter the name to search: ")
    search_lower = search.lower()
    found = False

    for i in range(0, len(contact), 2):
        if search_lower in contact[i].lower():
            print(f"Contact found: {contact[i]} - {contact[i + 1]}")
            found = True
            break

    if not found:
        print("Contact not found")
    # search = input("Enter the name to search: ")
    # search_lower = search.lower()
    # found = False
    # for i in range(0, len(contact)):
    #     if search_lower[:3] in [str(c).lower() for c in contact]:
    #         print(f"Contact found: {contact[i]} - {number[i]}")
    #         found = True
    #         break
    #     # if not found:
    #     else:
    #         print("Contact not found")
def update_contact(contact):
    con = input("Enter the contact name you want to modify: ")
    con_lower = con.lower()  # Convert user input to lowercase

    if con_lower not in [str(c).lower() for c in contact]:
        print("Contact not found")

    for i in range(0, len(contact)):
        if contact[i] == con:
            new_name = input("Enter the new name: ")
            new_number = input("Enter the new number: ")
            contact[i] = new_name
            contact[i] = new_number
            print("Contact updated successfully")


    # for contacts in contact:
    #     if con in contact :
    #         new_name = input("Enter the new name: ")
    #         new_number = input("Enter the new number: ")
    #         contact[con] = new_name
    #         contact[number] = new_number
    #         print("Contact updated successfully")
    #         return
    #print("Contact not found")


while True:
    choice = input("Enter your choice 1/2/3/4: \n 1.Add contact \n 2.Delete contact \n 3.search contact \n 4.Update contact \n 5. Exit")
    if choice=='1':
        add_contact()
    elif choice=='2':
        delete_contact()
    elif choice=='3':
        search_contact()
    elif choice=='4':
        update_contact(contact)
    elif choice=='5':
        print("Contact Book closed!")
        break
    else:
        print("Invalid choice. Please Enter the choice between 1 to 5")