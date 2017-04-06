#!/bin/bash

if [ $# -le 0 ]
then
	echo 'need args'
	exit -1
fi

l_work=`cd $(dirname $0)/..;pwd`
g_conf_dir="$l_work/conf/mysql"

function load_config()
{
    local cluster_name="$1.conf"

    if [ -f "$g_conf_dir/$cluster_name" ]
	then
        . $g_conf_dir/$cluster_name
	else
		echo $1' not exit'
		exit -2
    fi
}

load_config $1

str="mysql -u$user -p$pass -h$host -P$port"

if [ -n "$database" ]
then
	str="$str -D$database"
fi

if [ $# -gt 1 ] && [ -n "$database" ]
then
	mysql -u$user -p$pass -h$host -P$port -D$database -e "$2"
	exit 0
fi

$str
