from email import message
from flask import render_template, request # type: ignore
from . import main

# Route for initial page
@main.route('/')
def index():
    return render_template('index.html')

#Route for "About" page
@main.route('/about')
def about():
    return render_template('about.html')

#Route for process a form
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        #Process form data
        name = request.form['name']
        message = request.form['message']
        # Here you can send a e-mail or save the message in a database
        return render_template('thank_you.html',name=name)
    return render_template('contact.html')