from database import get_connection
from datetime import date

def checkout(booking_id):
    conn = get_connection()
    cur = conn.cursor()

    # 1️⃣ Get price and room_id
    cur.execute("""
        SELECT R.price, B.room_id
        FROM [TBL_BOOKING] AS B
        INNER JOIN [TBL_ROOM] AS R ON B.room_id = R.room_id
        WHERE B.booking_id = ?
    """, (booking_id,))



    row = cur.fetchone()
    if not row:
        print("Booking not found!")
        conn.close()
        return

    price, room_id = row

    # 2️⃣ Insert into invoice
    invoice_date = date.today()
    cur.execute("""
        INSERT INTO [TBL_INVOICE]
        (booking_id, total, paid, balance, invoice_date)
        VALUES (?, ?, ?, ?, ?)
    """, (booking_id, price, price, 0, invoice_date))

    # 3️⃣ Update booking status
    cur.execute("""
        UPDATE [TBL_BOOKING] SET booking_status='Checked-out'
        WHERE booking_id=?
    """, (booking_id,))

    # 4️⃣ Update room status
    cur.execute("""
        UPDATE [TBL_ROOM] SET status='Available'
        WHERE room_id=?
    """, (room_id,))

    conn.commit()
    conn.close()
    print("Checkout complete")
