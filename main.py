from citizen import Citizen
from officer import Officer
from admin import Admin
from complaint_data import ComplaintDatabase

ComplaintDatabase.load_data()

citizen = Citizen()
officer = Officer()
admin = Admin()

while True:

    print("\n===== SMART GRIEVANCE REDRESSAL SYSTEM =====")
    print("1. Citizen Module")
    print("2. Officer Module")
    print("3. Admin Module")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        while True:
            print("\n===== Citizen Module =====")
            print("1. Register Complaint")
            print("2. Track Complaint")
            print("3. Give Feedback")
            print("4. Back")

            ch = input("Enter Choice: ")

            if ch == "1":
                citizen.register_complaint()

            elif ch == "2":
                citizen.track_status()

            elif ch == "3":
                citizen.give_feedback()

            elif ch == "4":
                break

            else:
                print("Invalid Choice")

    elif choice == "2":

        while True:
            print("\n===== Officer Module =====")
            print("1. View Complaints")
            print("2. Update Status")
            print("3. Back")

            ch = input("Enter Choice: ")

            if ch == "1":
                officer.view_complaints()

            elif ch == "2":
                officer.update_status()

            elif ch == "3":
                break

            else:
                print("Invalid Choice")

    elif choice == "3":

        while True:
            print("\n===== Admin Module =====")
            print("1. Dashboard")
            print("2. View Feedback")
            print("3. Back")

            ch = input("Enter Choice: ")

            if ch == "1":
                admin.dashboard()

            elif ch == "2":
                admin.view_feedback()

            elif ch == "3":
                break

            else:
                print("Invalid Choice")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")