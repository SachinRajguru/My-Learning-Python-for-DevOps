# Import the Flask class from the 'flask' module.
# Flask is a lightweight web framework for Python that helps you create web applications.
# This line brings in the tools we need to build our app.
from flask import Flask

# Create an instance (object) of the Flask application.
# '__name__' is a special built-in Python variable that holds the name of the current module.
# Passing it to Flask tells the app where to look for templates, static files, etc.
# Think of 'app' as the main object that represents your web application.
app = Flask(__name__)

# This is a decorator (a special function that modifies another function).
# '@app.route('/')' means: when someone visits the root URL of your website (like http://localhost:5000/),
# Flask should call the function below it.
# The '/' represents the homepage or base path.
@app.route('/')

# Define a function called 'hello_world'.
# This function runs when the decorated route ('/') is accessed.
# It simply returns a string (text) that will be displayed in the browser.
def hello_world():
    return 'Hello, World!'

# This is a common Python idiom (pattern) to check if this script is being run directly
# (not imported as a module in another script).
# If you run this file with 'python hello-world.py', '__name__' will be '__main__',
# so the code inside will execute.
# This prevents the server from starting if this file is imported elsewhere.
if __name__ == '__main__':
    # Start the Flask development web server.
    # "0.0.0.0" means the server will listen on all available network interfaces (IPs),
    # not just localhost. This is useful for accessing the app from other devices on the network.
    # By default, it runs on port 5000. You can visit http://localhost:5000/ in your browser
    # to see "Hello, World!" once the server starts.
    app.run("0.0.0.0")

# HOW TO RUN THIS CODE (Step-by-Step for Beginners):
# 1. Install Flask: Open your terminal/command prompt and run:
#    pip install flask
#    (This installs the Flask library if you haven't already.)
#
# 2. Save the code: Save this as a file, e.g., 'hello-world.py'.
#
# 3. Run the script: In your terminal, navigate to the folder with the file and type:
#    python hello-world.py
#    (Or 'python3 hello-world.py' on some systems like macOS/Linux.)
#    You should see output like: "Running on all addresses (0.0.0.0)" and "Running on http://127.0.0.1:5000".
#    The server is now live! It will keep running until you stop it.
#
# 4. Test the app:
#    - Open your web browser and go to http://localhost:5000/ (or http://127.0.0.1:5000/).
#    - You should see "Hello, World!" displayed on the page.
#    - If you're on another device on the same network, you can access it via http://YOUR-COMPUTER-IP:5000/
#      (Find your IP with 'ipconfig' on Windows or 'ifconfig'/'ip addr' on macOS/Linux.)
#
# 5. Stop the server: In the terminal where it's running, press Ctrl+C (or Cmd+C on macOS).
#
# Troubleshooting:
# - If port 5000 is busy (e.g., another app using it), add 'port=5001' to app.run(), like: app.run("0.0.0.0", port=5001).
# - Ensure your firewall allows incoming connections on the port if accessing from other devices.
# - This is for development only; for production, use a proper server like Gunicorn.
# - No additional data or POST requests needed—this is a simple GET endpoint for the homepage.
#
# OR
#
# How to Run:
# 1. Save as 01-hello-world.py.
# 2. Terminal: pip install flask (if needed).
# 3. Run: python 01-hello-world.py
#    - Output: * Running on all addresses (0.0.0.0):5000
# 4. Test:
#    - Local: Browser/curl http://localhost:5000/ → "Hello, World!"
#    - EC2: http://ec2-public-ip:5000/ → Same.
#    - Wrong: http://localhost:5000/abc → 404 Not Found (Flask handles via decorator).
# Troubleshooting:
# - Port Busy: Change port=9000.
# - External Access: On EC2, open port 5000 in security group (inbound TCP).
# - Stop: Ctrl+C. For prod, use Gunicorn: pip install gunicorn; gunicorn -w 4 -b 0.0.0.0:5000 app:app
# Pro Tip: Decorators run "before" function (e.g., for auth: Check token first).
