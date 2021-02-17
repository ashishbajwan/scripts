#!/bin/sh
a=0
while [ "$a" -lt 9 ]   
do
  read -p 'Request: ' a
  sqlmap -r $a.txt --banner --batch --tamper=space2comment
  sleep 1
done
echo "Exit"

