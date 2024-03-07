from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Function to find matches and mismatches
def find_matches_and_mismatches(test_string, regex_pattern):
    # Find matches
    matches = re.findall(regex_pattern, test_string)

    # Find mismatches
    mismatches = re.sub(regex_pattern, "", test_string)

    return matches, mismatches

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")
def display_app():
    return render_template("app.html")

@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        # Process the regex pattern matching here
        # For demonstration purposes, let's assume some dummy matches
        matches, mismatches = find_matches_and_mismatches(test_string, regex_pattern)
        return render_template("results.html", matches=matches, mismatches=mismatches)
    else:
        return redirect(url_for("index"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Process the signup form data here
        # After processing, redirect to the main app page
        return redirect(url_for("app"))
    else:
        return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
