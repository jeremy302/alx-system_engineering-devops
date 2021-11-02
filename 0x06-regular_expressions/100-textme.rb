#!/usr/bin/env ruby
s = ARGV[0]
puts "#{/\[from:.*?\]/.match(s)},#{/\[to:.*?\]/.match(s)},#{/\[flags:.*?\]/.match(s)}"
