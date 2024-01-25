#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

domain="$1"

# Find subdomains using dnsdumpster (make sure to respect website policies)
curl -s "https://dnsdumpster.com/?&q=$domain" | grep -Eo "https?://[^\"/]+" | grep "$domain" | sort -u

# Get WHOIS information
whois $domain
