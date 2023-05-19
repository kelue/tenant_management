# Copyright (c) 2023, Nzeamalu Chikelue and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class Agent(Document):
	#this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'

        valid = validate_email_address(self.email)

        if valid == '':
            frappe.throw("Invalid email Please enter a valid email address")
