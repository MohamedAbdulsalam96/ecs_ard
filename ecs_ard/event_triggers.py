from __future__ import unicode_literals
import frappe
from frappe import auth
import datetime
import json, ast
from frappe.utils import now



################ Quotation


@frappe.whitelist()
def quot_onload(doc, method=None):
    pass


@frappe.whitelist()
def quot_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def quot_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def quot_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def quot_validate(doc, method=None):
    pass


@frappe.whitelist()
def quot_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def quot_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def quot_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def quot_before_save(doc, method=None):
    pass


@frappe.whitelist()
def quot_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def quot_on_update(doc, method=None):
    pass


################ Sales Order


@frappe.whitelist()
def so_onload(doc, method=None):
    pass


@frappe.whitelist()
def so_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def so_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def so_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def so_validate(doc, method=None):
    pass


@frappe.whitelist()
def so_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def so_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def so_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def so_before_save(doc, method=None):
    pass


@frappe.whitelist()
def so_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def so_on_update(doc, method=None):
    pass


################ Delivery Note


@frappe.whitelist()
def dn_onload(doc, method=None):
    pass


@frappe.whitelist()
def dn_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def dn_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def dn_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def dn_validate(doc, method=None):
    pass


@frappe.whitelist()
def dn_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def dn_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def dn_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def dn_before_save(doc, method=None):
    pass


@frappe.whitelist()
def dn_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def dn_on_update(doc, method=None):
    pass


################ Sales Invoice


@frappe.whitelist()
def siv_onload(doc, method=None):
    pass


@frappe.whitelist()
def siv_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def siv_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def siv_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def siv_validate(doc, method=None):
    pass


@frappe.whitelist()
def siv_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def siv_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def siv_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def siv_before_save(doc, method=None):
    pass


@frappe.whitelist()
def siv_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def siv_on_update(doc, method=None):
    pass


################ Payment Entry


@frappe.whitelist()
def pe_onload(doc, method=None):
    pass


@frappe.whitelist()
def pe_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def pe_after_insert(doc, method=None):
    pass


def pe_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def pe_validate(doc, method=None):
    pass


@frappe.whitelist()
def pe_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def pe_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def pe_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def pe_before_save(doc, method=None):
    pass


@frappe.whitelist()
def pe_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def pe_on_update(doc, method=None):
    pass


################ Material Request


@frappe.whitelist()
def mr_onload(doc, method=None):
    pass


@frappe.whitelist()
def mr_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def mr_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def mr_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def pe_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def mr_validate(doc, method=None):
    pass


@frappe.whitelist()
def mr_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def mr_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def mr_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def mr_before_save(doc, method=None):
    pass


@frappe.whitelist()
def mr_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def mr_on_update(doc, method=None):
    pass


################ Purchase Order


@frappe.whitelist()
def po_onload(doc, method=None):
    pass


@frappe.whitelist()
def po_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def po_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def po_before_validate(doc, method=None):
   # for x in doc.items:
    #    x.rate= doc.total_price2/x.qty
    pass






@frappe.whitelist()
def po_validate(doc, method=None):
    pass


@frappe.whitelist()
def po_on_submit(doc, method=None):
    pass

    # frappe.msgprint(" Installation Note Record " + new_doc.name + " created ")


@frappe.whitelist()
def po_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def po_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def po_before_save(doc, method=None):
    pass


@frappe.whitelist()
def po_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def po_on_update(doc, method=None):
    pass


################ Purchase Receipt

### demo.event_triggers.call_to_store


@frappe.whitelist()
def pr_onload(doc, method=None):
    pass





@frappe.whitelist()
def pr_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def pr_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def pr_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def pr_validate(doc, method=None):
    for item in doc.items:
        if item.item_group == "Animals":
            if not doc.average_weight1:
                frappe.throw("Please Insert Average Weight")
            item.weight_per_unit = (doc.average_weight1 / item.qty)
            item.total_weight = doc.average_weight1
            item.weight_uom = "Kg"

            max_weight = frappe.db.get_value("Warehouse", item.warehouse, "max_weight")
            min_weight = frappe.db.get_value("Warehouse", item.warehouse, "min_weight")
            if (item.weight_per_unit > max_weight) or (item.weight_per_unit < min_weight):
                frappe.msgprint("Weight Per Unit (" + str(round(item.weight_per_unit, 2))  
                                + " KG) Is Not In Range Of Warehouse (" + str(item.warehouse)
                                + ")" + "<br>" + "Warehouse Weight Range: (" + str(int(min_weight)) 
                                + " KG - " + str(int(max_weight)) + " KG)")


@frappe.whitelist()
def pr_on_submit(doc, method=None):
    for item in doc.items:
        if item.item_group == "Animals":
            mat_req_name, acc_qty, po_name = frappe.db.get_value(
                "Purchase Receipt Item", {"parent": doc.name}, ["material_request", "qty", "purchase_order"]
            )
            average_weight= frappe.db.get_value(
                "Material Request", {"name": mat_req_name}, ["average_weights1"]
            )
            tot_qty=0
            est_total=0

            po = ""
            if po_name:
                po = po_name

            if frappe.db.exists("Purchase Order", {"name": po_name}):
                tot_qty, est_total = frappe.db.get_value(
                    "Purchase Order", {"name": po_name}, ["total_qty", "estimated_total1"]
                )
            rec_qty, rate = frappe.db.get_value(
                "Purchase Receipt Item", {"parent": doc.name}, ["received_qty", "rate"]
            )


            if tot_qty - rec_qty !=0:
                if est_total==0:
                # doc.average_weight1 = average_weight
                    doc.estimated_total1 = (doc.average_weight1 - doc.current_weight1)
                else:
                    #doc.average_weight1 = est_total
                    doc.estimated_total1 = (doc.average_weight1 - doc.current_weight1)
            else:
                #doc.average_weight1 = est_total
                doc.estimated_total1 = (doc.average_weight1 -doc.current_weight1)
            frappe.db.set_value('Purchase Order', po_name, 'estimated_total1', doc.estimated_total1)

            serials = frappe.db.sql(f""" select name from `tabSerial No` where item_code = '{item.item_code}' and purchase_document_no = '{doc.name}' """, as_dict=1)
            batch = frappe.db.get_value("Batch", {"reference_name": doc.name}, "name")
            
            for serial in serials:
                record_name = str(batch) + " - " + str(serial.name)
                row_name1 = str(doc.name) + str(record_name)
                row_name2 = str(doc.name) + str(record_name) + str(doc.average_weight1)
                frappe.db.sql(""" INSERT INTO `tabCOW` (purchase_order, purchase_receipt, code, kilogram, item, item_name, current_warehouse, batch, creation, name)
                                VALUES ('{purchase_order}', '{purchase_receipt}', '{code}', '{kilogram}', '{item}', '{item_name}', '{current_warehouse}', 
                                '{batch}', '{creation}', '{name}')
                                """.format(purchase_order=po, purchase_receipt=doc.name, code=serial.name,
                                            kilogram=(float(doc.average_weight1) / item.qty),  item=item.item_code, item_name=item.item_name,
                                            current_warehouse=doc.set_warehouse, batch=batch, creation=now(), name=record_name))
                
                frappe.db.sql(""" INSERT INTO `tabCow History` (warehouse, reference_doctype, reference_name, date, parent, parentfield, parenttype, name)
                                VALUES ('{warehouse}', '{reference_doctype}', '{reference_name}', '{date}', '{parent}', '{parentfield}', '{parenttype}', '{name}')
                                """.format(warehouse=doc.set_warehouse, reference_doctype="Purchase Receipt", reference_name=doc.name, 
                                           date=(datetime.datetime.now()), parent=record_name, parentfield="warehouse", parenttype="COW", name=row_name1))
                
                frappe.db.sql(""" INSERT INTO `tabCow Weight History` (weight, date, remarks, reference_doctype, reference_name, parent, parentfield, parenttype, name)
                                VALUES ('{weight}', '{date}', '{remarks}', '{reference_doctype}', '{reference_name}', '{parent}', '{parentfield}', '{parenttype}', '{name}')
                                """.format(weight=(float(doc.average_weight1) / item.qty), date=(datetime.datetime.now()), 
                                           remarks="الوزن عند الإستلام", reference_doctype="Purchase Receipt", reference_name=doc.name,
                                           parent=record_name, parentfield="weight_history", parenttype="COW", name=row_name2))




            # new_cow = frappe.get_doc(
            #     {
            #         "doctype": "COW",
            #         "purchase_order": po_name,
            #         "purchase_receipt": doc.name,
            #         "code" : serial.name,
            #         "kilogram": (float(doc.average_weight1) / item.qty),
            #         "item": item.item_code,
            #         "item_name": item.item_name,
            #         "current_warehouse": doc.set_warehouse,
            #         "warehouse": [
            #             {
            #                 "warehouse": doc.set_warehouse,
            #                 "weight": (float(doc.average_weight1) / item.qty),
            #                 "purchase_receipt": doc.name,
            #                 "date": (datetime.datetime.now()),
            #             }
            #         ],
            #         "rate": rate
            #     }
            # )
            # new_cow.insert()
            # new_cow.submit()

@frappe.whitelist()
def pr_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def pr_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def pr_before_save(doc, method=None):
    pass


@frappe.whitelist()
def pr_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def pr_on_update(doc, method=None):
    pass


################ Purchase Invoice


@frappe.whitelist()
def piv_onload(doc, method=None):
    pass


@frappe.whitelist()
def piv_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def piv_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def piv_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def piv_validate(doc, method=None):
    pass


@frappe.whitelist()
def piv_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def piv_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def piv_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def piv_before_save(doc, method=None):
    pass


@frappe.whitelist()
def piv_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def piv_on_update(doc, method=None):
    pass


################ Employee Advance


@frappe.whitelist()
def emad_onload(doc, method=None):
    pass


@frappe.whitelist()
def emad_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def emad_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def emad_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def emad_validate(doc, method=None):
    pass


@frappe.whitelist()
def emad_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def emad_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def emad_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def emad_before_save(doc, method=None):
    pass


@frappe.whitelist()
def emad_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def emad_on_update(doc, method=None):
    pass


################ Expense Claim


@frappe.whitelist()
def excl_onload(doc, method=None):
    pass


@frappe.whitelist()
def excl_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def excl_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def excl_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def excl_validate(doc, method=None):
    pass


@frappe.whitelist()
def excl_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def excl_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def excl_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def excl_before_save(doc, method=None):
    pass


@frappe.whitelist()
def excl_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def excl_on_update(doc, method=None):
    pass


################ Stock Entry


@frappe.whitelist()
def ste_onload(doc, method=None):
    pass


@frappe.whitelist()
def ste_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def ste_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def ste_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def ste_validate(doc, method=None):
    pass


@frappe.whitelist()
def ste_on_submit(doc, method=None):
    if doc.stock_entry_type == 'Material Transfer':
        for item in doc.items:
            if item.item_group == "Animals":
                cow = frappe.get_doc("COW", {'item': item.item_code, 'code' : item.serial_no, 'batch' : item.batch_no})
                cow.append("warehouse", {
                    'warehouse': item.t_warehouse,
                    'reference_doctype': "Stock Entry",
                    'reference_name': doc.name,
                    'date' : doc.posting_date,
                    'remarks': doc.name,
                })
                cow.current_warehouse = item.t_warehouse
                cow.save()


@frappe.whitelist()
def ste_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def ste_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def ste_before_save(doc, method=None):
    pass


@frappe.whitelist()
def ste_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def ste_on_update(doc, method=None):
    pass


################ Blanket Order


@frappe.whitelist()
def blank_onload(doc, method=None):
    pass


@frappe.whitelist()
def blank_before_insert(doc, method=None):
    pass


@frappe.whitelist()
def blank_after_insert(doc, method=None):
    pass


@frappe.whitelist()
def blank_before_validate(doc, method=None):
    pass


@frappe.whitelist()
def blank_validate(doc, method=None):
    pass


@frappe.whitelist()
def blank_on_submit(doc, method=None):
    pass


@frappe.whitelist()
def blank_on_cancel(doc, method=None):
    pass


@frappe.whitelist()
def blank_on_update_after_submit(doc, method=None):
    pass


@frappe.whitelist()
def blank_before_save(doc, method=None):
    pass


@frappe.whitelist()
def blank_before_cancel(doc, method=None):
    pass


@frappe.whitelist()
def blank_on_update(doc, method=None):
    pass

