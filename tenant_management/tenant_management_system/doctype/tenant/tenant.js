// Copyright (c) 2023, Nzeamalu Chikelue and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenant', {
    refresh: function(frm) {
        frm.add_custom_button('Create Rental Agreement', () => {
            frappe.new_doc('Rental Agreement', {
                occupant: frm.doc.name
            })
        })
        frm.add_custom_button('Create Rent Billing', () => {
            frappe.new_doc('Rent Billing', {
                occupant: frm.doc.name
            })
        })
    }
});
