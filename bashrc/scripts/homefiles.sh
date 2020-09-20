#!/usr/bin/env bash
## source
# shellcheck disable=SC2034
export starting="${BASH_SOURCE[0]}"; debug.sh starting

test -n "${BASHRC_FILE}" || { error.bash BASHRC_FILE 'not defined'; return 1; }

function home_bashrc() {
  local user home file bashrc_path
  if bashrc_path="$( command -v "${BASHRC_FILE}" 2>&1 )"; then
    if sudo -u "${1}" tee "${2}" >/dev/null <<EOT; then
# shellcheck disable=SC1090
if test -f  "${bashrc_path}"; then
  source "${bashrc_path}"
else
  echo 'bashrc file not found'; return 1
fi
EOT
      info.sh homefiles "${2}" "${bashrc_path}"
    else
      error.sh homefiles "${2}"; return 1
    fi
  else
    error.sh files "${2}" "${BASHRC_FILE} - command not found"; return 1
  fi
}

function home_hushlogin () {
  if sudo -u "${1}" touch "${2}"; then
    info.sh homefiles "${2}"
  else
    error.sh homefiles "${2}"; return 1
  fi
}

function home_inputrc () {
  if sudo -u "${1}" cp -f "$( command -v inputrc 2>&1 )" "${2}"; then
    info.sh homefiles "${2}"
  else
    error.sh homefiles "${2}"; return 1
  fi
}

function home_profiles () {
  if sudo -u "${1}" tee "${2}" >/dev/null <<EOT; then
# shellcheck disable=SC1090
if [[ -f ~/.bashrc ]]; then
  . ~/.bashrc
fi
EOT
    info.sh homefiles "${2}"
  else
    error.sh homefiles "${file}"; return 1
  fi
}

function home_file() {
  local user home file bashrc_path
  for user in "${USERNAME}" root kali; do
    if home="$( home.sh "${user}" )"; then
      file="${home}/.bashrc"
      home_bashrc "${user}" "${file}" || return 1
      file="${home}/.hushlogin"
      home_hushlogin "${user}" "${file}" || return 1
      file="${home}/.inputrc"
      home_inputrc "${user}" "${file}" || return 1
      file="${home}/.profile"
      home_profiles "${user}" "${file}" || return 1
      file="${home}/.bash_profile"
      home_profiles "${user}" "${file}" || return 1
    fi
  done
}

function home_secrets() {
  local error
  if ! test -d "${GITHUB_SECRETS_PATH}"; then
    if error="$( git clone "${GITHUB_SECRETS_URL}" "${GITHUB_SECRETS_PATH}" --quiet  2>&1 )"; then
      info.sh clone "${GITHUB_SECRETS_URL}"
    else
      error.sh clone "${GITHUB_SECRETS_URL}" "${error}"; return 1
    fi
  fi
}

function home_links() {
  local error user home file
  cd "${USERHOME}" > /dev/null 2>&1 || { error.sh "${USERHOME}" "invalid"; return 1; }
  for user in root kali; do
    if home="$( home.sh "${user}" )"; then
      sudo -u "${user}" mkdir -p "${home}/.ssh"
      sudo -u "${user}" chmod go-rw "${home}/.ssh"
      touch .ssh/gitconfig
      for file in .ssh/config .ssh/credentials .ssh/gitconfig \
                  $( find .ssh -type f -exec grep -l "END OPENSSH PRIVATE KEY" "{}" \; ) .gitconfig; do
        if ! test -L "${home}/${file}"; then
          sudo -u "${user}" rm -r "${home}/${file}"
          if sudo -u "${user}" ln -s "${USERHOME}/${file}" "${home}/${file}"; then
            info.sh link "${home}/${file}"
          else
            error.sh link "${home}/${file}"; return 1
          fi
        fi
      done
    fi
    done
  cd - > /dev/null || return 1
}

if test "${USER}" = "${USERNAME}" && isuser.sh; then
  home_file || exit 1
  home_secrets || exit 1
  home_links || exit 1
fi

unset starting bashrc_path