# Copyright (c) 2023, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
import json

class CowTransaction(Document):
	@frappe.whitelist()
	def before_validate(doc):
		doc.calculate_qty_and_rate()
		doc.get_cow_details()

	
	@frappe.whitelist()
	def validate(doc):
		doc.calculate_food_cost()

	
	@frappe.whitelist()
	def on_submit(doc):
		doc.create_stock_reconciliation()



	@frappe.whitelist()
	def calculate_qty_and_rate(doc, method = None):
		if doc.transaction_type == "Feeding":
			doc.rate_for_1kg = frappe.get_last_doc('Bin', filters={"item_code": doc.feed_item, "warehouse" : doc.feed_warehouse,}).valuation_rate

		if doc.transaction_type == "Treatment":
			doc.rate_for_1kg = frappe.get_last_doc('Bin', filters={"item_code": doc.treatment_item, "warehouse" : doc.treatment_warehouse,}).valuation_rate
		
		doc.actual_qty = frappe.get_last_doc('Bin', filters={"item_code": doc.item_code, "warehouse" : doc.warehouse,}).actual_qty

		if doc.manual==0:
			doc.total_food_qty = float(doc.qty_per_one) * float(doc.actual_qty)

		doc.total_food_amount = float(doc.total_food_qty) * float(doc.rate_for_1kg)


	@frappe.whitelist()
	def get_cow_details(doc, method = None):
		doc.set("cows", [])
		selected_cow = frappe.db.sql(f"""
			select `tabCOW`.name, `tabCOW`.item_name, `tabCOW`.kilogram,
				`tabCow History`.warehouse, `tabCOW`.code, `tabCOW`.batch,`tabCOW`.current_warehouse
			from `tabCOW`
			join `tabCow History` on `tabCow History`.parent = `tabCOW`.name

			where `tabCOW`.current_warehouse = '{doc.warehouse}'
			and `tabCOW`.item = '{doc.item_code}'
			and `tabCOW`.batch = '{doc.batch}'
			and   `tabCOW`.docstatus = 1
			
			""", as_dict=1)

		if selected_cow != []:
			for i in selected_cow:
				doc.append("cows", {
					"cow_code":i.name,
					"item_name":i.item_name,
					"weight":i.kilogram,
					"warehouse":i.warehouse,
					"old_code":i.code,
					"valuation_rate":frappe.get_last_doc('Bin', filters={"item_code": doc.item_code, "warehouse" : doc.warehouse,}).valuation_rate,
					"batch":doc.batch,
					"quantity_of_food": doc.qty_per_one,
				})

		if selected_cow == []:
			frappe.msgprint("لا يوجد بيانات")


	@frappe.whitelist()
	def calculate_food_cost(doc,method = None):
		for m in doc.cows:
			m.value_of_food = m.quantity_of_food * doc.rate_for_1kg
			m.batch = doc.batch


	
	@frappe.whitelist()
	def create_stock_reconciliation(doc,method = None):
		new_doc = frappe.get_doc({
				'doctype': 'Stock Reconciliation',
				'purpose': 'Stock Reconciliation',
				'company' : 'Ardelkheir',
				'posting_date' : datetime.datetime.now(),
				'posting_time' : datetime.datetime.now().strftime("%H:%M:%S")


		})
		#valuation_rate2 = frappe.get_last_doc('Bin', filters={"item_code": doc.production_item, "warehouse" : doc.feed_warehouse,}).valuation_rate

		items = frappe.db.sql(""" select a.name, a.idx, b.item_code, b.warehouse, a.batch, a.old_code,b.production_item,b.feed_warehouse,b.total_food_qty,a.value_of_food
																			from `tabCOWS` a join `tabCow Codes` b
																			on a.parent = b.name
																			where b.name = '{name}' limit 1
																		""".format(name=doc.name), as_dict=1)
		
		for item in items:
			new = new_doc.append("items", {})
			new.item_code = item.item_code
			new.batch_no = item.batch
			#new.qty = 1
			new.warehouse = doc.warehouse
			#new.serial_no = item.old_code
			#new.current_serial_no = item.old_code
			new.valuation_rate = (item.value_of_food + frappe.db.get_value("Bin",{"item_code": doc.item_code, "warehouse":doc.warehouse},"valuation_rate"))
		if doc.feed_item == "سركي متوسط":
			new = new_doc.append("items", {})
			new.item_code = doc.feed_item
			new.warehouse = doc.feed_warehouse
			new.qty = frappe.db.get_value("Bin",{"item_code": doc.feed_item, "warehouse":doc.feed_warehouse},"actual_qty") -  doc.total_food_qty
			#new.valuation_rate = valuation_rate2 * new.qty

		new_doc.insert(ignore_permissions=True)
		new_doc.submit()