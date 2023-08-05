import sys
from os import environ
from os.path import basename, dirname

environ.update(TEST="1")

BASE_DIR = dirname(dirname(__file__))
PROJECT_NAME = basename(BASE_DIR)
sys.path = [BASE_DIR, *sys.path]
