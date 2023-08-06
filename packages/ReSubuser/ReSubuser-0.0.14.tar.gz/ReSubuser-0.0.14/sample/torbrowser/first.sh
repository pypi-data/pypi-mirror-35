#!/bin/bash 


APP="$HOME/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/start-tor-browser"


if [ ! -e "$APP" ] 
then
echo "Wait Tor connexion ... " 
tor &
sleep 10 ; torbrowser-launcher
fi

$APP


