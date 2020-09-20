#!/usr/bin/env bash
export starting="${BASH_SOURCE[0]}"; debug.sh starting

function authorized_keys() {
  local user home file key tmp
  for user in "${USERNAME}" root kali; do
    if home="$( home.sh "${user}" )"; then
      file="${home}/.ssh/authorized_keys"
      sudo -u "${user}" mkdir -p "${home}/.ssh"
      sudo -u "${user}" chmod go-rw "${home}/.ssh"
      sudo -u "${user}" touch "${file}"
      for key in "${GITHUB_USERNAME}" "${NFERX_GITHUB_USERNAME}"; do
        if tmp="$( curl -sLhttps://github.com/"${key}".keys )"; then
          if ! grep "${tmp}" "${file}" > /dev/null 2>&1; then
            if echo "${tmp}" | sudo -u "${user}" tee -a "${file}" > /dev/null 2>&1; then
              info.sh authorized_keys "${key}" "${file}"
            else
              info.sh authorized_keys "${key}" "${file}"; return 1
            fi
          fi
        else
          error.sh authorized_keys "${key} ${file}" "${tmp}"; return 1
        fi
      done
    fi
  done
}

function ssh_config() {
  local file
  file="${USERHOME}/.ssh/config"
  if tee "${file}" >/dev/null <<EOT; then
Host *
    AddressFamily inet
    BatchMode yes
    CheckHostIP no
    ControlMaster auto
    ControlPath /tmp/ssh-%h-%r-%p
    ControlPersist 20m
    IdentitiesOnly yes
    IdentityFile ~/.ssh/id_rsa
    LogLevel QUIET
    StrictHostKeyChecking no
    User ${USERNAME}
    UserKnownHostsFile /dev/null

  Host github.com
    HostName github.com
    User ${GITHUB_ORGANIZATION_ID}

  Host github.com.${GITHUB_USERNAME}
    HostName github.com
    User ${GITHUB_USERNAME}
    IdentityFile ~/.ssh/${GITHUB_USERNAME}
EOT
    info.sh ssh "${file}"
    if secrets-push.sh; then return 0; else return 1; fi
  else
    error.sh ssh "${file}"
    return 1
  fi
}

function etc_hosts() {
  local file
  file="/etc/hosts"
  if sudo tee "${file}" >/dev/null <<EOT; then
127.0.0.1       localhost
255.255.255.255 broadcasthost
${KALI_IP} kali.com kali
${HP_IP} hp.com hp
EOT
    info.sh ssh "${file}"
  else
    error.sh ssh "${file}"
    return 1
  fi
}

if test "${USER}" = "${USERNAME}" && isuserdarwin.sh; then
  etc_hosts || exit 1
  ssh_config || exit 1
fi

if test "${USER}" = "${USERNAME}"; then
  authorized_keys || exit 1
fi

unset starting