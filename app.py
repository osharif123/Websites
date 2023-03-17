from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

events = []
registrations = []

@app.route('/')
def home():
    return render_template('index.html', events=events, registrations=registrations)

@app.route('/create-event', methods=['POST'])
def create_event():
    password = request.form['password']
    if password == "NiceAbuu":
        location = request.form['location']
        time = request.form['time']
        day = request.form['day']
        date = request.form['date']
        event = {"location": location, "time": time, "day": day, "date": date}
        events.append(event)
    return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    if len(registrations) < 14:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        timestamp = datetime.now().strftime('%I:%M %p')
        order = len(registrations) + 1
        registration = {"first_name": first_name, "last_name": last_name, "order": order, "timestamp": timestamp}
        registrations.append(registration)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
