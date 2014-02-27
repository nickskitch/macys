#!/bin/bash
# description: get ips for nodes on environment:


export envDetailsUrl='http://mdc2vr4073:8888/NewEnvironmentDetails/EnvironmentDetails.html'

export envName=$1
if [[ -z "$envName" ]]
then 
	export envName=mcominternal5017
	echo "No environment specified so defaulting to hard-coded value $envName" 
fi

echo "scraping page to get IPs of Nodes for Macys: $envDetailsUrl"
export curlOutput=''
export curlOutput=`curl -s -d "envName=$envName" "$envDetailsUrl"`

if [[ -z "$curlOutput" ]]
then
	echo "page unreachable; exiting. $envDetailsUrl"
	exit
fi

echo $curlOutput > /tmp/$envName


export legacyIP=`grep 'Legacy' /tmp/$envName | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'`  
export navappIP=`grep 'NavApp' /tmp/$envName | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'` 
export sdpIP=`grep 'SDP' /tmp/$envName | grep 'SDPClient' | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'`  
export db2IP=`grep 'DB2' /tmp/$envName | |grep 'SITE-ASYNC-DB2'|grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'` 

echo "The following vars have been set:"
echo "legacyIP=$legacyIP"
echo "navappIP=$navappIP"
echo "sdpIP=$sdpIP"
echo "db2IP=$db2IP"


