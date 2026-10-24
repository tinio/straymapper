import os
import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Runs pycodestyle (formerly pep8) on the entire project'

    def handle(self, *args, **options):
        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        subprocess.call(['pycodestyle', project_root])
