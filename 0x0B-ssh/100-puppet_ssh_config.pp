# creates a file
file { '/etc/ssh/ssh_config':
  content => '# ssh client configuration
Match all
IdentityFile ~/.ssh/school
PasswordAuthentication no',
}

