# luca-piras.com

## Set-up

Install Python, Poetry and Git. The specific package names may change based on your distribution/OS.

Debian and Ubuntu:

```
apt install python3 python-is-python3 python3-poetry git
```

Arch:

```
pacman -S python poetry git
```

FreeBSD:

```
pkg install python39 py39-poetry git
```

Clone this repository:

```
git clone https://github.com/lucapiras5/luca-piras.com
```

Install dependencies:

```
cd luca-piras.com
poetry install
```

## Maintenance

Start the venv, so you can use tasks:

```
poetry shell
```

Launch a production server with Gunicorn:

```
task prod
```

Rebuild the CV (requires TeXLive):

```
task cv
```
