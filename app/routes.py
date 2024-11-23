# app/routes.py
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Example HTML with buttons for GET and POST
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to Flask App</h1>
        <form action="/api/data" method="get">
            <button type="submit">Trigger GET</button>
        </form>
        <form action="/api/data" method="post">
            <button type="submit">Trigger POST</button>
        </form>
    </body>
    </html>
    """
    return html
