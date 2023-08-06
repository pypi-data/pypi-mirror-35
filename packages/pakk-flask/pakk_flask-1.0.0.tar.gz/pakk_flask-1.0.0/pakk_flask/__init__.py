"""
Utilities for handling assets packaged in a Pakk file while working with Flask.
"""
from mimetypes import guess_type
from flask import send_file, send_from_directory as flask_send_from_directory
from werkzeug.exceptions import NotFound
from pakk import Pakk

def send_from_directory(directory, filename, **options):
    """
    A replacement for Flask's send_from_directory that supports pakked files.

    if directory is an instance of a Pakk object, then this method will decrypt the file within the Pakk and
    return the decrypted contents.
    """

    if isinstance(directory, Pakk):
        if directory.has_blob(filename):
            content = directory.get_blob(filename)

            guessed_type = guess_type(filename)
            mimetype = options.get("mimetype")

            if not mimetype:
                mimetype = f"{guessed_type[0]};"
                if not guessed_type[1]:
                    if guessed_type[0] is not None and guessed_type[0].startswith("text/"):
                        mimetype += f" charset=utf-8"
                else:
                    mimetype += f" charset={guessed_type[1]}"

            content.stream.seek(0)

            return send_file(
                content.stream,
                mimetype=mimetype
            )

        return NotFound()
    else:
        return flask_send_from_directory(directory, filename, **options)
