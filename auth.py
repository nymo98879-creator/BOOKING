from database import get_connection

def login():
    username = input("Username: ")
    password = input("Password: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT role FROM TBL_USER WHERE username=? AND password=? AND status=True",
        (username, password)
    )

    user = cur.fetchone()
    conn.close()

    if user:
        print("Login successful")
        return user[0]
    else:
        print("Invalid credentials")
        return None
