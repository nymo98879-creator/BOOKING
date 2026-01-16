from database import get_connection

def show_available_rooms():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT room_id, room_number, room_type, price
        FROM TBL_ROOM
        WHERE status='Available'
    """)

    rows = cur.fetchall()

    print("-" * 55)
    print(f"{'ID':<10}{'Room No':<15}{'Type':<15}{'Price':<10}")
    print("-" * 55)

    for r in rows:
        print(f"{r[0]:<10}{r[1]:<15}{r[2]:<15}{r[3]:<10}")

    print("-" * 55)

    conn.close()




