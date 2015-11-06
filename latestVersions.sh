#!/bin/bash
# get the latest hudson artifact versions
# legacy

cd $(dirname $0)

export branch=14K
export LegacyVersion=`echo -ne "Legacy: " && curl -s "http://buildserver.federated.fds:8080/hudson/view/0_UniqueVersionArtifacts/view/0_${branch}_DeployableArtifacts/job/Macys.war_${branch}_DEPLOY/lastSuccessfulBuild/consoleFull" | iconv -f windows-1251| grep -m 1 'Macys War Version: ' | grep -Eo '[0-9].[0-9]{2}.[0-9]{1,3}'$`

export NavAppVersion=`echo -ne "NavApp: " && curl -s "http://buildserver.federated.fds:8080/hudson/view/0_UniqueVersionArtifacts/view/0_${branch}_DeployableArtifacts/job/NavApp_${branch}_MCOM_Deploy_/lastSuccessfulBuild/consoleFull" | iconv -f windows-1251| grep -m 1 'MacysNavApp Version: ' | grep -Eo '[0-9]\.[0-9]{2}\.[0-9]{1,3}'$`

export SNSVersion=`echo -ne "ShopAndServe: " && curl -s "http://buildserver.federated.fds:8080/hudson/view/0_UniqueVersionArtifacts/view/0_${branch}_DeployableArtifacts/job/SNS_${branch}_MCOM_Deploy/lastSuccessfulBuild/consoleFull" | grep -m 1 'Deploying com.macys.hub:MacysShopNServe.war:' | grep -Eo '[0-9]\.[0-9]{2}\.[0-9]{1,3}'`

export WSSGVersion=`echo -ne "WSSG: " && curl -s "http://ci.federated.fds:9090/nexus/service/local/lucene/search?a=WebsiteServicesGateway&v=4.5.*" | grep -m 1 latestRelease | grep -Eo '[0-9]\.[0-9]\.[0-9]{1,3}'`

export MACYUIVersion=`echo -ne "MacyUI: " && curl -s "http://buildserver.federated.fds:8080/hudson/view/0_UniqueVersionArtifacts/view/0_${branch}_DeployableArtifacts/job/MacysUI_${branch}_DEPLOY/lastSuccessfulBuild/consoleFull" | iconv -f windows-1251| grep -m 1 'Macys UI Version: ' | grep -Eo '[0-9]\.[0-9]\.[0-9]{1,3}'$`



echo -e "Deploying ${branch} ${LegacyVersion} ${NavAppVersion} ${SNSVersion} ${MACYUIVersion} ${WSSGVersion}"
[ -f ./hoursPlus.py ] && python ./hoursPlus.py


