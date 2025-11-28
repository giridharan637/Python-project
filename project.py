import csv
import os

def load_csv(filename):
    data = []
    if not os.path.exists(filename):
        return data
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def save_csv(filename, data, fieldnames):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

PATIENT_FILE = "patients.csv"
DOCTOR_FILE = "doctors.csv"
APPT_FILE = "appointments.csv"

patients = load_csv(PATIENT_FILE)
doctors = load_csv(DOCTOR_FILE)
appointments = load_csv(APPT_FILE)

def add_patient():
    pid = input("Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    patients.append({"id": pid, "name": name, "age": age})
    save_csv(PATIENT_FILE, patients, ["id", "name", "age"])
    print("Patient added.\n")

def view_patients():
    for p in patients:
        print(p["id"], p["name"], p["age"])
    print()

def add_doctor():
    did = input("Doctor ID: ")
    name = input("Name: ")
    spec = input("Specialization: ")
    doctors.append({"id": did, "name": name, "spec": spec})
    save_csv(DOCTOR_FILE, doctors, ["id", "name", "spec"])
    print("Doctor added.\n")

def view_doctors():
    for d in doctors:
        print(d["id"], d["name"], d["spec"])
    print()

def book_appointment():
    pid = input("Patient ID: ")
    did = input("Doctor ID: ")
    date = input("Date (DD-MM-YYYY): ")
    appointments.append({"patient_id": pid, "doctor_id": did, "date": date})
    save_csv(APPT_FILE, appointments, ["patient_id", "doctor_id", "date"])
    print("Appointment booked.\n")

def view_appointments():
    for a in appointments:
        print(a["patient_id"], a["doctor_id"], a["date"])
    print()

while True:
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Add Doctor")
    print("4. View Doctors")
    print("5. Book Appointment")
    print("6. View Appointments")
    print("7. Exit")

    c = input("Choice: ")

    if c == "1":
        add_patient()
    elif c == "2":
        view_patients()
    elif c == "3":
        add_doctor()
    elif c == "4":
        view_doctors()
    elif c == "5":
        book_appointment()
    elif c == "6":
        view_appointments()
    elif c == "7":
        break
    else:
        print("Invalid.\n")
