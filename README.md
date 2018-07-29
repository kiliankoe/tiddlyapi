# 🧠 tiddlyapi

A tiny little JSON api for accessing tiddlywiki data programmatically.

Running this requires two environment variables to be set.

 - `TIDDLYWIKI_DIRECTORY`: pointing to the root directory of the wiki, a subdir named `tiddlers` is expected to exist.
 - `PASSPHRASE`: A passphrase that is expected to be sent with every request in an `Authorization` header.

A sample `docker-compose.yml` to deploy this could look like the following.

```yaml
version: '3'

services:
  app:
    build: .
    ports:
      - 5000:5000
    volumes:
      - /path/to/your/wiki:/wiki
    environment:
      - TIDDLYWIKI_DIRECTORY=/wiki
      - PASSPHRASE=foobarbaz
```
