#!/bin/bash


export leaseHtml="http://confluence.mstdev.corp:8080/display/myservicesjc/Johns+Creek+%28vCloud%29+MCOM+Active+Environment+Leases"
export envName="mcominternal5025"

export daysLeft=`curl -s $leaseHtml | grep -A 5 $envName | tail -n +6 | grep -Eo '[0-9]{1,3}'`
echo "Days until $envName expires:" $daysLeft

if [ $daysLeft -lt 3 ];then

    `terminal-notifier -message "$envName expires in $daysLeft days!!" --url "$leaseHtml"`
fi

export envName="mcomexternal113"

export daysLeft=`curl -s $leaseHtml | grep -A 5 $envName | tail -n +6 | grep -Eo '[0-9]{1,3}'`
echo "Days until $envName expires:" $daysLeft

if [ $daysLeft -lt 5 ];then
    `terminal-notifier -message "$envName expires in $daysLeft days!!" --url "$leaseHtml"`
fi