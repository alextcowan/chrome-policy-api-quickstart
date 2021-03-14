# chrome-policy-api-quickstart

Simple script to pull policies via Chrome Policy API  
Leverages google-api-python-client for credential/token handling and OAuth flow  
\
\
## Getting Started

virtualenv \<your_env\>   
source \<your-env\>/bin/activate

pip install google-api-python-client  
pip install google-auth-oauthlib  
\
\
\
## Usage

> Requires OU ID (from OU Settings URL) & OU Name (for results display)   

ORG1_ID=XXXXXXXXXX  
ORG1_NAME="My OU Name"  
\
\

>Show policies for OU  

python chrome_policy_api_qs.py --org_id $ORG1_ID --org_name $ORG1_NAME
\
\
>Show differences between two OUs

ORG2_ID=XXXXXXXXXX
ORG2_NAME="My Other OU"

python chrome_policy_api_qs.py --org_id $ORG1_ID --org_name "$ORG1_NAME" --compare --org2_id $ORG2_ID --org2_name "$ORG2_NAME"  
\
\
## Sample Output
  
>Single OU  

python chrome_policy_api_qs.py --org_id $ORG1 --org_name "$ORG1_NAME"  
Non-default policies for [Knowledge Workers]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.EnrollPermission {'deviceEnrollPermission': 'ALLOW_TO_ENROLL_DEVICES_ENUM_ALLOW_RE_ENROLL'}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.Screenshot {'disableScreenshots': True}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.GoogleCast {'enableMediaRouter': False}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.SecondaryGoogleAccountSignin {'allowedDomainsForApps': ['domain.com']}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.PromotionalTabsEnabled {'promotionalTabsEnabled': False}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.ShowAccessibilityOptionsInSystemTrayMenu {'showAccessibilityOptionsInSystemTrayMenu': 'TRUE'}  
\
\  
>Compare two OUs  

python chrome_policy_api_qs.py --org_id $ORG1 --org_name "$ORG1_NAME" --compare --org2_id=$ORG2_ID --org2_name="$ORG2_NAME"  
Unique to [Knowledge Workers]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.Screenshot {'disableScreenshots': True}  
  
Unique to [Kiosk]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.DeviceEnrollment {'autoDevicePlacementEnabled': True}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.AllowPopulateAssetIdentifier {'allowToUpdateDeviceAttribute': True}  

In both [Knowledge Workers] & [Kiosk]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.EnrollPermission:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Knowledge Workers]:  {'deviceEnrollPermission': 'ALLOW_TO_ENROLL_DEVICES_ENUM_ALLOW_RE_ENROLL'}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[      Kiosk      ]:  {'deviceEnrollPermission': 'ALLOW_TO_ENROLL_DEVICES_ENUM_DISALLOW_ENROLL_RE_ENROLL'}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.GoogleCast:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Knowledge Workers]:  {'enableMediaRouter': False}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[      Kiosk      ]:  {'enableMediaRouter': False}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.SecondaryGoogleAccountSignin:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Knowledge Workers]:  {'allowedDomainsForApps': ['domain.com']}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[      Kiosk      ]:  {'allowedDomainsForApps': ['domain.com']}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.PromotionalTabsEnabled:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Knowledge Workers]:  {'promotionalTabsEnabled': False}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[      Kiosk      ]:  {'promotionalTabsEnabled': False}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chrome.users.ShowAccessibilityOptionsInSystemTrayMenu:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Knowledge Workers]:  {'showAccessibilityOptionsInSystemTrayMenu': 'TRUE'}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[      Kiosk      ]:  {'showAccessibilityOptionsInSystemTrayMenu': 'TRUE'}  