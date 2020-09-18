#!/usr/bin/env bash

test -n "${1}" || { error.sh "Project Path" "must be specified"; exit 1; }
cd "${1}" > /dev/null 2>&1 || { error.sh "${1}" "invalid"; exit 1; }

/bin/rm -fr build/ > /dev/null
/bin/rm -fr dist/ > /dev/null
/bin/rm -fr .eggs/ > /dev/null
find . -name '*.egg-info' -exec /bin/rm -fr {} +
find . -name '*.egg' -exec /bin/rm -f {} +
find . -name '*.pyc' -exec /bin/rm -f {} +
find . -name '*.pyo' -exec /bin/rm -f {} +
find . -name '*~' -exec /bin/rm -f {} +
find . -name '__pycache__' -exec /bin/rm -fr {} +
/bin/rm -fr .tox/
/bin/rm -fr .pytest_cache
find . -name '.mypy_cache' -exec /bin/rm -rf {} +

debug Project: "${1}" clean
cd - || exit 1
