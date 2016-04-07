# eventbuild

Package eventlog through docker

## Installation

Please use virtualenv with python version 2, i don't tested with python 3.

```console
$ python setup.py install
```

[![asciicast](https://asciinema.org/a/41547.png)](https://asciinema.org/a/41547)


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

[![asciicast](https://asciinema.org/a/41547.png)](https://asciinema.org/a/41547)

### Status: Alpha (heavy development)
