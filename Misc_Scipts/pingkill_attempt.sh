#!/bin/bash

# While this appears to consume remote resources it is only using large ping packets and handling the responses strangely and is only detremental to the script host

num=100000

systemctl start ping

ping -s 65507 10.8.0.100 &
ping -s 65507 10.8.0.101 &
ping -s 65507 10.8.0.102 &
ping -s 65507 10.8.0.103 &
ping -s 65507 10.8.0.104 &
ping -s 65507 10.8.0.105 &
ping -s 65507 10.8.0.106 &
ping -s 65507 10.8.0.107 &
ping -s 65507 10.8.0.108 &
ping -s 65507 10.8.0.109 &
ping -s 65507 10.8.0.110 &
ping -s 65507 10.8.0.111 &
ping -s 65507 10.8.0.112 &
ping -s 65507 10.8.0.114 &
ping -s 65507 10.8.0.113 &
ping -s 65507 10.8.0.115 &
ping -s 65507 10.8.0.116 &
ping -s 65507 10.8.0.117 &
ping -s 65507 10.8.0.118 &
ping -s 65507 10.8.0.119 &
ping -s 65507 10.8.0.120 &
ping -s 65507 10.8.0.121 &
ping -s 65507 10.8.0.122 &
ping -s 65507 10.8.0.123 &
ping -s 65507 10.8.0.124 &
ping -s 65507 10.8.0.125 &
ping -s 65507 10.8.0.126 &
ping -s 65507 10.8.0.127 &
ping -s 65507 10.8.0.128 &
ping -s 65507 10.8.0.129 &
ping -s 65507 10.8.0.130 &
ping -s 65507 10.8.0.131 &
ping -s 65507 10.8.0.132 &
ping -s 65507 10.8.0.133 &
ping -s 65507 10.8.0.134 &
ping -s 65507 10.8.0.135 &

systemctl stop ping
