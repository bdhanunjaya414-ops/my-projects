import sqlite3

# ------------------ DATABASE SETUP ------------------ #
def create_db():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            disease TEXT,
            phone TEXT
        )
    """)
    conn.commit()
    conn.close()


# ------------------ ADD PATIENT ------------------ #
def add_patient():
    print("\n--- Add Patient ---")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender (M/F/O): ")
    disease = input("Enter Disease/Problem: ")
    phone = input("Enter Phone Number: ")

    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, age, gender, disease, phone) VALUES (?, ?, ?, ?, ?)",
                   (name, age, gender, disease, phone))
    conn.commit()
    conn.close()
    print("\nPatient Added Successfully!\n")


# ------------------ VIEW ALL PATIENTS ------------------ #
def view_patients():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()
    conn.close()

    print("\n--- All Patients ---")
    if not data:
        print("No patient records found.\n")
        return

    for row in data:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Gender: {row[3]} | Disease: {row[4]} | Phone: {row[5]}")
    print()


# ------------------ SEARCH PATIENT ------------------ #
def search_patient():
    keyword = input("Enter patient name to search: ")

    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE name LIKE ?", ('%' + keyword + '%',))
    data = cursor.fetchall()
    conn.close()

    print("\n--- Search Results ---")
    if not data:
        print("No patient found with that name.")
        return

    for row in data:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Gender: {row[3]} | Disease: {row[4]} | Phone: {row[5]}")
    print()


# ------------------ UPDATE PATIENT ------------------ #
def update_patient():
    pid = input("Enter Patient ID to update: ")

    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = ?", (pid,))
    data = cursor.fetchone()

    if not data:
        print("\nPatient ID not found!\n")
        return

    print("\n--- Update Patient ---")
    name = input(f"Enter New Name ({data[1]}): ") or data[1]
    age = input(f"Enter New Age ({data[2]}): ") or data[2]
    gender = input(f"Enter New Gender ({data[3]}): ") or data[3]
    disease = input(f"Enter New Disease ({data[4]}): ") or data[4]
    phone = input(f"Enter New Phone ({data[5]}): ") or data[5]

    cursor.execute("""
        UPDATE patients SET name=?, age=?, gender=?, disease=?, phone=? WHERE id=?
    """, (name, age, gender, disease, phone, pid))

    conn.commit()
    conn.close()
    print("\nPatient Updated Successfully!\n")


# ------------------ DELETE PATIENT ------------------ #
def delete_patient():
    pid = input("Enter Patient ID to delete: ")

    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = ?", (pid,))
    conn.commit()
    conn.close()

    print("\nPatient Record Deleted Successfully!\n")


# ------------------ MAIN MENU ------------------ #
def main():
    create_db()
    while True:
        print("====== Hospital Management System ======")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            print("Thank you! Exiting System...")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
