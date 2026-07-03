from collections import Counter
from complaint_data import ComplaintDatabase


class Admin:

    def dashboard(self):
        status_counter = Counter(
            complaint.status
            for complaint in ComplaintDatabase.complaints
        )

        print("\n===== ADMIN DASHBOARD =====")
        print("Total Complaints:",
              len(ComplaintDatabase.complaints))

        for status, count in status_counter.items():
            print(status, ":", count)

    def view_feedback(self):
        found = False

        for complaint in ComplaintDatabase.complaints:

            if complaint.feedback:
                found = True

                print("\nComplaint ID:",
                      complaint.complaint_id)

                print("Citizen:",
                      complaint.citizen_name)

                print("Feedback:",
                      complaint.feedback)

        if not found:
            print("No feedback available.")