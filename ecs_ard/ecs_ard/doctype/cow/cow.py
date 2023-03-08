# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class COW(Document):
	def validate(self):
		if self.edit_warehouse:
			if self.current_warehouse == self.new_warehouse:
				frappe.throw(" يجب إختيار مخزن جديد ")
			else:
				stock_entry = frappe.get_doc(
					{
						"doctype": "Stock Entry",
						"posting_date": self.warehouse_date,
						"stock_entry_type": "Material Transfer",
						"from_warehouse": self.current_warehouse,
						"to_warehouse": self.new_warehouse,
						"items": [
							{
								"s_warehouse": self.current_warehouse,
								"t_warehouse": self.new_warehouse,
								"item_code": self.item,
								"qty": 1,
								"serial_no": self.code,
								"batch_no": self.batch,
							}
						],
					}
				)
				stock_entry.insert()
				stock_entry.submit()
				

				warehouse = self.append("warehouse", {})
				warehouse.date = self.warehouse_date
				warehouse.warehouse = self.new_warehouse
				warehouse.remarks = self.warehouse_remarks
				warehouse.reference_doctype = "Stock Entry"
				warehouse.reference_name = stock_entry.name
				self.current_warehouse = self.new_warehouse
				self.warehouse_date = ""
				self.new_warehouse = ""
				self.edit_warehouse = ""
				self.warehouse_remarks = ""