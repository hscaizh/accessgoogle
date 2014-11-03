#!/bin/bash

set -e
set -u

HOSTSDIR="/etc"
STARTMARK="####mark#####forgoogle####start####"
ENDMARK="####mark#####forgoogle####end####"

if [ "$UID" -ne "0" ]
then
  echo "自动替换hosts需要root权限执行"
  exit 0
fi



function replace_hosts()
{
	if [ -f ./hosts ]
	then
	cp $HOSTSDIR/hosts $HOSTSDIR/hostsbak
	sed -i '/'${STARTMARK}'/,/'${ENDMARK}'/d' $HOSTSDIR/hosts
	echo $STARTMARK >> $HOSTSDIR/hosts
	cat ./hosts >> $HOSTSDIR/hosts
	echo $ENDMARK >> $HOSTSDIR/hosts
	else
	echo "hosts not find!"
	exit 1
	fi 
}

if [ $# -gt 2 ]
then
echo "useage:./accessgoogle.sh [ip path/url]"
elif [ $# -eq 2 ]
then
python googleip.py ${1:-''}
else
python googleip.py 
fi

replace_hosts
echo "replace hosts complete"
exit 0
