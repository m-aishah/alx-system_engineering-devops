# Installs flask from pip3.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package { 'werkzeug': # Use a compatible Werkzeug version.
  ensure   => '2.1.1',
  provider => 'pip3',
}
