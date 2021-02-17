#!/bin/sh

echo "Script Started"
i=0
while [ "$i" -lt 100 ]   
do
a=`shuf -i 1-999999999999999999 -n 1`
b=`shuf -i 1-99 -n 1`
echo "${a}${b}" >>random.txt
i=$((i+1))
done
echo "List creation Completed"