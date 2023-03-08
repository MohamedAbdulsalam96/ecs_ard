# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
import json

class CowCodes(Document):
	@frappe.whitelist()
	def validate(doc):
		doc.rate_for_1kg = frappe.get_last_doc('Bin', filters={"item_code": doc.production_item, "warehouse" : doc.feed_warehouse,}).valuation_rate
		doc.actual_qty = frappe.get_last_doc('Bin', filters={"item_code": doc.item_code, "warehouse" : doc.warehouse,}).actual_qty
		if doc.manual==0:
			doc.total_food_qty = float(doc.qty_per_one) * float(doc.actual_qty)


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
		if doc.production_item == "سركي متوسط":
			new = new_doc.append("items", {})
			new.item_code = doc.production_item
			new.warehouse = doc.feed_warehouse
			new.qty = frappe.db.get_value("Bin",{"item_code": doc.production_item, "warehouse":doc.feed_warehouse},"actual_qty") -  doc.total_food_qty
			#new.valuation_rate = valuation_rate2 * new.qty

		new_doc.insert(ignore_permissions=True)
		# insetred_doc = frappe.get_doc("Stock Reconciliation",new_doc.name)
		# for insert1 in insetred_doc.items:
		# 	if insert1.item_code=="سركي متوسط":
		# 		insert1.qty = insert1.current_qty - doc.total_food_qty

		
			
		# stock_reconciliation = frappe.get_doc({
		# 	'doctype': 'Stock Reconciliation',
		# 	'purpose': 'Stock Reconciliation',
		# 	'company' : 'Ardelkheir',
		# 	'posting_date' : datetime.datetime.now(),
		# 	'posting_time' : datetime.datetime.now().strftime("%H:%M:%S")
		# })
		# for item in doc.cows:
		# 	items = stock_reconciliation.append('items',{
		# 		'item_code' : "عجل سوداني",
		# 		'warehouse' : "2 حظيره استقبال - A",
		# 		'qty' : 4,
		# 		'valuation_rate' : 1,
		# 		'batch_no' :"S0030",
		# 		'serial_no' : "S0022"
		# 	})
			# items.item_code = "عجل سوداني"#doc.item_code
			# items.warehouse = "2 حظيره استقبال - A"#doc.warehouse
			# items.qty = 4
			# items.valuation_rate = 1 #frappe.get_last_doc('Stock Ledger Entry', filters={"item_code": doc.item_code, "serial_no" : item.old_code, "batch_no" : item.batch}).valuation_rate
			# items.batch_no = "S0030"#doc.batch1
			# items.serial_no = "S0022"#item.old_code
		# 	items.save()
		# stock_reconciliation.insert(ignore_permissions=True)
		# frappe.msgprint("تم إنشاء " + stock_reconciliation.name)

	@frappe.whitelist()
	def get_details(doc, method = None):
		selected_cow = frappe.db.sql(f"""
		select `tabCOW`.name, `tabCOW`.item_name, `tabCOW`.kilogram,
			`tabCow History`.warehouse, `tabCOW`.code, `tabCOW`.batch,`tabCOW`.current_warehouse
		from `tabCOW`
		join `tabCow History` on `tabCow History`.parent = `tabCOW`.name

		where `tabCOW`.current_warehouse = '{doc.warehouse}'
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
					#"batch":i.batch,
					"quantity_of_food": doc.qty_per_one,#((i.kilogram) // 200) * 11,
					#"value_of_food": float(doc.rate_for_1kg) * i.quantity_of_food
				})
			doc.save()

			# for i in selected_cow:
			# 	doc.append("cows", {
			# 		"value_of_food": i.quantity_of_food * doc.price_per_one
			# 	})



		if selected_cow == []:
			frappe.msgprint("لا يوجد بيانات")

	@frappe.whitelist()
	def calculate_food_cost(doc,method = None):
		

		for m in doc.cows:
			m.value_of_food = m.quantity_of_food * doc.rate_for_1kg
			
		doc.save()




