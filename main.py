from auth import login
from customer import add_customer
from room import show_available_rooms
from booking import create_booking
from invoice import checkout
from report import daily_room_report
from view_booking import view_active_bookings
from checkin import check_in
role = login()
if not role:
    exit()

while True:
    print("""
    1. Add Customer
    2. View Rooms
    3. Create Booking
    4. Check-In
    5. Check-Out
    6. Daily Income
    7. View Active Bookings
    0. Exit
    """)

    choice = input("Choose: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        show_available_rooms()
    elif choice == "3":
        create_booking()
    elif choice == "4":
        check_in()
    elif choice == "5":
        checkout(int(input("Booking ID: ")))
    elif choice == "6":
        daily_room_report()
    elif choice == "7":
        view_active_bookings()
    elif choice == "0":
        break
