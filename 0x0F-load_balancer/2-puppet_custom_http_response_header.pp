# installs and configures nginx with X-Served-By header

exec { '/usr/bin/apt-get update': }

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line { 'file1':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://sketchfab.com/bluepeno/models permanent;',
}

file_line { 'file2':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

service { 'nginx':
  ensure  => running,
}
