import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for,send_file)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/image.jpg')
def serve_image():
    referer = request.headers.get('Referer')
    print(f"Referer: {referer}")
    if referer:
        if 'https://login.microsoftonline.com/' in referer:
            
            image_path = 'img/OK.jpg'
        else:
            image_path = 'img/NG.jpg'
    else:
        image_path =  image_path = 'img/NG.jpg'

    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return "Image not found", 404


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5050)
