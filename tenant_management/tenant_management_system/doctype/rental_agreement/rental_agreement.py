# Copyright (c) 2023, Nzeamalu Chikelue and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class RentalAgreement(Document):
    def before_save(self):
        days = self.get_duration()
        #compute end date from duration
        self.end_date = frappe.utils.add_days(self.start_date, days)
        self.check_preferred_property()


    def before_submit(self):
        self.check_existing_agreement()

    def get_duration(self):
        #select number of days based on duration
        duration = {
            "Annual": 365,
            "Quarter": 90,
            "Month": 30
        }
        return duration[self.duration]
    
    def check_existing_agreement(self):
        valid_agreement = frappe.db.exists(
            "Rental Agreement",
            {
                "Occupant": self.occupant,
                "docstatus": DocStatus.submitted(),
                "end_date": (">", self.start_date)
            }
        )
        if valid_agreement:
            message = f'{self.full_name} has a active rental agreement!!'
            frappe.throw(message)

    def check_preferred_property(self):
        tenant = frappe.get_doc("Tenant", self.occupant)

        if self.residence != tenant.residence:
             message = f'{self.full_name} is registered to a different property({tenant.residence}). Check tenant details and update preference to {self.residence} before creating rental agreement.'			
             frappe.throw(message)
