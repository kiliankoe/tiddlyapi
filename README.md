# 🧠 tiddlyapi

[![Docker Automated build](https://img.shields.io/docker/automated/kiliankoe/tiddlyapi.svg)](https://hub.docker.com/r/kiliankoe/tiddlyapi/)

A tiny little JSON api for accessing tiddlywiki data programmatically.

Running this requires two environment variables to be set.

 - `TIDDLYWIKI_DIRECTORY`: pointing to the root directory of the wiki, a subdir named `tiddlers` is expected to exist.
 - `PASSPHRASE`: A passphrase that is expected to be sent with every request in an `Authorization` header.

A sample `docker-compose.yml` to deploy this could look like the following.

```yaml
version: '3'

services:
  app:
    image: kiliankoe/tiddlyapi
    ports:
      - 5000:5000
    volumes:
      - /path/to/your/wiki:/wiki
    environment:
      - TIDDLYWIKI_DIRECTORY=/wiki
      - PASSPHRASE=foobarbaz
```

## Usage

The following endpoints are currently available.

#### `/`

Returns a list of all existing tiddlers.

#### `/t/<name>`

Returns the contents and metadata of the tiddler with the specified name.

#### `/search?query=<query>`

Returns a list of tiddlers matching a specified search `query`.
