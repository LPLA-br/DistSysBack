#!/bin/bash

# CLIENTE curl
# LPLA-br

read -p 'a> ' A
read -p 'b> ' B

echo "{\"a\":$A,\"b\":$B}" | curl telnet://192.168.27.250:8080
