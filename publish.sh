#!/bin/bash

rm -rf book/_build/html
poetry run jupyter-book build book
pipx run ghp-import -n -p -f book/_build/html
