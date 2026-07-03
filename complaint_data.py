import json
import os
from dataclasses import dataclass, asdict
from collections import Counter, defaultdict


@dataclass
class Complaint:
    complaint_id: str
    citizen_name: str
    location: str
    description: str
    department: str
    status: str = "Submitted"
    feedback: str = ""


class ComplaintDatabase:
    FILE_NAME = "complaints.json"
    complaints = []

    @classmethod
    def load_data(cls):
        if os.path.exists(cls.FILE_NAME):
            with open(cls.FILE_NAME, "r") as file:
                try:
                    data = json.load(file)
                    cls.complaints = [Complaint(**item) for item in data]
                except json.JSONDecodeError:
                    cls.complaints = []
        else:
            cls.complaints = []

    @classmethod
    def save_data(cls):
        with open(cls.FILE_NAME, "w") as file:
            json.dump(
                [asdict(c) for c in cls.complaints],
                file,
                indent=4
            )

    @classmethod
    def generate_complaint_id(cls):
        return f"CMP{len(cls.complaints)+1:03d}"