# kills a program
exec { 'pkill killmenow':
  path => ['/bin', '/usr/bin'],
}
