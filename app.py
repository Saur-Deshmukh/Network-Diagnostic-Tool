from flask import Flask, request, render_template, redirect, url_for
import speedtest
import socket
import requests
import subprocess
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-connection')
def check_connection_page():
    return render_template('check_connection.html')

@app.route('/measure-speed')
def measure_speed_page():
    return render_template('measure_speed.html')

@app.route('/get-ip')
def get_ip_page():
    return render_template('get_ip.html')

@app.route('/geo-location')
def geo_location_page():
    return render_template('geo_location.html')

@app.route('/ping')
def ping_page():
    return render_template('ping.html')

@app.route('/traceroute')
def traceroute_page():
    return render_template('traceroute.html')

@app.route('/run-check-connection')
def run_check_connection():
    try:
        requests.get("http://google.com", timeout=5)
        result = "Internet connection is active."
    except requests.ConnectionError:
        result = "No internet connection."
    return render_template('check_connection.html', result=result)

@app.route('/run-measure-speed')
def run_measure_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        result = f"Download Speed: {round(download_speed, 2)} Mbps<br>Upload Speed: {round(upload_speed, 2)} Mbps"
    except Exception as e:
        result = f"Error: {e}"
    return render_template('measure_speed.html', result=result)

@app.route('/run-get-ip')
def run_get_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = requests.get('https://api.ipify.org').text
        result = f"Local IP: {local_ip}<br>Public IP: {public_ip}"
    except Exception as e:
        result = f"Error: {e}"
    return render_template('get_ip.html', result=result)

@app.route('/run-geo-location')
def run_geo_location():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        response = requests.get(f'https://ipapi.co/{public_ip}/json/').json()
        result = f"IP: {public_ip}<br>Location: {response.get('city')}, {response.get('region')}, {response.get('country_name')}"
    except Exception as e:
        result = f"Error: {e}"
    return render_template('geo_location.html', result=result)

@app.route('/run-ping', methods=['POST'])
def run_ping():
    site = request.form.get('site')
    try:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        process = subprocess.run(["ping", param, "4", site], capture_output=True, text=True)
        result = f"Ping to {site}:<br><pre>{process.stdout}</pre>"
    except Exception as e:
        result = f"Error: {e}"
    return render_template('ping.html', result=result)

@app.route('/run-traceroute', methods=['POST'])
def run_traceroute():
    site = request.form.get('site')
    try:
        param = "tracert" if platform.system().lower() == "windows" else "traceroute"
        process = subprocess.run([param, site], capture_output=True, text=True)
        result = f"Traceroute to {site}:<br><pre>{process.stdout}</pre>"
    except Exception as e:
        result = f"Error: {e}"
    return render_template('traceroute.html', result=result)
@app.route('/dns-lookup')
def dns_lookup_page():
    return render_template('dns_lookup.html')

@app.route('/run-dns-lookup', methods=['POST'])
def run_dns_lookup():
    domain = request.form.get('domain')
    try:
        result = socket.gethostbyname_ex(domain)
        hostname, aliases, ip_addresses = result
        output = f"Hostname: {hostname}<br>Aliases: {', '.join(aliases)}<br>IP Addresses: {', '.join(ip_addresses)}"
    except Exception as e:
        output = f"Error: {e}"
    return render_template('dns_lookup.html', result=output)


if __name__ == '__main__':
    app.run(debug=True)
