# installs and configures nginx
exec { 'apt-get update':
  path => ['/bin', '/usr/bin'],
}

package { 'nginx':
  provider        => apt,
  install_options => ['-y'],
}

file { '/var/www/html/index.html':
  content => "Hello World!"
}

file { '/etc/nginx/sites-enabled/default':
  content =>
"server {
	listen 80 default_server;
	listen [::]:80 default_server;

    root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

    server_name _;
    rewrite ^/redirect_me / permanent;
	location / {
		try_files \$uri \$uri/ =404;
	}
}"
}

exec { 'nginx':
  path    => '/usr/bin:/usr/sbin:/bin',
}
