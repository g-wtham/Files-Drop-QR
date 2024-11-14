import base64
from flask import Flask, redirect, request, send_file, render_template_string, url_for
from pyqrcode import QRCode
import socket
import os
from io import BytesIO

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads' # Create upload folder to store all the files while sending
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) # Create a folder if it doesn't exists in project directory called 'uploads'

def get_ip():
    try:
        ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Using ipv4 address and UDP socket
        ip.connect(('8.8.8.8', 80)) #connecting to google dns servers
        return ip.getsockname()[0]  #returning the ip address when trying to connect
    except:
        return '127.0.0.1'

IP_address = get_ip() 
local_ip_url = f'http://{IP_address}:5000'

def qr_generation(local_ip_url):
    url = QRCode(local_ip_url)
    buffer = BytesIO() 
    url.png(buffer, scale=5) #store as png in a buffer (in-memory, not in a disk)
    base64_image = base64.b64encode(buffer.getvalue()).decode() #bytes to base64 encoding & return as string decoding to render in html
    return base64_image

qr_gen_image = qr_generation(local_ip_url)  #generated QR code png for IP address

@app.route("/")
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>G - File Transfer</title>
    <style>
    .qr-code{
        text-align:center;
    }
    .form-data{
        text-align:center;
    }
    body{
        text-align: center;
    }
    a{
        display: block;
        text-decoration: none;
        margin: 5px;
    }
    .download-data{
        margin: 10px;
    }
    </style>
    </head>
    <body>
    
    <div class="qr-code">
    <h2>Scan this QR code: </h2>
    <img src="data:image/png;base64, {{ qr_gen_image }}">
    <h5>Or<br> Visit this url {{ local_ip_url }}</h5>
    </div>
    
    <div class="form-data">
    <form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="file" required>
    <input type="submit" value="Upload">
    </form>
    </div>
    
    <div class="download-data">
    <h2>Available Files</h2>
    {% for file in files %}
    <a href="{{ url_for('download_file', filename=file) }} "> {{ file }}</a>
    {% endfor %}
    
    </div>
    </body>
    </html>
    
    
    '''
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    return render_template_string(html_content, qr_gen_image = qr_gen_image, local_ip_url = local_ip_url, files=files)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)