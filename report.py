# from database import get_connection

# def daily_income():
#     conn = get_connection()
#     cur = conn.cursor()

#     sql = """
#     SELECT 
#         i.invoice_date,
#         b.booking_id,
#         c.customer_name,
#         r.room_number,
#         r.room_type,
#         b.check_in,
#         b.check_out,
#         i.total,
#         i.paid,
#         i.balance,
#         u.username
#     FROM 
#         (
#             (
#                 (TBL_INVOICE AS i
#                 INNER JOIN TBL_BOOKING AS b 
#                     ON i.booking_id = b.booking_id)
#                 INNER JOIN TBL_CUSTOMER AS c 
#                     ON b.customer_id = c.customer_id
#             )
#             INNER JOIN TBL_ROOM AS r 
#                 ON b.room_id = r.room_id
#         )
#         INNER JOIN TBL_USER AS u
#             ON b.created_by = u.user_id
#     ORDER BY i.invoice_date
#     """

#     cur.execute(sql)
#     rows = cur.fetchall()

#     if not rows:
#         print("\nNo income records found.\n")
#         return

#     print("\n===== DAILY INCOME REPORT =====")
#     print(f"{'Date':<12}{'BID':<6}{'Customer':<15}{'Room':<6}{'Type':<10}"
#           f"{'Check-in':<20}{'Check-out':<20}{'Total':<10}{'Paid':<10}{'Balance':<10}{'User':<10}")
#     print("-" * 140)

#     for r in rows:
#         print(f"{str(r[0])[:10]:<12}{r[1]:<6}{r[2]:<15}{r[3]:<6}{r[4]:<10}"
#               f"{str(r[5]):<20}{str(r[6]):<20}{r[7]:<10}{r[8]:<10}{r[9]:<10}{r[10]:<10}")

#     print("-" * 140)
# #     conn.close()


# oiuytrewertyuiop[poiutr]
# from database import get_connection

# def daily_income():
#     conn = get_connection()
#     cur = conn.cursor()

#     sql = """
#     SELECT 
#         [invoice_date],
#         SUM([total]) AS daily_total
#     FROM TBL_INVOICE
#     GROUP BY [invoice_date]
#     ORDER BY [invoice_date]
#     """

#     cur.execute(sql)
#     rows = cur.fetchall()

#     if not rows:
#         print("\nNo income records found.\n")
#         conn.close()
#         return

#     print("\n===== DAILY INCOME SUMMARY =====")
#     print(f"{'Date':<12}{'Total Income':<15}")
#     print("-" * 30)

#     for r in rows:
#         print(f"{str(r[0])[:10]:<12}{"$"}{r[1]:<15}")

#     print("-" * 30)
#     conn.close()

from database import get_connection

def daily_room_report():
    conn = get_connection()
    cur = conn.cursor()

    sql = """
    SELECT
        DateValue(I.invoice_date) AS report_date,
        R.room_id,
        R.room_type,
        R.price,
        I.total
    FROM 
        ((TBL_INVOICE AS I
        INNER JOIN TBL_BOOKING AS B ON I.booking_id = B.booking_id)
        INNER JOIN TBL_ROOM AS R ON B.room_id = R.room_id)
    ORDER BY DateValue(I.invoice_date), R.room_id;
    """

    cur.execute(sql)
    rows = cur.fetchall()

    if not rows:
        print("\nNo report data found.\n")
        conn.close()
        return

    print("\n===== DAILY ROOM USAGE REPORT =====")

    current_date = None
    daily_total = 0
    grand_total = 0

    for r in rows:
        report_date, room_id, room_type, price, amount = r

        date_str = str(report_date)[:10]

        if current_date != date_str:
            if current_date is not None:
                print("-" * 40)
                print(f"{'Daily Total:':<28}${daily_total:.2f}\n")
                daily_total = 0

            print(f"\nDate: {date_str}") 
            print(f"{'Room':<6}{'Type':<12}{'Price':<10}{'Amount':<10}")
            print("-" * 40)

            current_date = date_str

        print(f"{room_id:<6}{room_type:<12}${price:<9.2f}${amount:<9.2f}")

        daily_total += amount
        grand_total += amount

    print("-" * 40)
    print(f"{'Daily Total:':<28}${daily_total:.2f}")
    print("\n" + "=" * 40)
    print(f"{'GRAND TOTAL:':<28}${grand_total:.2f}")

    conn.close()
