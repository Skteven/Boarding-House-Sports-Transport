from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('sports_fixtures.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/transport_form', methods=['POST', 'GET'])
def add_card():
    if request.method == 'POST':
        Name = request.form['Full Name']
        Location = request.form['Location']
        Drop_off = request.form['Drop off Time']
        Pick_up = request.form['Pick up Time']
        conn = get_db_connection()
        conn.execute('INSERT INTO sports_fixtures (Name, Location, Drop_off, Pick_up) VALUES (?, ?, ?, ?)',
                    (Name, Location, Drop_off, Pick_up))
        conn.commit()
        
        return redirect(url_for('index'))
    
    return render_template('transport_form.html')

app.run(debug=True)
