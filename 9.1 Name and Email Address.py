def add_contact():
    print("\nAdd Contact\n")
    import pickle
    try:
        contact_file = open("Contacts.dat","rb")
        contact_set = pickle.load(contact_file)
        contact_file.close()
        new_contact = input("Enter Contact or 'Cancel': ")
        if new_contact.lower() == 'cancel':
            return
        else:
            contact_email = input("Enter Contact e-mail: ")
            contact_set.update({new_contact : contact_email})
            contact_file = open("Contacts.dat","wb")
            pickle.dump(contact_set,contact_file)
            contact_file.close()
    except:
        print("No Contacts found!")
        new_contact = input("Enter Contact or 'Cancel': ")
        if new_contact.lower() == 'cancel':
            return
        else:
            contact_email = input("Enter Contact e-mail: ")
            contact_set = {}
            contact_set.update({new_contact : contact_email})
            contact_file = open("Contacts.dat","wb")
            pickle.dump(contact_set,contact_file)
            contact_file.close()
            return


def check_list():
    import pickle
    try:
        contact_file = open("Contacts.dat","rb")
        contact_set = pickle.load(contact_file)
        contact_file.close()
        if contact_set == {}:
                print("No Contacts!")
                add = input("Add a Contact? ")
                if 'yes' in add.lower():
                    add_contact()
                else:
                    return
        else:
            return contact_set
    except EOFError:
        print("No contacts!")
        add = input("Add a contact? ")
        if 'yes' in add.lower():
            add_contact()
        else:
            return
    except FileNotFoundError:
        print("You have no contacts!")
        add = input("Would you like to add a contact? ")
        if 'yes' in add.lower():
            add_contact()
        else:
            return


def search_contact():
    print("\nSearch Contact\n")
    contact_set = check_list()
    if contact_set == None:
        return
    else:
        try:
            search_entry = input("Enter contact name, 'All', or 'Cancel': ")
            if search_entry.lower() == 'cancel':
                return
            elif search_entry.lower() == 'all':
                for key, value in sorted(contact_set.items()):
                    print("Name: ", key, "\nEmail:", \
                          value,"\n")
                return
            else:
                print("Name: ", search_entry, "\nEmail:", \
                      contact_set[search_entry])
                return
        except KeyError:
            print("Entry does not exist!")
            show_list = input("Check your list? ")
            if 'yes' in show_list.lower():
                for key, value in sorted(contact_set.items()):
                    print("Name: ", key, "\nEmail:", \
                          value,"\n")
            else:
                return


def edit_contact():
    print("\nEdit Contact\n")
    import pickle
    contact_set = check_list()
    if contact_set == None:
        return
    else:
        edit = input("Enter Contact or 'Cancel': ")
        if edit.lower() == 'cancel':
            return
        else:
            if edit not in contact_set:
                create = input("Contact not found. Create new contact? ")
                if 'yes' in create.lower():
                    new_email = input("Enter e-mail: ")
                    contact_set[edit] = new_email
                    print("Name:     ", edit, "\nEmail:", \
                      contact_set[edit])
                    contact_file = open("Contacts.dat","wb")
                    pickle.dump(contact_set,contact_file)
                    contact_file.close()
                    return
                else:
                    return
            else:
                new_email = input("Enter new e-mail or 'Cancel': ")
                if new_email.lower() == 'cancel':
                    return
                else:
                    contact_set[edit] = new_email
                    print("Name:     ", edit, "\nNew Email:", \
                      contact_set[edit])
                    contact_file = open("Contacts.dat","wb")
                    pickle.dump(contact_set,contact_file)
                    contact_file.close()
                    return


def delete_contact():
    print("\nDelete Contact\n")
    import pickle
    contact_set = check_list()
    if contact_set == None:
        return
    else:
        try:
            delete = input("Enter contact name or 'Cancel': ")
            if delete.lower() == 'cancel':
                return
            else:
                contact_set.pop(delete)
                print(delete,"has been deleted from your list.")
                contact_file = open("Contacts.dat","wb")
                pickle.dump(contact_set,contact_file)
                contact_file.close()
                if contact_set == None:
                    print("No contacts.")
                else:
                    return
        except KeyError:
            print("Entry does not exist!")
            show_list = input("Check your list? ")
            if 'yes' in show_list.lower():
                for key, value in sorted(contact_set.items()):
                    print("Name: ", key, "\nEmail:", \
                          value,"\n")
            else:
                return


def main_menu():
    selection = ""
    while selection.lower() != "quit":
        print("\nMain Menu\n")
        selection = input("Choose an option (Number or Name):\n"
                          "1. Add Contact\n"
                          "2. Search Contact\n"
                          "3. Edit Contact\n"
                          "4. Delete Contact\n"
                          "5. Quit\n\n")
        if selection.lower() in "1. add contact":
            add_contact()
        elif selection.lower() in "2. search contact":
            search_contact()
        elif selection.lower() in "3. edit contact":
            edit_contact()
        elif selection.lower() in "4. delete contact":
            delete_contact()
        elif selection.lower() in "5. quit":
            break
        else:
            print("Your input is invalid.")


main_menu()
