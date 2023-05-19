# Copyright (c) 2023, Nzeamalu Chikelue and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Tenant(Document):
	#this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
        self.validate_maximum_occupancy()

        

    def validate_maximum_occupancy(self):
        property = frappe.get_doc("Property", self.residence)

        count = frappe.db.count(
            "Tenant",
            {"residence": self.residence}

        )
        if count >= property.accomodation:
            message = f'No available occupancy at {self.residence}'
            frappe.throw(message)
