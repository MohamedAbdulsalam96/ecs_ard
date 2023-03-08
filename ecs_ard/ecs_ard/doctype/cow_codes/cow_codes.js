// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cow Codes', {
	get_cows: function(frm) {
		frm.doc.cows = []
		frappe.call({
			doc: frm.doc,
			method: "get_details",
			callback: function(r) {
				frm.refresh_fields();
				frm.refresh();
			}
		});
	},
	calculate_food_cost: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "calculate_food_cost",
			callback: function(r) {
				frm.refresh_fields();
				frm.refresh();
			}
		});
	},
	
	create_stock_reconciliation: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "create_stock_reconciliation",
			callback: function(r) {
				frm.refresh_fields();
				frm.refresh();
			}
		});
	}
});
