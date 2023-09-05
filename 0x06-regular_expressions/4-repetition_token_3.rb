#!/usr/bin/env ruby
# Matches 'hbtn' with zero or more t's.

puts ARGV[0].scan(/hbt*n/).join
