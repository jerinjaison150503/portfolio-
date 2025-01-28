from flask import Flask, render_template, request, redirect, flash, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_mail import Mail,Message


app = Flask(__name__)
app.secret_key = "temporary_secret_key"  

# @app.route("/", methods=["GET", "POST"])
# def home():
#     """Render the home page and handle contact form submissions."""
#     if request.method == "POST":
        
#         name = request.form.get("name")
#         email = request.form.get("email")
#         message = request.form.get("message")

        
#         if not name or not email or not message:
#             flash("All fields are required!", "danger")
#             return redirect(url_for("home"))

#         # Email credentials 
#         sender_email = "frommyportfolio015@gmail.com"
#         sender_password = "Frommyportfolio@#015"
#         recipient_email = "jerinforwork@gmail.com"

#         # sending the email
#         try:
#             # Create email content
#             msg = MIMEMultipart()
#             msg["From"] = sender_email
#             msg["To"] = recipient_email
#             msg["Subject"] = f"New Contact Form Submission from {name}"
#             body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
#             msg.attach(MIMEText(body, "plain"))

#             # Set up the SMTP connection
#             with smtplib.SMTP("smtp.gmail.com", 587) as server:
#                 server.starttls()
#                 server.login(sender_email, sender_password)
#                 server.sendmail(sender_email, recipient_email, msg.as_string())

#             flash("Your message has been sent successfully!", "success")
#         except smtplib.SMTPAuthenticationError:
#             flash("Failed to send email: Invalid email credentials.", "danger")
#         except Exception as e:
#             flash(f"An error occurred: {str(e)}", "danger")

#         return redirect(url_for("home"))
    
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)



mail=Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jerinforwork@gmail.com' # Replace with your email
app.config['MAIL_PASSWORD'] = '' # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = ('Jerin', 'jerinforwork@gmail.com') # Replace with your default sender email
# app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail=Mail(app)

@app.route('/')
def index():
    # flash("!! Messege sent successfull I will contact you as soon as possible !!","success")

    return render_template('index.html')

# if _name_ == '_main_':
# app.run(port=5001,debug=True)

# Configuration settings for Flask-Mail


@app.route('/contact_me', methods=['POST'])
def contact_me1():
    print("Contactme")
    if request.method=='POST':
        print(request)
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = Message(subject, recipients=['jerinforwork@gmail.com'],sender='Frommyportfolio@#015') # Replace with recipient email
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"
        print(name,email,subject,message)
        mail.send(msg)
        flash("!! Messege sent successfull I will contact you as soon as possible !!","success")


    return redirect(url_for('index'))
if _name_ == '_main_':
    app.run(debug=True)