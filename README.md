# eventbuild

Package eventlog through docker

## Usage

Build the image docker with:

```console
$ ./eventlog-build build image
```

Package the eventlog repo, you can specify the destination path (default is ./):

```console
$ ./eventlog-build -d /tmp package repo
```

And update the repo with a simple draft based on commit messages:

```console
$ ./eventlog-build --user zoek1 --repo 'https://github.com/zoek1/eventlog' publish draft
Password: 
Overview of the current release: 
release 0.2.14
```


### Status: Alpha (heavy development)
