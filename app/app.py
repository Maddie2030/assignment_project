from flask import Flask

# Create an instance of the Flask class
# __name__ is a special Python variable that gives the name of the current module.
# Flask uses this to know where to look for resources like templates and static files.
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    This function is called when someone accesses the root URL.
    It returns a simple HTML string to be displayed in the browser.
    """
    return '<p>Hello, World! ...............' \
    '..................................' \
    '...........................,,,,,,,,,...,,,,,,,,,...</p>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug="True")