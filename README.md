# eventbuild

Package eventlog through docker

## Installation

Please use virtualenv with python version 2, i don't tested with python 3.

```console
$ python setup.py install
```

<script type="text/javascript" src="https://asciinema.org/a/41547.js" id="asciicast-41547" async></script>

## Usage

Build the image docker with:

```console
$ eventlog-build build image
```

Package the eventlog repo, you can specify the destination path (default is ./):

```console
$ eventlog-build -d /tmp package repo
```

And update the repo with a simple draft based on commit messages:

```console
$ eventlog-build --user zoek1 --repo 'https://github.com/zoek1/eventlog' publish draft
Password: 
Overview of the current release: 
release 0.2.14
```

<script type="text/javascript" src="https://asciinema.org/a/41550.js" id="asciicast-41550" async></script>

### Status: Alpha (heavy development)
