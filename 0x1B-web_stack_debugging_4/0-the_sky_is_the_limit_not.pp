# fixes bug on sandbox
exec { 'patch':
  command => "bash -c \"sed -i.bak 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' /etc/default/nginx && service nginx restart",
  path    => '/usr/bin:/usr/sbin:/bin'
}
