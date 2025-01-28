# 🌐 Network Diagnostic Tool

A Flask-based web application that provides a suite of network diagnostic tools 🛠️, including checking internet connection, measuring network speed, retrieving IP addresses, finding geolocation, pinging websites, tracing routes, performing DNS lookups, and more.

---

## ✨ Features

- ✅ **Check Internet Connection**: Verify if your device is connected to the internet.
- 📊 **Measure Network Speed**: Test your download and upload speeds.
- 🕵️ **Get IP Address**: Retrieve your public IP address.
- 🌍 **Find Geolocation**: Get your current geographical location based on your IP.
- 📡 **Ping Website**: Check the reachability of a website.
- 🛤️ **Trace Route**: Trace the route to a specified website.
- 🧾 **DNS Lookup**: Retrieve DNS records for a domain name.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/network-diagnostic-tool.git
   cd network-diagnostic-tool
2. Run the application:
   ```bash
   python app.py
   ```
3. Open the application in your browser:
   ```bash
   http://127.0.0.1:5000
   ```
---
## 📂 Project Structure
```plaintext
network-diagnostic-tool/
│
├── app.py                   # Flask application
├── templates/               # HTML templates
│   ├── base.html            # Common layout
│   ├── check_connection.html
│   ├── measure_speed.html
│   ├── get_ip.html
│   ├── geo_location.html
│   ├── ping.html
│   ├── traceroute.html
│   └── dns_lookup.html
│
├── static/                  # Static files
│   └── styles.css           # CSS for styling
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
---
## 🛠️ Technologies Used
- Backend: Flask (Python)
- Frontend: HTML, CSS
- Tools: ping, traceroute, speedtest-cli

   
