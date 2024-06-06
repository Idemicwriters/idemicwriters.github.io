from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Email configuration
        sender_email = 'your_email@gmai.com'
        receiver_email = 'kiamba2munyao@gmail.com'
        password = 'your_email_password'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f'Message from {name} via Idemic Writers website'

        body = f"Name: {name}\nEmail: {email}\n\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            return 'Thank you! Your message has been sent.'
        except Exception as e:
            return f'Oops! Something went wrong. Please try again later. Error: {e}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
