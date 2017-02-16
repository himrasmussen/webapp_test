import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import hwinfo_analyze as hwinfo

UPLOAD_FOLDER = 'uploads'
ANALYSIS_FOLDER = 'analysis'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ANALYSIS_FOLDER'] = ANALYSIS_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = str(len(os.listdir(app.config['UPLOAD_FOLDER']))) + '.csv'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #The script runs here
            file_number = filename.split('.')[0]
            with open(os.path.join(app.config['ANALYSIS_FOLDER'], file_number + ".html"), 'w') as f:
                message = hwinfo.main(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                f.write("""
                    <!doctype html>
                    <title>Anylisis #{}</title>
                    <h1>Da results</h1>
                    """.format(file_number))
                f.write("<p>")
                for line in message.split("\n"):
                    f.write("{}<br>".format(line))
                f.write("</p>")


            return redirect(url_for('show_analysis', file_number=file_number))
            #return redirect(url_for('upload_file',
                                    #filename=filename))
            #TODO: Analyze log when uploaded.

    return '''
    <!doctype html>
    <title>HW-info analyzer, the free hwinfo analyzing helper.</title>
    <h1>Upload your hwinfo log.</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/analysis/<file_number>')
def show_analysis(file_number):
    with open(os.path.join(app.config["ANALYSIS_FOLDER"], file_number + ".html")) as f:
        return ''.join(f.readlines())


if __name__ == '__main__':
    app.debug = True
    app.run()
