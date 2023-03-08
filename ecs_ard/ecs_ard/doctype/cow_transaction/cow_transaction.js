// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cow Transaction', {
	setup: function(frm) {
		frm.set_query("batch", function() {
			return {
				filters: [
					["Batch","item", "=", frm.doc.item_code]
				]
			};
		});

		frm.set_query("feed_item", function() {
			return {
				filters: [
					["Item","item_group", "=", "Feeding"]
				]
			};
		});

		frm.set_query("treatment_item", function() {
			return {
				filters: [
					["Item","item_group", "=", "Treatment"]
				]
			};
		});
	}
});