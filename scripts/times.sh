#!/usr/bin/env bash

if [[ "${TIMES-}" ]]; then
  echo -n "$(grey.sh "${1}"): $(orange.sh "${!1}")"
  shift
  while (("$#")); do
    echo -n ", $(grey.sh "${1}"): $(orange.sh "${!1}")"
    shift
  done
  echo
fi
