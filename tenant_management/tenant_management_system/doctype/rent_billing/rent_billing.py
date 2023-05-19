# Copyright (c) 2023, Nzeamalu Chikelue and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class RentBilling(Document):	
	def before_save(self):
		lease = frappe.get_doc("Rental Agreement", self.lease_agreement)

		dn = get_divisor(lease.duration)

		#compute amount to be paid based on agreed duration
		self.amount_due = float(lease.price) / float(dn)

	def before_submit(self):
		lease = frappe.get_doc("Rental Agreement", self.lease_agreement)

		if lease.docstatus != DocStatus.submitted():
			frappe.throw("Rental agreement for this bill is Invalid. Please ensure that agreement has been submitted before billing!")

		if self.payment_date >= self.rent_expires:
			frappe.throw("Rental Agreemment has expired.")

		self.check_duplicate()
		self.check_paid()


	def check_duplicate(self):
		exists = frappe.db.exists(
			"Rent Billing",
			{
				"Occupant": self.occupant,
				"docstatus": DocStatus.submitted(),
				"rent_expires": (">=", self.rent_expires)
			}
		)
		if exists:
			message = f'A duplicate billing exists at {exists}'
			frappe.throw(message)

	def check_paid(self):
		if self.paid != "Yes":
			frappe.throw("Complete payment of bill before submittting ")



# return a divisor to split annual price to agreed payment
def get_divisor(duration):	
		divisor = {
			"Annual": 1,
			"Quarter": 4,
			"Month": 12
		}
		return divisor[duration]
