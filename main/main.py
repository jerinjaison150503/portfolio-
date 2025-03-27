from flask import Flask, render_template, request, redirect, flash, send_file
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = "temporary_secret_key"

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "frommyportfolio015@gmail.com"
app.config['MAIL_PASSWORD'] = "ybud mpzm syvw dgcu"
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_me', methods=['POST'])
def contact_me():
    """Handle contact form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not all([name, email, subject, message]):
            flash("All fields are required!", "danger")
            return redirect('/')

        # Create email message
        msg = Message(subject=f"New Contact: {subject}",
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=["jerinforwork@gmail.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            app.logger.error(f"Failed to send email: {e}")
            flash("Failed to send message. Please try again later.", "danger")

    return redirect('/')

@app.route('/download-pdf')
def download_pdf():
    """Serve an existing PDF file for download."""
    pdf_path = os.path.join(os.getcwd(), "static", "files", "resume.pdf")  
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
