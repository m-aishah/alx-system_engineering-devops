# Define SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => '
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
',
}

# Ensure correct permissions on the SSH configuration file
file { '/etc/ssh':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}
