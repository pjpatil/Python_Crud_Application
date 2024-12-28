from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='4433',
    database='itwork',
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()


@app.route('/')
def index():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('index.html', employees=employees)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)",
                       (name, age, department))
        mydb.commit()

        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
    employee = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        cursor.execute("UPDATE employees SET name = %s, age = %s, department = %s WHERE id = %s",
                       (name, age, department, id))
        mydb.commit()

        return redirect(url_for('index'))

    return render_template('update.html', employee=employee)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    mydb.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
