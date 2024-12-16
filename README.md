### QR-Based Local File Sharing Application  

A lightweight Flask-based application to enable local file sharing through QR codes or a direct URL accessible via any device on the same network.

- **Setup Instructions**:  
1. Run the script and scan the QR code with a smartphone or visit the provided local IP URL from a browser on the same network.
2. Or, download the package file (executable) and run on Windows directly. Check the releases page.]
3. Connect the devices to the same wi-fi network, and open the local flask server. Choose the local network IP and not the local development url 

- **Key Features**:  
  - Automatically generates a QR code linked to the local server's IP address for easy access.  
  - Allows file uploads through a simple web interface.  
  - Lists all uploaded files with download links for quick sharing.  

- **How It Works**:  
  - The application determines the local IP address and starts a server on port 5000.  
  - A QR code is dynamically generated and displayed for easy access. QR codes are stored in a memory buffer and not saved locally. 
  - Files uploaded via the web interface are stored in the `uploads` folder and made available for download.  

- **Prerequisites**: Python, Flask, `pyqrcode`, `pillow`. Install dependencies using `pip install -requirements.txt`.  

- **Access**:  
  - Visit the displayed URL or scan the QR code using any QR scanner app.  
  - Use the web interface to upload or download files seamlessly.  
  
