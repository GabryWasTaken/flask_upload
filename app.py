from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'img'
app.config['UPLOADED_PHOTOS_ALLOW'] = set(['png', 'jpg', 'jpeg', 'gif']) # allow file type
app.config['UPLOADD_PHOTOS_DENY'] = set(['txt', 'pdf', 'doc', 'docx']) # deny file type

configure_uploads(app, (photos))

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'up_photo' in request.files:
        try:
            filename = photos.save(request.files['up_photo'])
            return render_template('confirm.html', filename=filename)
        except UploadNotAllowed:
            return render_template('deny.html')
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)