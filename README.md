# NLP Resume Parser

A lightweight **resume parser using NLP-friendly PDF/Docx formats** that extracts structured data from resumes, designed to run locally with Flask and display results directly in the browser.

---

## Features

✅ Upload resumes in **NLP-friendly (editable text) PDF/Docx format**  
✅ Parses and extracts structured information from resumes  
✅ Displays extracted data on the same webpage for quick review  
✅ Shows full extracted text via a button for manual verification  
✅ Separate `script.js` for clean frontend integration

---

## Limitations

🚫 **Name extraction does not work reliably** due to keyword limitations.  
🚫 Requires resumes in **editable NLP-friendly format** (not scanned images).  
✅ You can modify/add keywords for better extraction in future enhancements.

---

## Setup

### 1️⃣ Clone the repository

\`\`\`bash
git clone <your-repo-url>
cd <repo-folder>
\`\`\`

### 2️⃣ Install dependencies

#### Using \`requirements.txt\`:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

#### Or individually:

\`\`\`bash
pip install flask,
pip install flask-cors,
pip install pdfplumber,
pip install python-docx,
\`\`\`

---

## VS Code Live Server Configuration (Optional)

If using **Live Server extension in VS Code** for frontend:

- Install **Live Server** extension.
- Uncheck:
  - \`Live Server - Settings: Wait\`
  - \`Live Server - Settings: Full Reload\`
  - \`Live Server - Settings: Auto Save\`
- Set:
  - \`liveServer.settings.wait\` to \`999999\`

This prevents automatic reloads while parsing resumes.

---

## Running the App

### Backend:
\`\`\`bash
python app.py
\`\`\`

Check your terminal for the **debug PIN and access URL**.

### Frontend:

- Open \`index.html\` with Live Server or go to:
  \`\`\`
  http://127.0.0.1:5000
  \`\`\`
- Upload your resume (PDF/Docx).
- View parsed output on the same page.

---

## Contributing

✨ Feel free to fork and contribute:
- Add better keyword matching
- Improve name extraction
- Integrate advanced NLP models for deeper parsing


## Author

**Harsh Pawar**
