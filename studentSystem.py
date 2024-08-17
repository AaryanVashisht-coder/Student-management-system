import mysql.connector

def main_menu():
    ch = 'y'
    while ch == 'y':
        print("***********STUDENT REGISTRATION SYSTEM*************")
        print("1: To show databases") 
        print("2: To create a table")
        print("3: To show tables present in the database") 
        print("4: To display structure of the table")
        print("5: To add a record in the table")
        print("6: To update a record in the table") 
        print("7: To delete a record from the table") 
        print("8: To display all the records from the table")
        print("9: To sort the data in descending order of total")
        print("10: To quit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            show_database() 
        elif choice == 2:
            create_table() 
        elif choice == 3:
            show_tables()
        elif choice == 4:
            display_struc() 
        elif choice == 5:
            add_rec()
        elif choice == 6:
            update_rec()
        elif choice == 7:
            delete_rec()
        elif choice == 8:
            fetch_data()
        elif choice == 9:
            topper_list()
        elif choice == 10:
            print("Exiting")
            break
        else:
            print("Wrong input")
        
        ch = input("Do you want to continue? (y/n): ").lower()

def connect_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="school"
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def show_database():
    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("SHOW DATABASES")
        for x in cursor:
            print(x)
        db.close()

def create_table():
    db = connect_db()
    if db:
        cursor = db.cursor()
        try:
            cursor.execute("""
                CREATE TABLE student1 (
                    rollno INT PRIMARY KEY,
                    name VARCHAR(20),
                    stream VARCHAR(50),
                    total INT,
                    grade VARCHAR(3),
                    Class INT
                )
            """)
            print("Table created")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        db.close()

def show_tables():
    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")
        for x in cursor:
            print(x)
        db.close()

def display_struc():
    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("DESC student1")
        for x in cursor:
            print(x)
        db.close()

def add_rec():
    db = connect_db()
    if db:
        cursor = db.cursor()
        try:
            rno = int(input("Enter roll number: ")) 
            nm = input("Enter name: ")
            st = input("Enter stream: ")
            tot = int(input("Enter total: ")) 
            gr = input("Enter grade: ")
            C = int(input("Enter class: "))
            sql_query = "INSERT INTO student1 VALUES (%s, %s, %s, %s, %s, %s)"
            val = (rno, nm, st, tot, gr, C)
            cursor.execute(sql_query, val) 
            db.commit() 
            print("Record added")
        except mysql.connector.Error as err:
            db.rollback()
            print(f"Error: {err}")
        db.close()

def update_rec():
    db = connect_db()
    if db:
        cursor = db.cursor()
        try:
            rno = int(input("Enter rollno: ")) 
            tot = int(input("Enter total: "))
            sql_query = "UPDATE student1 SET total = %s WHERE rollno = %s"
            val = (tot, rno)
            cursor.execute(sql_query, val)
            db.commit()
            print(cursor.rowcount, "record updated")
        except mysql.connector.Error as err:
            db.rollback()
            print(f"Error: {err}")
        db.close()

def delete_rec():
    db = connect_db()
    if db:
        cursor = db.cursor()
        try:
            rno = int(input("Enter rollno: "))
            sql_query = "DELETE FROM student1 WHERE rollno = %s"
            cursor.execute(sql_query, (rno,)) 
            db.commit()
            print(cursor.rowcount, "record deleted")
        except mysql.connector.Error as err:
            db.rollback()
            print(f"Error: {err}")
        db.close()

def fetch_data():
    db = connect_db()
    if db:
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM student1")
            records = cursor.fetchall()
            for x in records:
                print(x[0], x[1], x[2], x[3], x[4], x[5])
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        db.close()

def topper_list():
    db = connect_db()
    if db:
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM student1 ORDER BY total DESC")
            records = cursor.fetchall()
            for x in records:
                print(x[0], x[1], x[2], x[3], x[4], x[5])
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        db.close()

if __name__ == "__main__":
    main_menu()
