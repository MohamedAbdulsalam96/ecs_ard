# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AddCowWeight(Document):
	@frappe.whitelist()
	def validate(self):
		for item in self.cow_weight_table:
			max_weight = frappe.db.get_value("Warehouse", item.warehouse, "max_weight")
			min_weight = frappe.db.get_value("Warehouse", item.warehouse, "min_weight")
			if (item.new_weight > max_weight) or (item.new_weight < min_weight):
				frappe.msgprint("Row #" + str(item.idx) + ": New Weight (" + str(round(item.new_weight, 2))  
								+ " KG) Is Not In Range Of Warehouse (" + str(item.warehouse)
								+ ")" + "<br>" + "Warehouse Weight Range: (" + str(int(min_weight)) 
								+ " KG - " + str(int(max_weight)) + " KG)")
				
	@frappe.whitelist()
	def on_submit(self):
		for item in self.cow_weight_table:
			row_name = str(self.name) + str(item.cow_code)

			frappe.db.sql(""" UPDATE `tabCOW` set kilogram = '{current_weight}' where name='{name}'
							""".format(current_weight=item.new_weight, name=item.cow_code))
			
			frappe.db.sql(""" INSERT INTO `tabCow Weight History` (weight, date, remarks, reference_doctype, reference_name, parent, parentfield, parenttype, name)
                                VALUES ('{weight}', '{date}', '{remarks}', '{reference_doctype}', '{reference_name}', '{parent}', '{parentfield}', '{parenttype}', '{name}')
                                """.format(weight=item.new_weight, date=self.posting_date, reference_doctype="Add Cow Weight", reference_name=self.name,
                                           remarks=item.remarks, parent=item.cow_code, parentfield="weight_history", parenttype="COW", name=row_name))