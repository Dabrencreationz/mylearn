from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '727dcff49737090d34da619ec013fbe5'
bootstrap = Bootstrap(app)

@app.route('/')
def landing():
    return render_template('login.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/learnerpage')
def learnerpage():
  return render_template('learnerpage.html')

@app.route('/instructorpage')
def instructorpage():
  return render_template('instructorpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')

        # Perform authentication logic (e.g., check username and password against a database)
        if username == 'admin' and password == 'password':
            # Successful login, redirect to home page
            return redirect('/home')
        else:
            # Failed login, render login page with error message
            error_message = 'Invalid username or password.'
            return render_template('login.html', error_message=error_message)    
    # GET request, render the login page
    return render_template('login.html')

@app.route('/logout')
def logout():
  return render_template('login.html')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")