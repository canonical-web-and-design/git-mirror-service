# Git mirror service

A simple WSGI server to create a mirror of a remote git repository
on another remote.

## CLI usage

The simplest way to mirror repositories is directly on the command-line:

``` bash
./copy-repository.py git@github.com:someone/some-project git@github.com:someone/some-project-clone
```

## Service usage

You can run the service:

``` bash
./wsgi.py      # Directly
# OR
gunicorn wsgi  # With something that speaks WSGI
```

### Optional secret

By default the server is unsecured - anyone who can access it can
use it to mirror to repositories that the server has access to.

To prevent this, you can add a secret:

``` bash
echo "79a36d50-09be-4bf4-b339-cf005241e475" > .secret
```

Once this file is in place, the service will only allow requests if the
secret is provided.

*NB:* For this to be an effective security measure, the server should be
only accessible over HTTPS.

### Service API

Now you can query the service to mirror repositories. It accepts the following
parameters:

```
origin: A git URL to mirror from (the service user must have pull access)
destination: A git URL to mirror to (the service user must have push access)
secret: If secret is enabled, a secret token for authentication.
```

E.g.:

```
http://example.com/secret=79a36d50-09be-4bf4-b339-cf005241e475&origin=git@github.com:someone/some-project&destination=git@github.com:someone/some-project-clone
```
