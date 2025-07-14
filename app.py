from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pdfplumber
import docx
import re
import os

app = Flask(__name__)
CORS(app)



def extract_text_from_pdf(file_path):
    text = ''
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_info(text):
    emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)))
    phones = list(set(re.findall(r"\+?\d[\d\s\-]{7,}\d", text)))
    urls = list(set(re.findall(r"https?://\S+|www\.\S+", text)))

    skill_keywords = ["python", "flask", "machine learning", "data analysis", "java", "node.js", "react", "sql", "mongodb"]
    skills = [skill.title() for skill in skill_keywords if skill.lower() in text.lower()]

    locations_list = ["Pune", "Mumbai", "Bangalore", "Delhi", "India", "New York", "California", "London", "Germany"]
    locations = [loc for loc in locations_list if loc.lower() in text.lower()]

    qualifications_list = ["BSc", "MSc", "B.E", "B.Tech", "M.Tech", "PhD", "Bachelor", "Master", "Doctorate"]
    qualifications = [qual for qual in qualifications_list if qual.lower() in text.lower()]

    exp_match = re.search(r"(\d+)\+?\s*(years|yrs)\s*(of)?\s*experience", text.lower())
    years_of_experience = exp_match.group(1) if exp_match else "Not Found"

    return {
        "emails": emails if emails else ["Not Found"],
        "phones": phones if phones else ["Not Found"],
        "urls": urls if urls else ["Not Found"],
        "skills": skills if skills else ["Not Found"],
        "locations": locations if locations else ["Not Found"],
        "qualifications": qualifications if qualifications else ["Not Found"],
        "years_of_experience": years_of_experience,
        "full_text": text[:3000] + "..." if len(text) > 3000 else text  
    }



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/parse_resume", methods=["POST"])
def parse_resume():
    file = request.files.get("resume")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = f"temp_{file.filename}"
    file.save(file_path)

    try:
        if file.filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.filename.lower().endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            os.remove(file_path)
            return jsonify({"error": "Unsupported file type"}), 400

        extracted = extract_info(text)

        parsed_data = {
            "name": "Name Extraction TBD",
            "emails": extracted["emails"],
            "phones": extracted["phones"],
            "urls": extracted["urls"],
            "locations": extracted["locations"],
            "skills": extracted["skills"],
            "qualifications": extracted["qualifications"],
            "years_of_experience": extracted["years_of_experience"],
            "full_text": extracted["full_text"]
        }

        os.remove(file_path)
        return jsonify(parsed_data)
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
