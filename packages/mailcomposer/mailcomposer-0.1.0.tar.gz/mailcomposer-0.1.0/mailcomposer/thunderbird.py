#!/usr/bin/env python

"""Interface for Mozilla Thunderbird."""

import os
import sys
import subprocess

from .base import BaseMailComposer
from .exceptions import MailComposerError

try:
    # Python 3
    from urllib.parse import quote
except (ImportError):
    # Python 2
    from urllib import quote


__all__ = ["ThunderbirdComposer"]


# Find the Thunderbird executable
thunderbird = None
if sys.platform.startswith("win"):
    # Paths to Program Files
    pf_dirs = os.getenv("PROGRAMFILES"), os.getenv("PROGRAMFILES(x86)")

    for program_files in pf_dirs:
        # Path to the Thunderbird executable
        thunderbird_exe = os.path.join(program_files,
                                       "Mozilla Thunderbird",
                                       "thunderbird.exe")

        if os.path.exists(thunderbird_exe):
            thunderbird = thunderbird_exe
            break

else:
    # Search the system path
    system_path = os.getenv("PATH")

    for bin_dir in system_path.split(os.pathsep):
        # Path to the Thunderbird executable
        thunderbird_exe = os.path.join(bin_dir,
                                       "thunderbird")

        if os.path.exists(thunderbird_exe):
            thunderbird = thunderbird_exe
            break


class _ThunderbirdComposer(BaseMailComposer):
    """Interface for Mozilla Thunderbird."""

    def display(self, blocking=True):
        """Display the message in Mozilla Thunderbird."""

        message = {}
        compose_args = []

        # Process the message headers
        if self._to:
            message["to"] = ",".join(self._to)
        if self._cc:
            message["cc"] = ",".join(self._cc)
        if self._bcc:
            message["bcc"] = ",".join(self._bcc)
        if self._subject:
            message["subject"] = self._subject

        # Format the message body
        if self._body:
            if self._body_format == "hybrid":
                message["body"] = self._html_escape(self._body)
                message["format"] = "html"

            else:
                message["body"] = self._body
                message["format"] = self._body_format

        # Process message attachments
        if self._attachments:
            message["attachment"] = ",".join(self._attachments)

        # "thunderbird -compose" uses a variation on standard URL encoding,
        # using "%20" to encode spaces and "," to separate fields
        for kw in message:
            compose_args.append("{0}={1}".format(kw, quote(message[kw])))

        # Process the Thunderbird command line
        thunderbird_args = [thunderbird,
                            "-compose",
                            ",".join(compose_args)]

        # Display the message
        thunderbird_process = subprocess.Popen(thunderbird_args)
        if blocking:
            thunderbird_process.wait()

    # ------------------------------------------------------------------------

    @staticmethod
    def _html_escape(value):
        """Escape HTML special characters in the specified value."""

        return (value
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))


if thunderbird:
    ThunderbirdComposer = _ThunderbirdComposer

else:
    ThunderbirdComposer = None
