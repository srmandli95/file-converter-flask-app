import os
from flask import Flask, render_template, request, send_file, redirect, url_for
from pdf2docx import Converter
from werkzeug.utils import secure_filename
from docx2pdf import convert as docx_to_pdf

app = Flask(__name__)

# Set upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'outputs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure the folders exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Check if the uploaded file is valid for the selected conversion
def allowed_file(filename, conversion_type):
    if conversion_type == 'pdf_to_word':
        return filename.lower().endswith('.pdf')
    elif conversion_type == 'word_to_pdf':
        return filename.lower().endswith('.docx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    conversion_type = request.form['conversion_type']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename, conversion_type):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        if conversion_type == 'pdf_to_word':
            word_filename = filename.rsplit('.', 1)[0] + '.docx'
            word_path = os.path.join(app.config['OUTPUT_FOLDER'], word_filename)

            # Convert PDF to Word
            cv = Converter(file_path)
            cv.convert(word_path)
            cv.close()

            return redirect(url_for('download_file', filename=word_filename))

        elif conversion_type == 'word_to_pdf':
            pdf_filename = filename.rsplit('.', 1)[0] + '.pdf'
            pdf_path = os.path.join(app.config['OUTPUT_FOLDER'], pdf_filename)

            # Convert Word to PDF using docx2pdf
            docx_to_pdf(file_path, pdf_path)

            return redirect(url_for('download_file', filename=pdf_filename))

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
