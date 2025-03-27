from flask import Flask, request, render_template
import os

from werkzeug.utils import secure_filename

import analyzer_module

app = Flask(__name__)

# Configure Upload Folder
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        if "resumeFile" not in request.files:
            return "No file part"

        file = request.files["resumeFile"]
        job_description = request.form.get("jobDescription", "").strip()

        if file.filename == "":
            return "No selected file"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Analyze Resume
            analyzer = analyzer_module.ResumeAnalyzer()
            results = analyzer.analyze_resume(filepath, job_description)  # Call your analysis function

            return render_template("analyzer.html", results=results)

    return render_template("analyzer.html", results=None)


if __name__ == "__main__":
    app.run(debug=True)
