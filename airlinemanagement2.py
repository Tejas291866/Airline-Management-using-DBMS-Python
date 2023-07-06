import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

# Create a window
window = tk.Tk()
window.title("Airline Management System")
window.attributes('-fullscreen', True)  # Set full screen
window.configure(bg="white")

# Load background images
background_image_home = ImageTk.PhotoImage(Image.open("background.jpg"))
background_image_aeroplane = ImageTk.PhotoImage(Image.open("background.jpg"))
background_image_boarding_pass = ImageTk.PhotoImage(Image.open("background.jpg"))
background_image_cabin_crew = ImageTk.PhotoImage(Image.open("background.jpg"))

# Create the main frame
main_frame = tk.Frame(window)
main_frame.pack(fill="both", expand=True)

# Dictionary to keep track of the pages
pages = {}

# Function to show a specific page
def show_page(page):
    # Hide all pages
    for p in pages.values():
        p.pack_forget()
    # Show the selected page
    page.pack()

# Function to execute a MySQL query
def execute_query(query, success_message, error_message):
    try:
        cursor.execute(query)
        db.commit()
        messagebox.showinfo("Success", success_message)
    except mysql.connector.Error as error:
        db.rollback()
        messagebox.showerror("Error", f"{error_message}\nError Message: {error}")

# Function to handle the Aeroplane page submit button click
def insert_aeroplane():
    callsign = callsign_entry.get()
    airline_id = airline_id_entry.get()
    model = model_entry.get()
    manufacturer = manufacturer_entry.get()

    query = f"INSERT INTO Aeroplane (Callsign, Airline_ID, Model, Manufacturer) VALUES ('{callsign}', {airline_id}, '{model}', '{manufacturer}')"
    execute_query(query, "Aeroplane record inserted successfully!", "Error occurred while inserting Aeroplane record.")

# Function to handle the Aeroplane page update button click
def update_aeroplane():
    callsign = callsign_entry.get()
    new_airline_id = new_airline_id_entry.get()

    query = f"UPDATE Aeroplane SET Airline_ID = {new_airline_id} WHERE Callsign = '{callsign}'"
    execute_query(query, "Aeroplane record updated successfully!", "Error occurred while updating Aeroplane record.")

# Function to handle the Aeroplane page delete button click
def delete_aeroplane():
    callsign = callsign_entry.get()

    query = f"DELETE FROM Aeroplane WHERE Callsign = '{callsign}'"
    execute_query(query, "Aeroplane record deleted successfully!", "Error occurred while deleting Aeroplane record.")

# Create a frame for the Home page
home_page = tk.Frame(main_frame, bg="white")
home_page.background = background_image_home
home_page.pack(fill="both", expand=True)

# Create the Boarding Pass button
def open_boarding_pass_page():
    show_page(boarding_pass_page)

boarding_pass_button = tk.Button(home_page, text="Boarding Pass", font=("Arial", 12), command=open_boarding_pass_page)
boarding_pass_button.pack()

# Create the Cabin Crew button
def open_cabin_crew_page():
    show_page(cabin_crew_page)

cabin_crew_button = tk.Button(home_page, text="Cabin Crew", font=("Arial", 12), command=open_cabin_crew_page)
cabin_crew_button.pack()

# Create a frame for the Aeroplane page
aeroplane_page = tk.Frame(main_frame, bg="white")
aeroplane_page.background = background_image_aeroplane

# Create a frame for the Aeroplane page
aeroplane_page = tk.Frame(main_frame, bg="white")
aeroplane_page.background = background_image_aeroplane
aeroplane_page.pack(fill="both", expand=True)

# Create labels and entry fields for the Aeroplane page
aeroplane_callsign_label = tk.Label(aeroplane_page, text="Callsign:", font=("Arial", 12), bg="white")
aeroplane_callsign_label.pack()
aeroplane_callsign_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
aeroplane_callsign_entry.pack()

aeroplane_airline_label = tk.Label(aeroplane_page, text="Airline ID:", font=("Arial", 12), bg="white")
aeroplane_airline_label.pack()
aeroplane_airline_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
aeroplane_airline_entry.pack()

aeroplane_model_label = tk.Label(aeroplane_page, text="Model:", font=("Arial", 12), bg="white")
aeroplane_model_label.pack()
aeroplane_model_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
aeroplane_model_entry.pack()

aeroplane_manufacturer_label = tk.Label(aeroplane_page, text="Manufacturer:", font=("Arial", 12), bg="white")
aeroplane_manufacturer_label.pack()
aeroplane_manufacturer_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
aeroplane_manufacturer_entry.pack()

# Function to handle the Aeroplane page submit button click
def insert_aeroplane():
    callsign = aeroplane_callsign_entry.get()
    airline_id = aeroplane_airline_entry.get()
    model = aeroplane_model_entry.get()
    manufacturer = aeroplane_manufacturer_entry.get()

    if callsign and model:
        query = f"INSERT INTO Aeroplane (Callsign, Airline_ID, Model, Manufacturer) VALUES ('{callsign}', '{airline_id}', '{model}', '{manufacturer}')"
        execute_query(query, "Aeroplane inserted successfully.", "Failed to insert Aeroplane.")
    else:
        messagebox.showwarning("Warning", "Callsign and Model are required fields.")

# Create the Aeroplane page submit button
aeroplane_submit_button = tk.Button(aeroplane_page, text="Submit", font=("Arial", 12), command=insert_aeroplane)
aeroplane_submit_button.pack()

# Create the Aeroplane page back button
def back_to_home():
    show_page(home_page)

aeroplane_back_button = tk.Button(aeroplane_page, text="Back", font=("Arial", 12), command=back_to_home)
aeroplane_back_button.pack()


# Create a frame for the Boarding Pass page
boarding_pass_page = tk.Frame(main_frame, bg="white")
boarding_pass_page.background = background_image_boarding_pass

# Create a frame for the Boarding Pass page
boarding_pass_page = tk.Frame(main_frame, bg="white")
boarding_pass_page.background = background_image_boarding_pass
boarding_pass_page.pack(fill="both", expand=True)

# Create labels and entry fields for the Boarding Pass page
boarding_pass_id_label = tk.Label(boarding_pass_page, text="Pass ID:", font=("Arial", 12), bg="white")
boarding_pass_id_label.pack()
boarding_pass_id_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_pass_id_entry.pack()

boarding_pass_flight_label = tk.Label(boarding_pass_page, text="Flight No.:", font=("Arial", 12), bg="white")
boarding_pass_flight_label.pack()
boarding_pass_flight_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_pass_flight_entry.pack()

boarding_pass_passenger_label = tk.Label(boarding_pass_page, text="Passenger ID:", font=("Arial", 12), bg="white")
boarding_pass_passenger_label.pack()
boarding_pass_passenger_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_pass_passenger_entry.pack()

boarding_pass_ticket_label = tk.Label(boarding_pass_page, text="Ticket ID:", font=("Arial", 12), bg="white")
boarding_pass_ticket_label.pack()
boarding_pass_ticket_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_pass_ticket_entry.pack()

boarding_pass_gate_label = tk.Label(boarding_pass_page, text="Gate:", font=("Arial", 12), bg="white")
boarding_pass_gate_label.pack()
boarding_pass_gate_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_pass_gate_entry.pack()

boarding_pass_checkin_label = tk.Label(boarding_pass_page, text="Check-in:", font=("Arial", 12), bg="white")
boarding_pass_checkin_label.pack()
boarding_pass_checkin_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_pass_checkin_entry.pack()

boarding_pass_boarding_label = tk.Label(boarding_pass_page, text="Boarding:", font=("Arial", 12), bg="white")
boarding_pass_boarding_label.pack()
boarding_pass_boarding_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_pass_boarding_entry.pack()

# Function to handle the Boarding Pass page submit button click
def insert_boarding_pass():
    pass_id = boarding_pass_id_entry.get()
    flight_no = boarding_pass_flight_entry.get()
    passenger_id = boarding_pass_passenger_entry.get()
    ticket_id = boarding_pass_ticket_entry.get()
    gate = boarding_pass_gate_entry.get()
    check_in = boarding_pass_checkin_entry.get()
    boarding = boarding_pass_boarding_entry.get()

    if pass_id and flight_no:
        query = f"INSERT INTO Boarding_Pass (Pass_ID, Flight_NO, Passenger_ID, Ticket_ID, Gate, Check_in, Boarding) " \
                f"VALUES ('{pass_id}', '{flight_no}', '{passenger_id}', '{ticket_id}', '{gate}', '{check_in}', '{boarding}')"
        execute_query(query, "Boarding Pass inserted successfully.", "Failed to insert Boarding Pass.")
    else:
        messagebox.showwarning("Warning", "Pass ID and Flight No. are required fields.")

# Create the Boarding Pass page submit button
boarding_pass_submit_button = tk.Button(boarding_pass_page, text="Submit", font=("Arial", 12), command=insert_boarding_pass)
boarding_pass_submit_button.pack()

# Create the Boarding Pass page back button
boarding_pass_back_button = tk.Button(boarding_pass_page, text="Back", font=("Arial", 12), command=back_to_home)
boarding_pass_back_button.pack()

# Create a frame for the Cabin Crew page
cabin_crew_page = tk.Frame(main_frame, bg="white")
cabin_crew_page.background = background_image_cabin_crew

# Create a frame for the Cabin Crew page
cabin_crew_page = tk.Frame(main_frame, bg="white")
cabin_crew_page.background = background_image_cabin_crew
cabin_crew_page.pack(fill="both", expand=True)

# Create labels and entry fields for the Cabin Crew page
cabin_crew_id_label = tk.Label(cabin_crew_page, text="Crew ID:", font=("Arial", 12), bg="white")
cabin_crew_id_label.pack()
cabin_crew_id_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
cabin_crew_id_entry.pack()

cabin_crew_flight_label = tk.Label(cabin_crew_page, text="Flight No.:", font=("Arial", 12), bg="white")
cabin_crew_flight_label.pack()
cabin_crew_flight_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
cabin_crew_flight_entry.pack()

cabin_crew_first_name_label = tk.Label(cabin_crew_page, text="First Name:", font=("Arial", 12), bg="white")
cabin_crew_first_name_label.pack()
cabin_crew_first_name_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
cabin_crew_first_name_entry.pack()

cabin_crew_last_name_label = tk.Label(cabin_crew_page, text="Last Name:", font=("Arial", 12), bg="white")
cabin_crew_last_name_label.pack()
cabin_crew_last_name_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
cabin_crew_last_name_entry.pack()

cabin_crew_contact_label = tk.Label(cabin_crew_page, text="Contact No.:", font=("Arial", 12), bg="white")
cabin_crew_contact_label.pack()
cabin_crew_contact_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
cabin_crew_contact_entry.pack()

# Function to handle the Cabin Crew page submit button click
def insert_cabin_crew():
    crew_id = cabin_crew_id_entry.get()
    flight_no = cabin_crew_flight_entry.get()
    first_name = cabin_crew_first_name_entry.get()
    last_name = cabin_crew_last_name_entry.get()
    contact_no = cabin_crew_contact_entry.get()

    if crew_id and flight_no and first_name:
        query = f"INSERT INTO Cabin_Crew (Crew_ID, Flight_NO, First_name, Last_name, Contact_NO) " \
                f"VALUES ('{crew_id}', '{flight_no}', '{first_name}', '{last_name}', '{contact_no}')"
        execute_query(query, "Cabin Crew inserted successfully.", "Failed to insert Cabin Crew.")
    else:
        messagebox.showwarning("Warning", "Crew ID, Flight No., and First Name are required fields.")

# Create the Cabin Crew page submit button
cabin_crew_submit_button = tk.Button(cabin_crew_page, text="Submit", font=("Arial", 12), command=insert_cabin_crew)
cabin_crew_submit_button.pack()

# Create the Cabin Crew page back button
cabin_crew_back_button = tk.Button(cabin_crew_page, text="Back", font=("Arial", 12), command=back_to_home)
cabin_crew_back_button.pack()


# Add the pages to the dictionary
pages["home_page"] = home_page
pages["aeroplane_page"] = aeroplane_page
pages["boarding_pass_page"] = boarding_pass_page
pages["cabin_crew_page"] = cabin_crew_page

# Show the Home page initially
show_page(home_page)

# Connect to MySQL database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="bumblebee291",  # Replace with your MySQL password
        database="airline_management_system"  # Replace with your MySQL database name
    )
    cursor = db.cursor()
except mysql.connector.Error as error:
    messagebox.showerror("Error", f"Failed to connect to MySQL database.\nError Message: {error}")
    window.destroy()

# Start the Tkinter event loop
window.mainloop()
