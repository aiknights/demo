from flask import Flask, render_template, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
 
app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

@app.route('/articles')
def api_articles():
	return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
	return 'You are reading ' + articleid

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'dataset.csv' in request.files:
	file = request.files['dataset.csv']
        file.save(file.filename)
	flash("dataset saved.")
	return redirect(url_for('show', id=rec.id))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host = '192.187.114.202')

