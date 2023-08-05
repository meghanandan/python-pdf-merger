from flask import Flask, request, render_template, jsonify, send_file, make_response
import PyPDF2
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge_pdfs', methods=['POST'])
def merge_pdfs():
    pdf1 = request.files['pdf1']
    pdf2 = request.files['pdf2']

    pdf_merger = PyPDF2.PdfMerger()

    pdf_merger.append(pdf1)
    pdf_merger.append(pdf2)

    merged_pdf = 'merged.pdf'
    with open(merged_pdf, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

    response = make_response(jsonify({"status": "success", "url": "/download"}))
    response.headers["Content-Disposition"] = "attachment; filename=merged.pdf"
    return response

@app.route('/download')
def download():
    merged_pdf = 'merged.pdf'
    return send_file(merged_pdf, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
