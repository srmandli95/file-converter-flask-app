# PDF to Word / Word to PDF Converter

This is a Flask-based web application that allows users to upload a PDF or Word file and convert it between the two formats:
- **PDF to Word** (using `pdf2docx`)
- **Word to PDF** (using `docx2pdf`)

## Features:

- Upload a PDF and download it as a Word file.
- Upload a Word document and download it as a PDF file.
- Simple and easy-to-use web interface built using Flask and Bootstrap.

## Requirements

- Python 3.11
- Flask
- pdf2docx
- docx2pdf
- Pipenv (for managing dependencies)

## Installation

To run this project on your local machine, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies:
This project uses Pipenv for dependency management. If Pipenv is not already installed, you can install it and then set up the project dependencies by running the following c

```bash
pip install pipenv
pipenv install
```
### 3. Run the Flask App:
Once the dependencies are installed, activate the virtual environment and run the Flask application:

```bash
pipenv shell
python app.py
```
### 4.Directory Structure:
```bash
.
├── app.py              # Flask application
├── Pipfile             # Pipenv dependencies file
├── Pipfile.lock        # Pipenv lock file
├── templates/          # Contains HTML files for the UI
│   └── index.html      # Main HTML template for file upload
├── uploads/            # Folder for storing uploaded files (auto-created)
├── outputs/            # Folder for storing converted files (auto-created)
└── README.md           # Instructions for the project
```

### 5.Conversion Logic:
- PDF to Word: Converts a .pdf file to a .docx Word document using pdf2docx.
- Word to PDF: Converts a .docx file to a .pdf document using docx2pdf.

### 6.How to Use:
- Open your browser and go to http://127.0.0.1:5000/.
- Upload either a PDF or a Word document.
- Select the conversion type (PDF to Word or Word to PDF) from the dropdown.
- Click Upload and Convert.
- Once the file is converted, it will be automatically downloaded to your device.
