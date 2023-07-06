import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bumblebee291",
    database="airline_management_system"
)

# Create the main window
window = tk.Tk()
window.title("Airline Management System")

# Function to execute a SQL query and display the result in a message box
def execute_query(query, success_message, error_message):
    try:
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        cursor.close()
        messagebox.showinfo("Success", success_message)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"{error_message}\n\nError Message: {error}")

# Create labels, entry fields, and buttons for Aeroplane
aeroplane_callsign_label = tk.Label(window, text="Callsign:")
aeroplane_callsign_label.pack()

aeroplane_callsign_entry = tk.Entry(window)
aeroplane_callsign_entry.pack()

aeroplane_airline_id_label = tk.Label(window, text="Airline ID:")
aeroplane_airline_id_label.pack()

aeroplane_airline_id_entry = tk.Entry(window)
aeroplane_airline_id_entry.pack()

aeroplane_model_label = tk.Label(window, text="Model:")
aeroplane_model_label.pack()

aeroplane_model_entry = tk.Entry(window)
aeroplane_model_entry.pack()

aeroplane_manufacturer_label = tk.Label(window, text="Manufacturer:")
aeroplane_manufacturer_label.pack()

aeroplane_manufacturer_entry = tk.Entry(window)
aeroplane_manufacturer_entry.pack()

def insert_aeroplane():
    callsign = aeroplane_callsign_entry.get()
    airline_id = aeroplane_airline_id_entry.get()
    model = aeroplane_model_entry.get()
    manufacturer = aeroplane_manufacturer_entry.get()
    query = f"INSERT INTO Aeroplane (Callsign, Airline_ID, Model, Manufacturer) VALUES ('{callsign}', {airline_id}, '{model}', '{manufacturer}')"
    success_message = "Aeroplane inserted successfully!"
    error_message = "Failed to insert Aeroplane!"
    execute_query(query, success_message, error_message)

aeroplane_insert_button = tk.Button(window, text="Insert Aeroplane", command=insert_aeroplane)
aeroplane_insert_button.pack()

def update_aeroplane():
    callsign = aeroplane_callsign_entry.get()
    airline_id = aeroplane_airline_id_entry.get()
    model = aeroplane_model_entry.get()
    manufacturer = aeroplane_manufacturer_entry.get()
    query = f"UPDATE Aeroplane SET Airline_ID = {airline_id}, Model = '{model}', Manufacturer = '{manufacturer}' WHERE Callsign = '{callsign}'"
    success_message = "Aeroplane updated successfully!"
    error_message = "Failed to update Aeroplane!"
    execute_query(query, success_message, error_message)

aeroplane_update_button = tk.Button(window, text="Update Aeroplane", command=update_aeroplane)
aeroplane_update_button.pack()

def delete_aeroplane():
    callsign = aeroplane_callsign_entry.get()
    query = f"DELETE FROM Aeroplane WHERE Callsign = '{callsign}'"
    success_message = "Aeroplane deleted successfully!"
    error_message = "Failed to delete Aeroplane!"
    execute_query(query, success_message, error_message)

aeroplane_delete_button = tk.Button(window, text="Delete Aeroplane", command=delete_aeroplane)
aeroplane_delete_button.pack()

# Create labels, entry fields, and buttons for Airline
airline_id_label = tk.Label(window, text="Airline ID:")
airline_id_label.pack()

airline_id_entry = tk.Entry(window)
airline_id_entry.pack()

airline_name_label = tk.Label(window, text="Name:")
airline_name_label.pack()

airline_name_entry = tk.Entry(window)
airline_name_entry.pack()

airline_home_base_label = tk.Label(window, text="Home Base:")
airline_home_base_label.pack()

airline_home_base_entry = tk.Entry(window)
airline_home_base_entry.pack()

airline_phone_no_label = tk.Label(window, text="Phone No:")
airline_phone_no_label.pack()

airline_phone_no_entry = tk.Entry(window)
airline_phone_no_entry.pack()

airline_email_label = tk.Label(window, text="Email:")
airline_email_label.pack()

airline_email_entry = tk.Entry(window)
airline_email_entry.pack()

def insert_airline():
    airline_id = airline_id_entry.get()
    name = airline_name_entry.get()
    home_base = airline_home_base_entry.get()
    phone_no = airline_phone_no_entry.get()
    email = airline_email_entry.get()
    query = f"INSERT INTO Airline (Airline_ID, Name, Home_Base, Phone_NO, email) VALUES ({airline_id}, '{name}', '{home_base}', {phone_no}, '{email}')"
    success_message = "Airline inserted successfully!"
    error_message = "Failed to insert Airline!"
    execute_query(query, success_message, error_message)

airline_insert_button = tk.Button(window, text="Insert Airline", command=insert_airline)
airline_insert_button.pack()

def update_airline():
    airline_id = airline_id_entry.get()
    name = airline_name_entry.get()
    home_base = airline_home_base_entry.get()
    phone_no = airline_phone_no_entry.get()
    email = airline_email_entry.get()
    query = f"UPDATE Airline SET Name = '{name}', Home_Base = '{home_base}', Phone_NO = {phone_no}, email = '{email}' WHERE Airline_ID = {airline_id}"
    success_message = "Airline updated successfully!"
    error_message = "Failed to update Airline!"
    execute_query(query, success_message, error_message)

airline_update_button = tk.Button(window, text="Update Airline", command=update_airline)
airline_update_button.pack()

def delete_airline():
    airline_id = airline_id_entry.get()
    query = f"DELETE FROM Airline WHERE Airline_ID = {airline_id}"
    success_message = "Airline deleted successfully!"
    error_message = "Failed to delete Airline!"
    execute_query(query, success_message, error_message)

airline_delete_button = tk.Button(window, text="Delete Airline", command=delete_airline)
airline_delete_button.pack()

# Create labels, entry fields, and buttons for Boarding Pass
boarding_pass_id_label = tk.Label(window, text="Pass ID:")
boarding_pass_id_label.pack()

boarding_pass_id_entry = tk.Entry(window)
boarding_pass_id_entry.pack()

boarding_pass_flight_no_label = tk.Label(window, text="Flight No:")
boarding_pass_flight_no_label.pack()

boarding_pass_flight_no_entry = tk.Entry(window)
boarding_pass_flight_no_entry.pack()

boarding_pass_passenger_id_label = tk.Label(window, text="Passenger ID:")
boarding_pass_passenger_id_label.pack()

boarding_pass_passenger_id_entry = tk.Entry(window)
boarding_pass_passenger_id_entry.pack()

boarding_pass_ticket_id_label = tk.Label(window, text="Ticket ID:")
boarding_pass_ticket_id_label.pack()

boarding_pass_ticket_id_entry = tk.Entry(window)
boarding_pass_ticket_id_entry.pack()

boarding_pass_gate_label = tk.Label(window, text="Gate:")
boarding_pass_gate_label.pack()

boarding_pass_gate_entry = tk.Entry(window)
boarding_pass_gate_entry.pack()

boarding_pass_check_in_label = tk.Label(window, text="Check-in:")
boarding_pass_check_in_label.pack()

boarding_pass_check_in_entry = tk.Entry(window)
boarding_pass_check_in_entry.pack()

boarding_pass_boarding_label = tk.Label(window, text="Boarding:")
boarding_pass_boarding_label.pack()

boarding_pass_boarding_entry = tk.Entry(window)
boarding_pass_boarding_entry.pack()

def insert_boarding_pass():
    pass_id = boarding_pass_id_entry.get()
    flight_no = boarding_pass_flight_no_entry.get()
    passenger_id = boarding_pass_passenger_id_entry.get()
    ticket_id = boarding_pass_ticket_id_entry.get()
    gate = boarding_pass_gate_entry.get()
    check_in = boarding_pass_check_in_entry.get()
    boarding = boarding_pass_boarding_entry.get()
    query = f"INSERT INTO Boarding_pass (Pass_ID, Flight_NO, Passenger_ID, Ticket_ID, Gate, Check_in, Boarding) VALUES ({pass_id}, {flight_no}, {passenger_id}, {ticket_id}, '{gate}', '{check_in}', '{boarding}')"
    success_message = "Boarding Pass inserted successfully!"
    error_message = "Failed to insert Boarding Pass!"
    execute_query(query, success_message, error_message)

boarding_pass_insert_button = tk.Button(window, text="Insert Boarding Pass", command=insert_boarding_pass)
boarding_pass_insert_button.pack()

def update_boarding_pass():
    pass_id = boarding_pass_id_entry.get()
    flight_no = boarding_pass_flight_no_entry.get()
    passenger_id = boarding_pass_passenger_id_entry.get()
    ticket_id = boarding_pass_ticket_id_entry.get()
    gate = boarding_pass_gate_entry.get()
    check_in = boarding_pass_check_in_entry.get()
    boarding = boarding_pass_boarding_entry.get()
    query = f"UPDATE Boarding_pass SET Flight_NO = {flight_no}, Passenger_ID = {passenger_id}, Ticket_ID = {ticket_id}, Gate = '{gate}', Check_in = '{check_in}', Boarding = '{boarding}' WHERE Pass_ID = {pass_id}"
    success_message = "Boarding Pass updated successfully!"
    error_message = "Failed to update Boarding Pass!"
    execute_query(query, success_message, error_message)

boarding_pass_update_button = tk.Button(window, text="Update Boarding Pass", command=update_boarding_pass)
boarding_pass_update_button.pack()

def delete_boarding_pass():
    pass_id = boarding_pass_id_entry.get()
    query = f"DELETE FROM Boarding_pass WHERE Pass_ID = {pass_id}"
    success_message = "Boarding Pass deleted successfully!"
    error_message = "Failed to delete Boarding Pass!"
    execute_query(query, success_message, error_message)

boarding_pass_delete_button = tk.Button(window, text="Delete Boarding Pass", command=delete_boarding_pass)
boarding_pass_delete_button.pack()

# Create labels, entry fields, and buttons for Cabin Crew
cabin_crew_id_label = tk.Label(window, text="Crew ID:")
cabin_crew_id_label.pack()

cabin_crew_id_entry = tk.Entry(window)
cabin_crew_id_entry.pack()

cabin_crew_flight_no_label = tk.Label(window, text="Flight No:")
cabin_crew_flight_no_label.pack()

cabin_crew_flight_no_entry = tk.Entry(window)
cabin_crew_flight_no_entry.pack()

cabin_crew_position_label = tk.Label(window, text="Position:")
cabin_crew_position_label.pack()

cabin_crew_position_entry = tk.Entry(window)
cabin_crew_position_entry.pack()

cabin_crew_name_label = tk.Label(window, text="Name:")
cabin_crew_name_label.pack()

cabin_crew_name_entry = tk.Entry(window)
cabin_crew_name_entry.pack()

def insert_cabin_crew():
    crew_id = cabin_crew_id_entry.get()
    flight_no = cabin_crew_flight_no_entry.get()
    position = cabin_crew_position_entry.get()
    name = cabin_crew_name_entry.get()
    query = f"INSERT INTO Cabin_crew (Crew_ID, Flight_NO, Position, Name) VALUES ({crew_id}, {flight_no}, '{position}', '{name}')"
    success_message = "Cabin Crew inserted successfully!"
    error_message = "Failed to insert Cabin Crew!"
    execute_query(query, success_message, error_message)

cabin_crew_insert_button = tk.Button(window, text="Insert Cabin Crew", command=insert_cabin_crew)
cabin_crew_insert_button.pack()

def update_cabin_crew():
    crew_id = cabin_crew_id_entry.get()
    flight_no = cabin_crew_flight_no_entry.get()
    position = cabin_crew_position_entry.get()
    name = cabin_crew_name_entry.get()
    query = f"UPDATE Cabin_crew SET Flight_NO = {flight_no}, Position = '{position}', Name = '{name}' WHERE Crew_ID = {crew_id}"
    success_message = "Cabin Crew updated successfully!"
    error_message = "Failed to update Cabin Crew!"
    execute_query(query, success_message, error_message)

cabin_crew_update_button = tk.Button(window, text="Update Cabin Crew", command=update_cabin_crew)
cabin_crew_update_button.pack()

def delete_cabin_crew():
    crew_id = cabin_crew_id_entry.get()
    query = f"DELETE FROM Cabin_crew WHERE Crew_ID = {crew_id}"
    success_message = "Cabin Crew deleted successfully!"
    error_message = "Failed to delete Cabin Crew!"
    execute_query(query, success_message, error_message)

cabin_crew_delete_button = tk.Button(window, text="Delete Cabin Crew", command=delete_cabin_crew)
cabin_crew_delete_button.pack()

# Run the main event loop
window.mainloop()
