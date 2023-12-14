# 0x17. Web stack debugging #3

## Overview

This project focuses on debugging a WordPress website running on a LAMP (Linux, Apache, MySQL, and PHP) stack. Debugging involves using tools like strace to identify and fix issues causing Apache to return a 500 error. The goal is to automate the fix using Puppet.

## Concepts

- Web Server

- Web Stack Debugging

# Task

<b>0. Strace is your friend</b>

- Description: Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

- File: [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp)
