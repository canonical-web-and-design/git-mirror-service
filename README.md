Git mirroring service
===

A simple WSGI server to create a mirror of a remote git repository
on another remote.

Server setup
---

Before running the server you need to setup a secret:

``` bash
$ uuidgen > .secret
$ cat .secret
79a36d50-09be-4bf4-b339-cf005241e475  # For example
```

Now run the server:

``` bash
./wsgi.py      # Directly
# OR
gunicorn wsgi  # With something that speaks WSGI
```

Server usage
---

Then visit the server on the correct port with the appropriate parameters:

*NB:* For this to be truly secure, the server should be only accessible over HTTPS.

```
http://example.com/secret=79a36d50-09be-4bf4-b339-cf005241e475&origin=git@github.com:someone/some-project&destination=git@github.com:someone/some-project-clone
```

CLI usage
---

You can also copy repositories directly on the command-line:

``` bash
./copy-repository.py git@github.com:someone/some-project git@github.com:someone/some-project-clone
```
