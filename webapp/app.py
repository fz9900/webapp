from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Replace this with actual user authentication logic
def is_authenticated(username, password):
    return username == 'admin' and password == 'admin'

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_authenticated(username, password):
            return redirect(url_for('dashboard', username=username))
        else:
            error = "Invalid credentials. Please try again."
            return render_template('login.html', error=error)

    return render_template('login.html', error=None)

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('home.html', username=username)

@app.route('/logout')
def logout():
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
