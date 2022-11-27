import frappe


def after_install():
    insert_doc_county_code("Baranya megye", "02", "22")
    insert_doc_county_code("Bács-Kiskun megye", "03", "23")
    insert_doc_county_code("Békés megye", "04", "24")
    insert_doc_county_code("Borsod-Abaúj-Zemplén megye", "05", "25")
    insert_doc_county_code("Csongrád megye", "06", "26")
    insert_doc_county_code("Fejér megye", "07", "27")
    insert_doc_county_code("Győr-Moson-Sopron megye", "08", "28")
    insert_doc_county_code("Hajdú-Bihar megye", "09", "29")
    insert_doc_county_code("Heves megye", "10", "30")
    insert_doc_county_code("Komárom-Esztergom megye", "11", "31")
    insert_doc_county_code("Nógrád megye", "12", "32")
    insert_doc_county_code("Pest megye", "13", "33")
    insert_doc_county_code("Somogy megye", "14", "34")
    insert_doc_county_code("Szabolcs-Szatmár-Bereg megye", "15", "35")
    insert_doc_county_code("Jász-Nagykun-Szolnok megye", "16", "36")
    insert_doc_county_code("Tolna megye", "17", "37")
    insert_doc_county_code("Vas megye", "18", "38")
    insert_doc_county_code("Veszprém megye", "19", "39")
    insert_doc_county_code("Zala megye", "20", "40")
    insert_doc_county_code("Észak-Budapest", "41", "41")
    insert_doc_county_code("Kelet-Budapest", "42", "42")
    insert_doc_county_code("Dél-Budapest", "43", "43")
    insert_doc_county_code("Pest Megyei és Fővárosi Kiemelt Adózók Igazgatósága", "44", "44")
    insert_doc_county_code("Kizárólagos illetéskességű adóalanyok", "51", "51")


def insert_doc_county_code(name, county_code_for_company, county_code_for_self_employed):
    doc = frappe.get_doc({
        "doctype": "NavGovHuCountyCode",
        "name": name,
        "county_name": name,
        "county_code_for_company": county_code_for_company,
        "county_code_for_self_employed": county_code_for_self_employed,
    })
    doc.flags.name_set = True
    doc.insert()

