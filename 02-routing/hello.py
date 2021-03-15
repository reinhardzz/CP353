from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/abouts')
def about():
    return '<h1>About us</h1>'

@app.route('/news')
def news():
    return """<html> 
        <h1>News</h1> 
        <p>SWU News daily topics:</p>
        <ul>
            <li>Technology</li>
            <li>Sport</li>
            <li>Education</li>
        </ul>
    </html>"""

@app.route('/news/tech')
def tech_news():
    return '<b>technology news</b>'

