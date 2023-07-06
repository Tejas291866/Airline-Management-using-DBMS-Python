import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Create a MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bumblebee291",
    database="airline_management_system"
)

# Create a cursor object
cursor = connection.cursor()

# Function to execute SQL queries
def execute_query(query, success_message, error_message):
    try:
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", success_message)
    except Exception as e:
        connection.rollback()
        messagebox.showerror("Error", f"{error_message}\nError: {str(e)}")

# Function to navigate back to the Home page
def back_to_home():
    home_page.tkraise()

# Create the main window
root = tk.Tk()
root.title("Airline Management System")
root.geometry("800x600")
root.resizable(False, False)

# Create a frame for the main content
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Create a dictionary to store background images for each page
background_images = {
    "Home": "home.jpeg",
    "Aeroplane": "download.jpeg",
    "Boarding Pass": "boarding-pass-isolated-background_53876-147830.avif",
    "Cabin Crew": "cabin_crew_training_2.jpg",
}

# Function to switch between pages
def show_page(page):
    page.tkraise()

# Function to exit the application
def exit_app():
    root.destroy()

# Create the Home page
home_page = tk.Frame(main_frame, bg="white")
home_page.background = tk.PhotoImage(file="download (2).jpeg")
home_page.pack(fill="both", expand=True)

# Create buttons to navigate to different pages
aeroplane_button = tk.Button(home_page, text="Aeroplane", font=("Arial", 12), command=lambda: show_page(aeroplane_page))
aeroplane_button.pack()

boarding_pass_button = tk.Button(home_page, text="Boarding Pass", font=("Arial", 12), command=lambda: show_page(boarding_pass_page))
boarding_pass_button.pack()

cabin_crew_button = tk.Button(home_page, text="Cabin Crew", font=("Arial", 12), command=lambda: show_page(cabin_crew_page))
cabin_crew_button.pack()

# Create the Aeroplane page
aeroplane_page = tk.Frame(main_frame, bg="white")
aeroplane_page.background = tk.PhotoImage(file="download (2).jpeg")
aeroplane_page.pack(fill="both", expand=True)

# Create labels and entry fields for the Aeroplane page
callsign_label = tk.Label(aeroplane_page, text="Callsign:", font=("Arial", 12), bg="white")
callsign_label.pack()
callsign_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
callsign_entry.pack()

airline_id_label = tk.Label(aeroplane_page, text="Airline ID:", font=("Arial", 12), bg="white")
airline_id_label.pack()
airline_id_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
airline_id_entry.pack()

model_label = tk.Label(aeroplane_page, text="Model:", font=("Arial", 12), bg="white")
model_label.pack()
model_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
model_entry.pack()

manufacturer_label = tk.Label(aeroplane_page, text="Manufacturer:", font=("Arial", 12), bg="white")
manufacturer_label.pack()
manufacturer_entry = tk.Entry(aeroplane_page, font=("Arial", 12))
manufacturer_entry.pack()

# Create buttons for Aeroplane page
aeroplane_insert_button = tk.Button(aeroplane_page, text="Insert", font=("Arial", 12), command=lambda: execute_query(f"INSERT INTO Aeroplane (Callsign, Airline_ID, Model, Manufacturer) VALUES ('{callsign_entry.get()}', {airline_id_entry.get()}, '{model_entry.get()}', '{manufacturer_entry.get()}')", "Aeroplane inserted successfully!", "Error occurred while inserting Aeroplane"))
aeroplane_insert_button.pack()

aeroplane_back_button = tk.Button(aeroplane_page, text="Back", font=("Arial", 12), command=back_to_home)
aeroplane_back_button.pack()

# Create the Boarding Pass page
boarding_pass_page = tk.Frame(main_frame, bg="white")
boarding_pass_page.background = tk.PhotoImage(file="boarding-pass-isolated-background_53876-147830.avif")
boarding_pass_page.pack(fill="both", expand=True)

# Create labels and entry fields for the Boarding Pass page
pass_id_label = tk.Label(boarding_pass_page, text="Pass ID:", font=("Arial", 12), bg="white")
pass_id_label.pack()
pass_id_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
pass_id_entry.pack()

flight_no_label = tk.Label(boarding_pass_page, text="Flight No:", font=("Arial", 12), bg="white")
flight_no_label.pack()
flight_no_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
flight_no_entry.pack()

passenger_id_label = tk.Label(boarding_pass_page, text="Passenger ID:", font=("Arial", 12), bg="white")
passenger_id_label.pack()
passenger_id_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
passenger_id_entry.pack()

ticket_id_label = tk.Label(boarding_pass_page, text="Ticket ID:", font=("Arial", 12), bg="white")
ticket_id_label.pack()
ticket_id_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
ticket_id_entry.pack()

gate_label = tk.Label(boarding_pass_page, text="Gate:", font=("Arial", 12), bg="white")
gate_label.pack()
gate_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
gate_entry.pack()

check_in_label = tk.Label(boarding_pass_page, text="Check-in:", font=("Arial", 12), bg="white")
check_in_label.pack()
check_in_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
check_in_entry.pack()

boarding_label = tk.Label(boarding_pass_page, text="Boarding:", font=("Arial", 12), bg="white")
boarding_label.pack()
boarding_entry = tk.Entry(boarding_pass_page, font=("Arial", 12))
boarding_entry.pack()

# Create buttons for Boarding Pass page
boarding_pass_insert_button = tk.Button(boarding_pass_page, text="Insert", font=("Arial", 12), command=lambda: execute_query(f"INSERT INTO Boarding_Pass (Pass_ID, Flight_NO, Passenger_ID, Ticket_ID, Gate, Check_in, Boarding) VALUES ({pass_id_entry.get()}, {flight_no_entry.get()}, {passenger_id_entry.get()}, {ticket_id_entry.get()}, '{gate_entry.get()}', '{check_in_entry.get()}', '{boarding_entry.get()}')", "Boarding Pass inserted successfully!", "Error occurred while inserting Boarding Pass"))
boarding_pass_insert_button.pack()

boarding_pass_back_button = tk.Button(boarding_pass_page, text="Back", font=("Arial", 12), command=back_to_home)
boarding_pass_back_button.pack()

# Create the Cabin Crew page
cabin_crew_page = tk.Frame(main_frame, bg="white")
cabin_crew_page.background = tk.PhotoImage(file="cabin_crew_training_2.jpg")
cabin_crew_page.pack(fill="both", expand=True)

# Create labels and entry fields for the Cabin Crew page
crew_id_label = tk.Label(cabin_crew_page, text="Crew ID:", font=("Arial", 12), bg="white")
crew_id_label.pack()
crew_id_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
crew_id_entry.pack()

crew_name_label = tk.Label(cabin_crew_page, text="Crew Name:", font=("Arial", 12), bg="white")
crew_name_label.pack()
crew_name_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
crew_name_entry.pack()

designation_label = tk.Label(cabin_crew_page, text="Designation:", font=("Arial", 12), bg="white")
designation_label.pack()
designation_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
designation_entry.pack()

contact_no_label = tk.Label(cabin_crew_page, text="Contact No:", font=("Arial", 12), bg="white")
contact_no_label.pack()
contact_no_entry = tk.Entry(cabin_crew_page, font=("Arial", 12))
contact_no_entry.pack()

# Create buttons for Cabin Crew page
cabin_crew_insert_button = tk.Button(cabin_crew_page, text="Insert", font=("Arial", 12), command=lambda: execute_query(f"INSERT INTO Cabin_Crew (Crew_ID, Crew_Name, Designation, Contact_No) VALUES ({crew_id_entry.get()}, '{crew_name_entry.get()}', '{designation_entry.get()}', '{contact_no_entry.get()}')", "Cabin Crew inserted successfully!", "Error occurred while inserting Cabin Crew"))
cabin_crew_insert_button.pack()

cabin_crew_back_button = tk.Button(cabin_crew_page, text="Back", font=("Arial", 12), command=back_to_home)
cabin_crew_back_button.pack()

# Create the Exit button
exit_button = tk.Button(main_frame, text="Exit", font=("Arial", 12), command=exit_app)
exit_button.pack()

# Set the Home page as the initially displayed page
show_page(home_page)

# Start the Tkinter event loop
root.mainloop()

# Close the database connection
connection.close()
