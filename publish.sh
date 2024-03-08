#!/bin/bash

rm -rf book/_build/html
pipx run black\[jupyter\] book
poetry run jupyter-book build book
pipx run ghp-import -n -p -f book/_build/html -c aprenda.quantumket.org
