# Puppet SSH Config
include stdlib
file_line { 'Disable password authentication':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^*PasswordAuthentication*',
}

file_line { 'add identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/holberton',
  match => '^*IdentityFile ~/xssh/holberton*',
}
