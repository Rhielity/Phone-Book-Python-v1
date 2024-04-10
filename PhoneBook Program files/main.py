# Advanced Programming Project I v.1
import datetime


def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


contacts = {}
dateAdded = []
toCallQueue = []


def addNewContact(name, phoneNum):
    contacts[len(contacts)] = {name: phoneNum}
    dateAdded.append(get_current_date())


def printContacts():
    print("Contact List:")
    for i in range(len(contacts)):
        print(f"    {contacts[i]}    Added on: {dateAdded[i]}")
    print()


def save_contacts_to_file():
    """Saves all contacts to a text file named 'contact_list.txt'"""
    with open("contact_list.txt", "w") as file:
        for i in range(len(contacts)):
            contact_name = list(contacts[i].keys())[0]
            contact_phone = list(contacts[i].values())[0]
            file.write(f"{contact_name},{contact_phone},{dateAdded[i]}\n")


def load_contacts_from_file():
    """Loads all contacts from a text file named 'contact_list.txt'"""
    contacts.clear()
    dateAdded.clear()
    try:
        with open("contact_list.txt", "r") as file:
            for line in file:
                contact_info = line.strip().split(",")
                contacts[len(contacts)] = {contact_info[0]: contact_info[1]}
                dateAdded.append(contact_info[2])
    except FileNotFoundError:
        print("Contact list file not found. No contacts loaded.")


def clearContacts():
    # Simulate clearing program memory
    contacts.clear()
    dateAdded.clear()


def addToCallQueue(name):
    toCallQueue.append(name)


def popToCallQueue():
    toCallQueue.pop(0)


def printToCallQueue():
    n = 1
    print("Caller Queue:")
    if len(toCallQueue) < 1:
        print("    Caller Queue Empty")
    else:
        for i in toCallQueue:
            print(f"    {n}: {i}")
            n += 1
        print()


def save_call_queue_to_file():
    """Saves all callers in the queue to a text file named 'caller_queue.txt'"""
    with open("caller_queue.txt", "w") as file:
        for name in toCallQueue:
            file.write(f"{name}\n")


def load_call_queue_from_file():
    """Loads all callers from a text file named 'caller_queue.txt'"""
    toCallQueue.clear()
    try:
        with open("caller_queue.txt", "r") as file:
            for line in file:
                toCallQueue.append(line.strip())
    except FileNotFoundError:
        print("Caller queue file not found. No callers loaded.")


def manage_contacts():
    """Provides options to interact with the contact list"""
    while True:
        print("\nContact List Menu:")
        print("  1. Add New Contact")
        print("  2. Print Contacts")
        print("  3. Save Contacts to File")
        print("  4. Load Contacts from File")
        print("  5. Clear Contacts")  # Added this option
        print("  q. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == '1':
            name = input("Enter contact name: ")
            phone_num = input("Enter phone number: ")
            addNewContact(name, phone_num)
            print(f"Contact '{name}' added successfully!")
        elif choice == '2':
            if contacts:
                printContacts()
            else:
                print("Your contact list is empty.")
        elif choice == '3':
            save_contacts_to_file()
            print("Contacts saved to file 'contact_list.txt'.")
        elif choice == '4':
            load_contacts_from_file()
            print("Contacts loaded from file 'contact_list.txt'.")
        elif choice == '5':
            clearContacts()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")


def manage_call_queue():
    """Provides options to interact with the Call Queue"""
    while True:
        print("\nCall Queue Menu:")
        print("  1. Add Caller to Queue")
        print("  2. Remove Caller from Queue (Serve Caller)")
        print("  3. Print Call Queue")
        print("  4. Save Call Queue to File (New)")
        print("  5. Load Call Queue from File (New)")
        print("  q. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == '1':
            name = input("Enter caller name: ")
            addToCallQueue(name)
            print(f"Caller '{name}' added to queue.")
        elif choice == '2':
            caller_name = popToCallQueue()
            if caller_name:
                print(f"Serving caller: {caller_name}")
            # Simulate serving the caller (could involve removing them from contacts if appropriate)
        elif choice == '3':
            printToCallQueue()
        elif choice == '4':
            save_call_queue_to_file()
            print("Call Queue saved to file 'caller_queue.txt'.")
        elif choice == '5':
            load_call_queue_from_file()
            print("Call Queue loaded from file 'caller_queue.txt'.")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    """Main function to continuously run the program"""
    load_contacts_from_file()  # Load contacts on program start
    load_call_queue_from_file()  # Preload call queue on program start

    do_while = True
    while do_while:
        print("\nMain Menu:")
        print("  1. Manage Contacts")
        print("  2. Manage Call Queue")
        print("  q. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == '1':
            manage_contacts()
        elif choice == '2':
            manage_call_queue()
        elif choice == 'q':
            do_while = False
            print("Quitting program...")
        else:
            print("Invalid choice. Please try again.")

    # Save contacts before exiting
    save_contacts_to_file()


if __name__ == "__main__":
    main()
