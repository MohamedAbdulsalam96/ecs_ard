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
		doc.actual_qty = frappe.db.count('COW', {"item": doc.item_code, "current_warehouse" : doc.warehouse, "batch": doc.batch})
		if doc.transaction_type == "Feeding":
			doc.rate_for_1kg = frappe.db.get_value('Bin', {"item_code": doc.feed_item, "warehouse" : doc.feed_warehouse}, 'valuation_rate') or 0
			doc.qty_per_one = frappe.db.get_value('Warehouse', doc.warehouse, 'feeding_qty')

		if doc.transaction_type == "Treatment":
			doc.rate_for_1kg = frappe.db.get_value('Bin', {"item_code":doc.treatment_item, "warehouse": doc.treatment_warehouse}, 'valuation_rate') or 0
			if doc.manual2 == 0:
				doc.qty_per_one = 0

		if doc.manual == 0:
			doc.total_food_qty = doc.qty_per_one * doc.actual_qty

		doc.total_food_amount = doc.total_food_qty * doc.rate_for_1kg


	@frappe.whitelist()
	def get_cow_details(doc, method = None):
		doc.set("cows", [])
		selected_cow = frappe.db.sql(
			"""
				select 
					name, item_name, kilogram, code, batch, current_warehouse
				from 
					`tabCOW`
				where 
					current_warehouse = '{warehouse}'
					and item = '{item}'
					and batch = '{batch}'
			""".format(warehouse=doc.warehouse, item=doc.item_code, batch=doc.batch), as_dict=1)

		if selected_cow != []:
			# record_name = int(doc.total_food_amount)+100000
			for i in selected_cow:
				if doc.transaction_type != "Expense":
					doc.append("cows", {
						"cow_code":i.name,
						"item_name":i.item_name,
						"weight":i.kilogram,
						"warehouse":i.current_warehouse,
						"old_code":i.code,
						"valuation_rate":frappe.db.get_value('Bin', {"item_code": doc.item_code, "warehouse" : doc.warehouse}, 'valuation_rate') or 0,
						"batch":i.batch,
						"quantity_of_food": doc.qty_per_one,
					})

				if doc.transaction_type == "Expense":
					doc.append("cows", {
						"cow_code":i.name,
						"item_name":i.item_name,
						"weight":i.kilogram,
						"warehouse":i.current_warehouse,
						"old_code":i.code,
						"valuation_rate":frappe.db.get_value('Bin', {"item_code": doc.item_code, "warehouse" : doc.warehouse}, 'valuation_rate') or 0,
						"batch":i.batch,
						"quantity_of_food": 0,
					})

				# 	frappe.db.sql(""" INSERT INTO `tabCOWS` (cow_code, item_name, weight, warehouse, old_code, valuation_rate, batch, quantity_of_food, 
				# 						parent, parentfield, parenttype, name)
				#                     VALUES ('{cow_code}', '{item_name}', '{weight}', '{warehouse}', '{old_code}', '{valuation_rate}', '{batch}', 
				#                     '{quantity_of_food}', '{parent}', '{parentfield}', '{parenttype}', '{name}')
				#                     """.format(cow_code=i.name, item_name=i.item_name, weight=i.kilogram,
				#                                 warehouse=i.current_warehouse, old_code=i.code, 
				# 								valuation_rate=frappe.db.get_value('Bin', {"item_code": doc.item_code, "warehouse" : doc.warehouse}, 'valuation_rate') or 0,
				#                                 batch=i.batch, quantity_of_food=doc.qty_per_one, 
				# 								parent=doc.name, parentfield="cows", parenttype="Cow Transaction", name=record_name))
			# 	record_name +=1
			# frappe.db.commit()

		if selected_cow == []:
			frappe.msgprint("لا يوجد بيانات")


	@frappe.whitelist()
	def calculate_food_cost(doc,method = None):
		for m in doc.cows:
			if doc.transaction_type == "Expense":
				m.value_of_food = 0
			if doc.manual == 0:
				m.value_of_food = m.quantity_of_food * doc.rate_for_1kg
			if doc.manual == 1:
				m.value_of_food = (doc.total_food_qty * doc.rate_for_1kg) / doc.actual_qty

	
	@frappe.whitelist()
	def create_stock_reconciliation(doc,method = None):
		if doc.transaction_type != "Expense":
			new_doc = frappe.get_doc({
				'doctype': 'Stock Reconciliation',
				'purpose': 'Stock Reconciliation',
				'posting_date' : doc.posting_date,
			})
			serial_no = "\n".join([row.old_code for row in doc.cows])

			new = new_doc.append("items", {})
			new.item_code = doc.item_code
			new.qty = doc.actual_qty
			new.warehouse = doc.warehouse
			new.batch_no = doc.batch
			new.serial_no = serial_no
			# new.current_serial_no = serial_no
			cow_item_rate = frappe.db.get_value("Bin",{"item_code": doc.item_code, "warehouse":doc.warehouse},"valuation_rate") or 0
			new.valuation_rate = (doc.total_food_amount / doc.actual_qty) + cow_item_rate
			
			if doc.transaction_type == "Feeding":
				new = new_doc.append("items", {})
				new.item_code = doc.feed_item
				new.warehouse = doc.feed_warehouse
				feed_item_qty = frappe.db.get_value("Bin",{"item_code": doc.feed_item, "warehouse":doc.feed_warehouse},"actual_qty") or 0
				new.qty = feed_item_qty -  doc.total_food_qty

			if doc.transaction_type == "Treatment":
				new = new_doc.append("items", {})
				new.item_code = doc.treatment_item
				new.warehouse = doc.treatment_warehouse
				treatment_item_qty = frappe.db.get_value("Bin",{"item_code": doc.treatment_item, "warehouse":doc.treatment_warehouse},"actual_qty") or 0
				new.qty = treatment_item_qty -  doc.total_food_qty

			new_doc.insert(ignore_permissions=True)
			new_doc.submit()

		if doc.transaction_type == "Expense":
			new_doc = frappe.get_doc({
				'doctype': 'Stock Reconciliation',
				'purpose': 'Stock Reconciliation',
				'posting_date' : doc.posting_date,
				'expense_account' : doc.account,
			})
			serial_no = "\n".join([row.old_code for row in doc.cows])
			
			new = new_doc.append("items", {})
			new.item_code = doc.item_code
			new.qty = doc.actual_qty
			new.warehouse = doc.warehouse
			new.batch_no = doc.batch
			new.serial_no = serial_no
			cow_item_rate = frappe.db.get_value("Bin",{"item_code": doc.item_code, "warehouse":doc.warehouse},"valuation_rate") or 0
			new.valuation_rate = (doc.expense_amount / doc.actual_qty) + cow_item_rate

			new_doc.insert(ignore_permissions=True)
			new_doc.submit()