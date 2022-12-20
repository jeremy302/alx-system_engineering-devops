# installs and configures nginx with X-Served-By header

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  provider        => apt,
  install_options => ['-y'],
}

file_line { 'a':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://sketchfab.com/bluepeno/models permanent;',
}

file_line { 'b':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
}
