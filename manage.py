#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # hack to prevent admin promt
    if 'syncdb' in sys.argv:
        sys.argv.append('--noinput')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PLEX.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
