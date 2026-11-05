from flask import Flask, request, redirect, send_from_directory
import mysql.connector
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

def get_db_connection():

    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST", "localhost"),
        port=int(os.environ.get("MYSQLPORT", 3306)),
        user=os.environ.get("MYSQLUSER", "root"),
        password=os.environ.get("MYSQLPASSWORD", "4444"),
        database=os.environ.get("MYSQLDATABASE", "college_db")
    )

courses = {
    "bsc-it": "B.Sc Information Technology",
    "bca": "Bachelor of Computer Applications",
    "bcom": "Bachelor of Commerce",
    "bms": "Bachelor of Management Studies"
}

@app.route("/")
def home():

    return send_from_directory(TEMPLATE_DIR, "index.html")

@app.route("/about")
def about():

    return send_from_directory(TEMPLATE_DIR, "about.html")

@app.route("/courses")
def course_list():

    return send_from_directory(TEMPLATE_DIR, "courses.html")

@app.route("/course/<slug>")
def course_details(slug):

    if slug not in courses:
        return "Course Not Found", 404

    return send_from_directory(
        TEMPLATE_DIR,
        "course_details.html"
    )

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not email or not phone or not course:
            return "Please fill all fields", 400

        if not phone.isdigit() or len(phone) != 10:
            return "Enter a valid 10-digit phone number", 400

        valid_courses = [
            "B.Sc Information Technology",
            "BCA",
            "B.Com",
            "BMS"
        ]

        if course not in valid_courses:
            return "Invalid course selected", 400

        conn = None
        cursor = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO students
                (name, email, phone, course)
                VALUES (%s, %s, %s, %s)
            """

            values = (name, email, phone, course)

            cursor.execute(query, values)

            conn.commit()

            return redirect("/register?success=1")

        except mysql.connector.Error as error:

            print("Database Error:", error)

            if conn:
                conn.rollback()

            return "Registration failed. Please try again.", 500

        finally:

            if cursor:
                cursor.close()

            if conn and conn.is_connected():
                conn.close()

    return send_from_directory(TEMPLATE_DIR, "register.html")

@app.route("/contact")
def contact():

    return send_from_directory(TEMPLATE_DIR, "contact.html")

if __name__ == "__main__":

    app.run(debug=True)