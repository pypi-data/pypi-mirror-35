# pakk flask

Utilities for working with pakk files in a flask web application.

## Getting Started

Install pakk and pakk_flask:

```sh
$ python3 -m pip install pakk pakk_flask
```

Then you can use pakk_flask to send pakked assets as static files in a flask web application:

```py
from pakk_flask import send_from_directory

@APP.route("/static/<path:path>")
def get_static_file(path):
    with open("./files.pakk", "rb") as in_file:
        unpakked = unpakk(KEY, in_file)
        if unpakked.has_blob(path):
            return send_from_directory(unpakked, path)
        else:
            return send_from_directory("./static", path)
```
