# python app.py
import os
import pandas as pd
from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
app.secret_key = "keep-it-secret"  # Needed for flash messages

ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    summary_html = None
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Read the CSV and create a summary
            try:
                df = pd.read_csv(filepath)
                summary = df.describe(include='all').T  # Transpose for clarity
                summary_html = summary.to_html(classes="table table-striped", border=0)
                flash('File successfully uploaded and processed!')
            except Exception as e:
                flash(f'Failed to process file: {e}')
        else:
            flash('Invalid file type. Only CSV allowed.')
            return redirect(request.url)
    return render_template('upload.html', summary_html=summary_html)


if __name__ == '__main__':
    app.run(debug=True)
