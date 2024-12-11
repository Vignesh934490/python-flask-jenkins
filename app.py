from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, Jenkins!'

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)

