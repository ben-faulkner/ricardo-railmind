
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Simulated Q&A database based on sample data
qa_data = {
    "how do i isolate the battery on a class 220": "To isolate the battery on a Class 220 Diesel Multiple Unit:\n1. Locate the battery isolation switch inside the equipment cabinet.\n2. Turn the switch to the OFF position and secure it with a padlock.\n3. Verify isolation by checking voltage at terminals.",
    "what does fault code e514 mean": "Fault Code E514 indicates an Inverter Cooling Fan Failure. Steps:\n- Check the cooling fan fuse (FAN-F1).\n- Inspect the fan for debris or mechanical obstruction.\n- Replace the fan if it is not operational.",
    "what torque should i use for axle bolts": "Axle bolt torque for Class 220 units should be 800 Nm.",
    "brake system inspection steps": "Brake System Inspection:\n- Inspect brake calipers for wear and cracks.\n- Measure brake pad thickness. Minimum allowed: 15mm.\n- Check for any air leaks in pneumatic lines."
}

html_template = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>RailMind Assistant</title>
</head>
<body>
    <h1>RailMind Assistant</h1>
    <form method=\"post\">
        <label for=\"question\">Ask a question:</label><br>
        <input type=\"text\" id=\"question\" name=\"question\" style=\"width: 300px;\"><br><br>
        <input type=\"submit\" value=\"Ask\">
    </form>
    {% if answer %}
    <h3>Answer:</h3>
    <p>{{ answer }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        question = request.form.get("question", "").lower()
        answer = qa_data.get(question, "I'm sorry, I don't have information on that yet.")
    return render_template_string(html_template, answer=answer)

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question", "").lower()
    response = qa_data.get(question, "I'm sorry, I don't have information on that yet.")
    return jsonify({"answer": response})

if __name__ == "__main__":
    # Disable debug mode to avoid _multiprocessing error in restricted environments
    app.run(debug=False)
