from flask import Flask
from markupsafe import escape as esc
from markdown import markdown

class Layout:
    def __init__(self, title, body, description=''):
        self.title = title
        self.body = body
        self.description = description or title
        self.html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>{esc(title)}</title>

        <link rel="icon" href="/static/favicon.png">

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/index.css">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <meta property="og:title" content="{esc(title)}">
        <meta property="og:image" content="/static/avatar.jpg">
        <meta property="og:description" content="{esc(self.description)}">

        </head>

        <body>
        <div id="wrapper">
        <header>
        <div class="horizontal-links">
        <div class="link"><a href="/">Home</a></div>
        <div class="link"><a href="/cv-certifications">CV & Certifications</a></div>
        <div class="link"><a href="/personal-knowledge">Personal Knowledge</a></div>
        <div class="link"><a href="/news">News</a></div>
        <div class="link"><a href="/future-plans">Future Plans</a></div>
        </div>
        </header>
        {body}
        <footer>&copy; Luca Piras, 2024, CC BY-SA and AGPL-licensed, see the <a href="/legal-notices">legal notices</a>.</footer>
        </div>
        </body>
        </html>
        """

app = Flask(__name__)

def read_file(filename: str):
    with open(filename, "r") as fp:
        return fp.read()

def read_markdown_file(filename: str):
    return markdown(read_file(filename))

@app.get("/")
def homepage():
    body = read_markdown_file("pages/index.md")
    return Layout(title='Luca Piras', body=body).html

@app.get("/cv-certifications")
def cv_and_certifications():
    body = read_markdown_file("pages/cv-certifications.md")
    return Layout(title="Luca Piras' CV and resume", body=body).html

@app.get("/legal-notices")
def legal_notices():
    body = read_markdown_file("pages/legal-notices.md")
    return Layout(title="Legal Notices", body=body).html

@app.get("/personal-knowledge")
def notes():
    body = markdown("""
# Personal Knowledge

## Notes on Programming

## Notes on Linux

## Notes on Digital Forensics
""")

    return Layout(title="Personal Knowledge", body=body).html

@app.get("/news")
def news():
    body = read_markdown_file("pages/news.md")
    return Layout(title="News", body=body).html

@app.get("/future-plans")
def future_plans():
    body = read_markdown_file("pages/future-plans.md")
    return Layout(title="Future Plans", body=body).html

