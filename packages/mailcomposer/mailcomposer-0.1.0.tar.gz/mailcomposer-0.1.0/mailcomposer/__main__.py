#!/usr/bin/env python

"""Demonstration of the MailComposer class."""

import os
import sys

from . import *


def demo():
    """Demonstrate the MailComposer class."""

    mc = MailComposer()
    mc.to = "Odysseus <nobody@example.com>"
    mc.subject = "MailComposer Demo"

    try:
        # Use the README file as our test message
        with open("README", "r") as readme:
            mc.body = readme.read()

    except (Exception) as err:
        # Use the exception text as our test message
        mc.body = err

    try:
        # Attach the base.py file
        mc.attach_file(os.path.join("mailcomposer", "base.py"))

    except (OSError):
        # No worries; we just won't get to test attachments
        pass

    mc.display()


if __name__ == "__main__":
    demo()
