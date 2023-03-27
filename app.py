from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route('/')
def home():
    """Landing page."""
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Pics', 'url': 'https://example.com/3'}]
    
    return render_template(
        'home.html',
        title="Creator Website",
        description="Smarter page templates with Flask & Jinja."
    )

if __name__ == '__main__':
    app.run(debug=True)
    