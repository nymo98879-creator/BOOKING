from database import get_connection
from datetime import datetime

def check_in():
    booking_id = int(input("Booking ID: "))
    check_in_time = datetime.now()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT room_id FROM TBL_BOOKING
        WHERE booking_id=? AND booking_status='Booked'
    """, (booking_id,))

    result = cur.fetchone()
    if not result:
        print("Invalid booking or already checked in")
        conn.close()
        return

    room_id = result[0]

    cur.execute("""
        UPDATE TBL_BOOKING
        SET booking_status='Checked-in', check_in=?
        WHERE booking_id=?
    """, (check_in_time, booking_id))

    cur.execute("""
        UPDATE TBL_ROOM
        SET status='Occupied'
        WHERE room_id=?
    """, (room_id,))

    conn.commit()
    conn.close()

    print("Check-in completed")

