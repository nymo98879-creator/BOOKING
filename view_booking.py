from database import get_connection
def view_active_bookings():
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        SELECT 
    b.[booking_id],
    c.[customer_name],
    r.[room_number],
    b.[check_in],
    b.[check_out],
    b.[booking_status]
FROM 
    ([TBL_BOOKING] AS b
     INNER JOIN [TBL_CUSTOMER] AS c 
        ON b.[customer_id] = c.[customer_id])
    INNER JOIN [TBL_ROOM] AS r 
        ON b.[room_id] = r.[room_id]
WHERE b.[booking_status] <> 'Checked-out'

    """

    cur.execute(sql)
    rows = cur.fetchall()

    if not rows:
        print("\nNo active bookings found.\n")
        conn.close()
        return

    print("\n===== ACTIVE BOOKINGS =====")
    print(f"{'ID':<8}{'Customer':<20}{'Room':<10}{'Check-in-date':<30}{'Check-out_date':<30}{'Status':<20}")
    print("-" * 110)

    for row in rows:
        print(f"{row[0]:<8}{row[1]:<20}{row[2]:<10}{str(row[3]):<30}{str(row[4]):<30}{row[5]:<20}")

    print("-" * 110)

    conn.close()
