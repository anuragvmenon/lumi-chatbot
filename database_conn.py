import sqlite3

def GetData(FirstName, Feedback):
    db_file = "journal.db"
    
    # Connect to the database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_file)
    mycursor = conn.cursor()

    # Create the table if it doesn't exist
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS user_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT,
            Feedback TEXT
        )
    ''')

    # Insert the data
    sql = 'INSERT INTO user_info (FirstName, Feedback) VALUES (?, ?)'
    mycursor.execute(sql, (FirstName, Feedback))
    conn.commit()
    
    print(mycursor.rowcount, "Record successfully inserted.")
    
    # Close the connection
    conn.close()
