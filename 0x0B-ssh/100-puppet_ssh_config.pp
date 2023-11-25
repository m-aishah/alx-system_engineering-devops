# Ensure correct permissions on the SSH directory
file { '/etc/ssh':
  ensure => 'directory',
#  owner  => 'ubuntu',
#  group  => 'ubuntu',
#  mode   => '0700',
}

# Define SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
#  owner   => 'ubuntu',
#  group   => 'ubuntu',
}

# Include the stdlib module
include stdlib

# Manage IdentityFile line in SSH client configuration
file_line { 'ssh_identity_file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#*IdentityFile\s.*$',
  ensure  => present,
}

# Manage PasswordAuthentication line in SSH client configuration
file_line { 'ssh_password_authentication':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#*PasswordAuthentication\s.*$',
  ensure  => present,
}
