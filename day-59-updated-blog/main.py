from flask import Flask, render_template, request
import requests
import smtplib


npoint_endpoint = "https://api.npoint.io/41aeb34357eb2fbdde24"
response = requests.get(npoint_endpoint)
response.raise_for_status()
json_data = response.json()
SMTP_SERVER = "smtp-mail.outlook.com"
FROM_EMAIL = "xxxxxxxxxxxxxxxxxxxxxxxx"
PASSWORD = "xxxxxxxxxxxxxxxxxxxxx"

app = Flask(__name__)

def send_email(sender, email_addr, phone_no, text):
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs="jonathan_garvin@hotmail.com",
                            msg=f"Subject:New message received from {sender}\n\n\n"
                                f"Contact details:\n{email_addr}\n{phone_no}\n\n{text}"
                            )

@app.route("/")
def home():
    return render_template("index.html", all_posts=json_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:ref>")
def post(ref):
    return render_template("post.html", all_posts=json_data, post_ref=ref)

@app.route("/contact", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone, message)
        return render_template("contact.html", message_sent=True)
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)