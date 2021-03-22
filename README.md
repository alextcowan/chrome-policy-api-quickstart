# chrome-policy-api-quickstart

**This is not an officially supported Google product**

Simple script to pull policies via Chrome Policy API  
Leverages google-api-python-client for credential/token handling and OAuth flow.  
  
  
## Getting Started

```shellscript
$ python3 -m venv chrome-policy-api-test

$ source chrome-policy-api-test/bin/activate

$ pip install google-api-python-client

$ pip install google-auth-oauthlib
```

## OAuth 2.0 Access to Google APIs

The script leverages the google-api-python-client and google-auth-oauthlib libraries to authenticate for API access.  
The script will expect and load a credentials.json file created and downloaded via instructions: [here](https://developers.google.com/identity/protocols/oauth2)  
After creating the cloud project on the domain, and creating OAuth credentials then download them into the script directory.  

## Sourcing OrgUnit IDs

The customers.policies.resolve takes an OrgUnit (OU) ID as a parameter.  
These IDs can be sourced from the admin console by selecting an OU from the Organizational Unit sidebar at the [device setting page](https://admin.google.com/ac/chrome/settings/user)  
After selecting the OU link from the left-hand column, the URL will have an "org=" argument which contains the OU ID.  
For example, https://admin.google.com/ac/chrome/settings/user?org=03ph8a2z468tl2k  

## Sample Output
  
>Single OU  

```shellscript
$ ORG_ID=03ph8a2z468tl2k
$ ORG_NAME="Frontline"
$ python chrome_policy_api_qs.py --org_id=$ORG_ID --org_name=$ORG_NAME
Non-default policies for [Frontline]:
         chrome.users.GoogleCast {'enableMediaRouter': False}
         chrome.users.SecondaryGoogleAccountSignin {'allowedDomainsForApps': ['finelder.com']}
         chrome.users.PromotionalTabsEnabled {'promotionalTabsEnabled': False}
         chrome.users.ShowAccessibilityOptionsInSystemTrayMenu {'showAccessibilityOptionsInSystemTrayMenu': 'TRUE'}
```

>Compare two OUs  

```shellscript
$ ORG_ID=03ph8a2z468tl2k
$ ORG_NAME="Frontline"
$ ORG2_ID=03ph8a2z1sn57b6
$ ORG2_NAME="Knowledge"
$ python chrome_policy_api_qs.py --org_id=$ORG_ID --org_name="$ORG_NAME" --compare --org2_id=$ORG2_ID --org2_name="$ORG2_NAME"

Unique to [Knowledge]:
         chrome.users.EnrollPermission {'deviceEnrollPermission': 'ALLOW_TO_ENROLL_DEVICES_ENUM_ALLOW_RE_ENROLL'}
         chrome.users.Screenshot {'disableScreenshots': True}

In both [Frontline] & [Knowledge]:
        chrome.users.GoogleCast:
                [Frontline]:  {'enableMediaRouter': False}
                [Knowledge]:  {'enableMediaRouter': False}
        chrome.users.SecondaryGoogleAccountSignin:
                [Frontline]:  {'allowedDomainsForApps': ['finelder.com']}
                [Knowledge]:  {'allowedDomainsForApps': ['finelder.com']}
        chrome.users.PromotionalTabsEnabled:
                [Frontline]:  {'promotionalTabsEnabled': False}
                [Knowledge]:  {'promotionalTabsEnabled': False}
        chrome.users.ShowAccessibilityOptionsInSystemTrayMenu:
                [Frontline]:  {'showAccessibilityOptionsInSystemTrayMenu': 'TRUE'}
                [Knowledge]:  {'showAccessibilityOptionsInSystemTrayMenu': 'TRUE'}
 ```
