// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Add Cow Weight', {
	refresh: (frm) => {
		frm.set_query("cow_code", "cow_weight_table", () => {
			const added_cows = frm.doc.cow_weight_table.map((r) => r.cow_code);
			return {
				filters: [
				    ["name", "not in", added_cows]
				],
			};
		});
	},
});