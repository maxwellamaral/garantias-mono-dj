#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json
from django.core.exceptions import ImproperlyConfigured


def get_secret(setting, secrets_file='secrets.json'):
    """
    Configura a leitura das variáveis de ambiente
    """
    
    with open(secrets_file) as f:
        secrets = json.loads(f.read())
        try:
            return secrets[setting]
        except KeyError as e:
            error_msg = f"Set the {setting} environment variable"
            raise ImproperlyConfigured(error_msg) from e

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_secret("DJANGO_SETTINGS_MODULE"))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
