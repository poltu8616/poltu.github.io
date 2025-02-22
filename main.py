
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import datetime
import csv
import os

app = Flask(__name__)

@app.route('/templates/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates', filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        datetime_str = request.form['datetime']
        purpose = request.form['purpose']
        
        try:
            # Create CSV file if it doesn't exist
            if not os.path.exists('booking.csv'):
                with open('booking.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Timestamp', 'Name', 'Email', 'Appointment Time', 'Purpose'])
            
            # Check if timeslot is already taken
            is_slot_available = True
            with open('booking.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Appointment Time'] == datetime_str:
                        is_slot_available = False
                        break
            
            if not is_slot_available:
                return render_template('booking.html', error="This time slot is already booked. Please select a different time.")
            
            # Append the new booking
            with open('booking.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    name,
                    email,
                    datetime_str,
                    purpose
                ])
            
            return render_template('confirmation.html')
        except Exception as e:
            return render_template('booking.html', error=f"An error occurred: {str(e)}")
            
    return redirect(url_for('booking'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
