from complaint_data import ComplaintDatabase


class Officer:

    def view_complaints(self):
        if not ComplaintDatabase.complaints:
            print("No complaints found.")
            return

        for complaint in ComplaintDatabase.complaints:
            print("\n----------------------------")
            print("Complaint ID :", complaint.complaint_id)
            print("Citizen Name :", complaint.citizen_name)
            print("Location :", complaint.location)
            print("Complaint :", complaint.description)
            print("Department :", complaint.department)
            print("Status :", complaint.status)

    def update_status(self):
        complaint_id = input("Enter Complaint ID: ")

        for complaint in ComplaintDatabase.complaints:

            if complaint.complaint_id == complaint_id:

                print("\n1. Under Review")
                print("2. In Progress")
                print("3. Resolved")

                choice = input("Enter Choice: ")

                status_map = {
                    "1": "Under Review",
                    "2": "In Progress",
                    "3": "Resolved"
                }

                complaint.status = status_map.get(
                    choice,
                    complaint.status
                )

                ComplaintDatabase.save_data()

                print("Status Updated Successfully")
                return

        print("Complaint Not Found")