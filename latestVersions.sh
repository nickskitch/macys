
# get the latest hudson artifact versions
# legacy
export red='\e[0;31m'
export NC='\e[0m' # No Color 

export branch=14C
echo $branch
export LegacyVersion=`echo -ne "\033[31mLegacy: " && curl -s "http://buildserver:8080/hudson/view/0_UniqueVersionArtifacts/view/${branch}_DeployableArtifacts/job/Macys.war_${branch}_DEPLOY/lastSuccessfulBuild/consoleFull" | grep -m 1 'Macys War Version: ' | grep -Eo '[0-9].[0-9]{2}.[0-9]{1,3}'$`

export NavAppVersion=`echo -ne "\033[31mNavApp: " && curl -s "http://buildserver:8080/hudson/view/0_UniqueVersionArtifacts/view/${branch}_DeployableArtifacts/job/NavApp_${branch}_MCOM_Deploy/lastSuccessfulBuild/consoleFull" | grep -m 1 'MacysNavApp Version: ' | grep -Eo '[0-9]\.[0-9]{2}\.[0-9]{1,3}'$`

export SNSVersion=`echo -ne "\033[31mShopAndServe: " && curl -s "http://buildserver:8080/hudson/view/0_UniqueVersionArtifacts/view/${branch}_DeployableArtifacts/job/SNS_${branch}_MCOM_Deploy/lastSuccessfulBuild/consoleFull" | grep -m 1 'Deploying com.macys.hub:MacysShopNServe.war:' | grep -Eo '[0-9]\.[0-9]{2}\.[0-9]{1,3}'`

echo $LegacyVersion $NavAppVersion $SNSVersion

