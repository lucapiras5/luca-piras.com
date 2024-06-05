from flask import Flask, request
from markupsafe import escape as esc
from markdown import markdown
import tomli
import re


class Layout:
    def __init__(self, title, body, description=''):
        self.title = esc(title)
        self.body = body
        self.meta_description = esc(description or title)
        self.description = esc(description)
        self.html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>{self.title}</title>

        <link rel="icon" href="/static/favicon.png">

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/index.css">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <meta property="og:title" content="{self.title}">
        <meta property="og:image" content="/static/avatar.jpg">
        <meta property="og:description" content="{self.meta_description}">

        </head>

        <body>
        <div id="wrapper">
        <header>
        <div class="horizontal-links">
        <div class="link"><a href="/">Home</a></div>
        <div class="link"><a href="/cv-resume">CV / Resume</a></div>
        <div class="link"><a href="/personal-knowledge">Personal Knowledge</a></div>
        <div class="link"><a href="/news">News</a></div>
        <div class="link"><a href="/future-plans">Future Plans</a></div>
        </div>

        <h1>{self.title}</h1>

        {self.description}

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
    return markdown(read_file(filename), extensions=['smarty', 'fenced_code', 'toc'])

def page_from_markdown_file(filename: str):
    rendered = read_markdown_file(filename)
    # Extract metadata block
    pattern = r"""<!--
(.+?)
-->"""
    block = re.search(pattern, rendered, re.DOTALL)
    if block is None:
        raise ValueError("Page is missing metadata block")
    metadata = tomli.loads(block.group(1))
    print(repr(metadata))
    return Layout(body=rendered, **metadata).html

@app.get("/")
def homepage():
    return page_from_markdown_file("pages/index.md")

@app.get("/<page_id>")
def get_page(page_id):
    return page_from_markdown_file(f"pages/{page_id}.md")
