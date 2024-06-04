# luca-piras.com

## Set-up

Install Python, Pipenv and Git. The specific package names may change based on your distribution/OS.

- Debian and Ubuntu: `apt install python3 python-is-python3 pipenv git`
- Arch: `pacman -S python pipenv git`
- FreeBSD: `pkg install python39 py39-pipenv git`

Clone this repository:

`git clone https://github.com/lucapiras5/luca-piras.com`

Install dependencies:

```
cd luca-piras.com
pipenv install
```

## Maintenance

Start the venv:

`pipenv shell`

Launch the server with Gunicorn:

`gunicorn app:app`

Rebuild the CV (requires TeXLive):

`./mkcv.sh`
