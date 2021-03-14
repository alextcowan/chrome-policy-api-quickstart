# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#from __future__ import print_function
import os.path
import argparse
#utilize discovery/build when API is available
#from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import AuthorizedSession


SCOPES = ['https://www.googleapis.com/auth/chrome.management.policy.readonly']
#Only using readonly scope to pull policies (no changes made)
#SCOPES = ['https://www.googleapis.com/auth/chrome.management.policy']

def get_resolved_policies_by_ou(creds, orgunit):
    """Returns resolved policies from orgunit ID via Chrome Policy API"""
    target = "orgunits/"+orgunit
    body = {
        "policySchemaFilter": "chrome.users.*",
        "policyTargetKey": {
            "targetResource": target
        }
    }

    policy_url = 'https://chromepolicy.googleapis.com/v1/customers/my_customer/policies:resolve'

    session = AuthorizedSession(creds)
    try:
        response = session.post(url=policy_url, json=body)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print (error)
        quit()
    
    results = response.json() 

    policies = {}

    for items in results['resolvedPolicies']:
        item = items.get("value")
        policy = item.get("policySchema")
        value = item.get("value")
        policies[policy] = value

    return policies


def diff_orgs(first_policies, fo, second_policies, so):
    """Prints unique and shared resolved policies across two OUs"""
    result = []
    for i in first_policies:
        if i not in second_policies:
            result.append((i,first_policies[i]))
    if result:
        print ("Unique to [%s]:" % fo)
        for i in result:
            print ("\t",i[0], i[1])

    result = []
    for i in second_policies:
        if i not in first_policies:
            result.append((i,second_policies[i]))
    if result:
        print ("\nUnique to [%s]:" % so)
        for i in result:
            print ("\t",i[0], i[1])

    result = []
    for i in first_policies:
        if i in second_policies:
            result.append((i, first_policies[i], second_policies[i]))


    if result:
        print ("\nIn both [%s] & [%s]:" % (fo, so))
        
        #find longest org name and expand shorter to same length
        #aligns policy values in output
        longest_len = len(max(fo,so,key=len))
        so = so.center(longest_len)
        fo = fo.center(longest_len)

        for i in result:
            print ("\t" + i[0] + ":")
            print ("\t\t[%s]: " % (fo), i[1])
            print ("\t\t[%s]: " % (so),i[2])
    
    return

def print_policies(policies, org_name):
    """Prints resolved policies from a single OU"""
    print ("Non-default policies for [%s]:" % (org_name))
    for i in policies:
        print ("\t", i, policies[i])

    return
        
def setup_args():
    """Build argparse arguments"""
    parser = argparse.ArgumentParser(description='Chrome Policy API Quickstart Example')
    parser.add_argument('--compare', help="Compare two orgs",
            action="store_true")
    parser.add_argument('--org_id', help="OU1 ID", required=True)
    parser.add_argument('--org_name', help="OU1 Name", required=True)
    parser.add_argument('--org2_id', help="OU2 ID")
    parser.add_argument('--org2_name', help="OU2 Name")
    return parser

def main():
    parser = setup_args()
    args = parser.parse_args()

    if args.compare and (args.org2_id is None or args.org2_name is None):
        parser.error("--compare requires --org2_id and --org2_name")

    first_org_id = args.org_id
    first_org_name = args.org_name

    if args.org2_id:
        second_org_id = args.org2_id
    if args.org2_name:
        second_org_name = args.org2_name

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    policies = get_resolved_policies_by_ou(creds, first_org_id)
    
    if (args.compare):
        #if --compare then get second OU policies and print differences
        second_policies = get_resolved_policies_by_ou(creds, second_org_id)
        diff_orgs(policies, first_org_name, second_policies, second_org_name)
    else:
        #no --compare so only print policies from first OU
        print_policies(policies, first_org_name)

if __name__ == '__main__':
    main()
