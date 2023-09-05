#!/usr/bin/env ruby

input_string = ARGV[0]

# Use a regular expression to match the pattern and capture groups
matches = input_string.scan(/from:(\+?.+)\]\s.to:(\+?.+)\]\s.flags:(.{12,13})\]/)

# Check if there is a match
if matches.any?
  # Join the captured groups
  result = matches.map { |match| match.join(",") }.join
  puts result
else
  puts "No match found"
end
