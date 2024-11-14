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

