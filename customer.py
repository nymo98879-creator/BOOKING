from database import get_connection

def add_customer():
    name = input("Customer name: ")
    phone = input("Phone: ")
    id_card = input("ID card: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO TBL_CUSTOMER (customer_name, phone, id_card, status)
        VALUES (?, ?, ?, True)
    """, (name, phone, id_card))

    conn.commit()
    conn.close()
    print("Customer added")
