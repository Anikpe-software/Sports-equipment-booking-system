equipment_bookings = []

def book_equipment():
    student = input("Enter student name: ")
    equipment = input("Enter equipment name: ")
    equipment_bookings.append({"student": student, "equipment": equipment})
    print("Equipment booked successfully")

def view_bookings():
    if not equipment_bookings:
        print("No bookings available")
    else:
        for booking in equipment_bookings:
            print("Student:", booking["student"], "| Equipment:", booking["equipment"])

def main():
    while True:
        print("1. Book Equipment")
        print("2. View Bookings")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_equipment()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
