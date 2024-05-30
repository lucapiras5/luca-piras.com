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
        </div>
        </header>
        {body}
        <footer>&copy; Luca Piras, 2024, CC BY-SA and AGPL-licensed, see the <a href="/legal-notices">legal notices</a>.</footer>
        </div>
        </body>
        </html>
        """

app = Flask(__name__)

@app.get("/")
def homepage():
    body = markdown(
"""

# Luca Piras

<div class="center-text">

<figure id="avatar">
<img width="256px" src="/static/avatar.jpg">
<figcaption><p>Photo by <a href="https://unsplash.com/photos/yellow-and-white-fish-in-water-h_4fe8fmb1E">Max Ducourneau</a>.</p></figcaption>
</figure>

<p>
Law school graduate; self-taught programmer; aspiring digital forensics consultant.
</p>

<div class="vertical-links">
<div class="link"><a href="/digital-forensics">Digital forensics</a></div>
<div class="link"><a href="/notes-on-gnu-linux">Notes on GNU/Linux</a></div>
<div class="link"><a href="/notes-on-programming">Notes on programming</a></div>
</div>

</div>

""")
    return Layout(title='Luca Piras', body=body).html

@app.get("/digital-forensics")
def digital_forensics():
    body = markdown(
"""
# Digital forensics

[**Uso del software libero e open source per l'analisi scientifica della prova digitale nell'informatica forense**](/static/informatica-forense/Tesi_Informatica_Forense_2024.pdf)
(2024).
(*On using free and open source software to scientifically analyze digital evidence in digital forensics*.)
My final dissertation. Currently it's only available in Italian, but an English translation is in the works.
The [source files](https://github.com/lucapiras5/tesi-informatica-forense) are available.

The "[*Notes on programming*](/notes-on-programming)" section of this website expands upon the third chapter of my dissertation, which analyzes some good practices on how to develop reliable and scientific-grade free and open source software.

[**Alcune osservazioni sulla digital evidence &ndash; caratteristiche, ricerca, valutazione**](/static/informatica-forense/Alcune_osservazioni_sulla_digital_evidence_2020.pdf)
(2020).
(*Some observations on digital evidence &ndash; its characteristics, investigation, evaluation*.)
A research paper written while attending the digital forensics course in university.

In 2016, I attended a practical course on digital forensics held by [BIT4LAW](https://www.bit4law.com/).

Over the years, I've also attended various seminars on the subject.
""")
    return Layout(title='Digital Forensics', body=body).html

@app.get("/cv-certifications")
def cv_and_certifications():
    body = markdown("""
# CV & Certifications

[**Curriculum vitae**](/static/Piras_Luca_CV.pdf): also includes my contact information.

[**Autodichiarazione sostitutiva della laurea con voti degli esami**](static/Dichiarazione_sostitutiva_laurea_voti.pdf): *Self-signed degree certificate, with exam scores*, acts as an interim certificate until I receive my degree. I obtained the maximum score, 110/110 *cum laude*.
""")
    return Layout(title="Luca Piras' CV/Resume", body=body).html


@app.get("/legal-notices")
def legal_notices():
    body = markdown("""
# Legal Notices

## Source code

All content on this website is licensed under the [Creative Commons Attribution ShareAlike 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/deed.en), unless noted otherwise (e.g., code samples may be licensed with a different license).

The source code for this website is available [here](https://github.com/lucapiras5/luca-piras.com), under the [AGPLv3.0-or-later](https://spdx.org/licenses/AGPL-3.0-or-later.html) license.

## Limitations of liability

The information provided in this website is accompanied by two disclaimers.

The first is that it shouldn't be considered legal or technical advice.

All information presented here is generic, and shouldn't be considered a substitute for a professional assessment given by someone who is familiar with the specifics of your case.

The second is that it may contain factual errors, inaccuracies, or omissions.

There is no warranty of accuracy, please double-check yourself before using the information for any purposes, including citing me. If you'd like, please submit a correction by contacting me, or opening an issue on GitHub.

## Privacy
   
Please note that for security and performance reasons, this website is proxied by [Cloudflare](https://cloudflare.com). If this is a cause for concern for you, feel free to obtain and run a local copy of this website.
""")
    return Layout(title="Legal Notices", body=body).html

@app.get("/notes-on-programming")
def notes_on_programming():
    body = markdown("""
# Notes on programming

(coming soon)
""")

    return Layout(title="Notes on programming", body=body).html

@app.get("/notes-on-gnu-linux")
def notes_on_linux():
    body = markdown("""
# Notes on GNU/Linux

(coming soon)
""")

    return Layout(title="Notes on programming", body=body).html
