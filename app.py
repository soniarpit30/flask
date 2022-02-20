from flask import Flask, render_template, request

#initialize the app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('form.html')

@app.route('/contacts')
def contact():
    return 'Contact page'

@app.route('/submit', methods = ['POST'])
def form_data():
    fname = request.form.get('fname')
    sname = request.form.get('sname')
    phone = request.form.get('phone number')
    email = request.form.get('email')

    print(fname, sname, phone, email)

    return render_template('data.html', data = (fname, sname, phone, email))

if __name__ == '__main__':
    app.run(debug = True)