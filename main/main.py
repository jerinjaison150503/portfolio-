from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "temporary_secret_key"

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "frommyportfolio015@gmail.com"  
app.config['MAIL_PASSWORD'] = "ybud mpzm syvw dgcu"          
app.config['MAIL_DEFAULT_SENDER'] = "frommyportfolio015@gmail.com"

mail = Mail(app)

@app.route('/')
def index():
    """Render the homepage with the contact form."""
    return render_template('index.html')

@app.route('/contact_me', methods=['POST'])
def contact_me():
    """Handle contact form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not name or not email or not subject or not message:
            flash("All fields are required!", "danger")
            return redirect(url_for('index'))

        # Create email message
        msg = Message(subject=subject, recipients=["jerinforwork@gmail.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"

        try:
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
