#!/bin/bash

export leaseHtml="http://confluence.mstdev.corp:8080/display/myservicesjc/Johns+Creek+%28vCloud%29+MCOM+Active+Environment+Leases"
export envName="mcominternal5024"

export daysLeft=`curl -s $leaseHtml | grep -A 5 $envName | tail -n +6 | grep -Eo '[0-9]{1,3}'`
echo "Days until env expires:" $daysLeft

if [ $daysLeft -lt 6 ];then
    terminal-notifier -message "$envName expires in $daysLeft days!!" -execute "python -mwebbrowser $leaseHtml"
fi