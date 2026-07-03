from complaint_data import ComplaintDatabase, Complaint


class Citizen:

    DEPARTMENT_KEYWORDS = {
        "Water Department": {
            "water", "pipe", "leak", "leakage", "drain",
            "drainage", "sewage", "tap", "tank"
        },

        "Road Department": {
            "road", "street", "pothole", "bridge",
            "traffic", "signal", "highway"
        },

        "Electricity Department": {
            "electricity", "power", "wire",
            "transformer", "street light",
            "current", "voltage"
        },

        "Sanitation Department": {
            "garbage", "waste", "dustbin",
            "dirty", "cleaning", "mosquito"
        },

        "Health Department": {
            "hospital", "doctor", "ambulance",
            "medicine", "health", "medical"
        },

        "Transport Department": {
            "bus", "train", "metro",
            "transport", "station"
        },

        "Police Department": {
            "theft", "crime", "robbery",
            "fraud", "harassment", "fight"
        }
    }

    def assign_department(self, description):
        words = set(description.lower().split())

        for department, keywords in self.DEPARTMENT_KEYWORDS.items():
            if words.intersection(keywords):
                return department

        return "General Department"

    def register_complaint(self):
        citizen_name = input("Enter Citizen Name: ")
        location = input("Enter Location: ")
        description = input("Enter Complaint Description: ")

        complaint_id = ComplaintDatabase.generate_complaint_id()
        department = self.assign_department(description)

        complaint = Complaint(
            complaint_id=complaint_id,
            citizen_name=citizen_name,
            location=location,
            description=description,
            department=department
        )

        ComplaintDatabase.complaints.append(complaint)
        ComplaintDatabase.save_data()

        print("\nComplaint Registered Successfully")
        print("Complaint ID :", complaint_id)
        print("Assigned Department :", department)
        print("Current Status : Submitted")

    def track_status(self):
        complaint_id = input("Enter Complaint ID: ")

        for complaint in ComplaintDatabase.complaints:
            if complaint.complaint_id == complaint_id:
                print("\n===== Complaint Details =====")
                print("Complaint ID :", complaint.complaint_id)
                print("Citizen Name :", complaint.citizen_name)
                print("Location :", complaint.location)
                print("Complaint :", complaint.description)
                print("Department :", complaint.department)
                print("Status :", complaint.status)
                return

        print("Complaint ID not found.")

    def give_feedback(self):
        complaint_id = input("Enter Complaint ID: ")

        for complaint in ComplaintDatabase.complaints:

            if complaint.complaint_id == complaint_id:

                if complaint.status != "Resolved":
                    print(
                        "Feedback can only be submitted "
                        "after the complaint is resolved."
                    )
                    return

                feedback = input("Enter Feedback: ")

                complaint.feedback = feedback

                ComplaintDatabase.save_data()

                print("Feedback submitted successfully.")
                return

        print("Complaint ID not found.")

    def display_menu(self):
        while True:

            print("\n===== Citizen Module =====")
            print("1. Register Complaint")
            print("2. Track Complaint Status")
            print("3. Give Feedback")
            print("4. Back to Main Menu")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.register_complaint()

            elif choice == "2":
                self.track_status()

            elif choice == "3":
                self.give_feedback()

            elif choice == "4":
                break

            else:
                print("Invalid Choice. Please try again.")