// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on("COW", {
	setup: function(frm) {
		frm.set_query("new_warehouse", function() {
			return {
				filters: [
					["Warehouse","name", "!=", frm.doc.current_warehouse]
				]
			};
		});
	}
});