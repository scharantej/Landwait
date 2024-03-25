
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        # Save email to database or email list
        # Send confirmation message to user
        return redirect(url_for('success'))
    return render_template('landing.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()
