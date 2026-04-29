# Copyright (c) 2026, Admin User and contributors
# For license information, please see license.txt

import random
from frappe.model.document import Document


class AirplaneTicket(Document):

    def before_insert(self):
        number = random.randint(1, 99)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{number}{letter}"