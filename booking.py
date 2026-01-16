
# from database import get_connection

# def create_booking():
#     customer_id = int(input("Customer ID: "))
#     room_id = int(input("Room ID: "))
#     check_in = input("Check-in date (YYYY-MM-DD): ")
#     check_out = input("Check-out date (YYYY-MM-DD): ")

#     conn = get_connection()
#     cur = conn.cursor()

#     cur.execute("""
#         INSERT INTO TBL_BOOKING
#         (customer_id, room_id, [check_in], [check_out], booking_status)
#         VALUES (?, ?, ?, ?, 'Booked')
#     """, (customer_id, room_id, check_in, check_out))

#     cur.execute("""
#         UPDATE TBL_ROOM
#         SET status='Booked'
#         WHERE room_id=?
#     """, (room_id,))

#     conn.commit()
#     conn.close()

#     print("✅ Booking created successfully")
from database import get_connection
from datetime import datetime

def create_booking():
    customer_id = int(input("Customer ID: "))
    room_id = int(input("Room ID: "))
    check_in = input("Check-in date (YYYY-MM-DD): ")
    check_out = input("Check-out date (YYYY-MM-DD): ")

    check_in_dt = datetime.strptime(check_in, "%Y-%m-%d")
    check_out_dt = datetime.strptime(check_out, "%Y-%m-%d")

    if check_out_dt <= check_in_dt:
        print("❌ Check-out must be after check-in")
        return

    conn = get_connection()
    cur = conn.cursor()

    # ✅ Overlap check (CORRECT)
    cur.execute("""
        SELECT booking_id
        FROM TBL_BOOKING
        WHERE room_id = ?
          AND booking_status IN ('Booked', 'Checked-in')
          AND [check_in] < ?
          AND [check_out] > ?
    """, (room_id, check_out_dt, check_in_dt))

    if cur.fetchone():
        print("❌ This room is already booked for those dates.")
        conn.close()
        return

    # ✅ Insert booking
    cur.execute("""
        INSERT INTO TBL_BOOKING
        (customer_id, room_id, [check_in], [check_out], booking_status)
        VALUES (?, ?, ?, ?, 'Booked')
    """, (customer_id, room_id, check_in_dt, check_out_dt))

    cur.execute("""
        UPDATE TBL_ROOM
        SET status='Booked'
        WHERE room_id=?
    """, (room_id,))

    conn.commit()
    conn.close()

    print("✅ Booking created successfully")
