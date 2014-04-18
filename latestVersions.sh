#!/bin/bash
# get the latest hudson artifact versions
# legacy


export branch=14D
export LegacyVersion=`echo -ne "Legacy: " && curl -s "http://buildserver:8080/hudson/view/0_UniqueVersionArtifacts/view/${branch}_DeployableArtifacts/job/Macys.war_${branch}_DEPLOY/lastSuccessfulBuild/consoleFull" | grep -m 1 'Macys War Version: ' | grep -Eo '[0-9].[0-9]{2}.[0-9]{1,3}'$`

export NavAppVersion=`echo -ne "NavApp: " && curl -s "http://buildserver:8080/hudson/view/0_UniqueVersionArtifacts/view/${branch}_DeployableArtifacts/job/NavApp_${branch}_MCOM_Deploy/lastSuccessfulBuild/consoleFull" | grep -m 1 'MacysNavApp Version: ' | grep -Eo '[0-9]\.[0-9]{2}\.[0-9]{1,3}'$`

export SNSVersion=`echo -ne "ShopAndServe: " && curl -s "http://buildserver:8080/hudson/view/0_UniqueVersionArtifacts/view/${branch}_DeployableArtifacts/job/SNS_${branch}_MCOM_Deploy/lastSuccessfulBuild/consoleFull" | grep -m 1 'Deploying com.macys.hub:MacysShopNServe.war:' | grep -Eo '[0-9]\.[0-9]{2}\.[0-9]{1,3}'`

echo -e "Deploying ${branch} ${LegacyVersion} ${NavAppVersion} ${SNSVersion}"
[ -f ./hoursPlus.py ] && python ./hoursPlus.py

