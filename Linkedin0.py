# -*- coding: utf-8 -*-

#Reading Oauth file from the ../auth/in_auth file
from linkedin import linkedin
import json 

credentials='../auth/In_auth'#add your authentication data 
f=open(credentials,'r')
keys=f.readlines()
f.close()
#Read credentials keys
CONSUMER_KEY=keys[0].strip()
CONSUMER_SECRET=keys[1].strip()
USER_TOKEN=keys[2].strip()
USER_SECRET=keys[3].strip()
RETURN_URL=''
#authorizaton object
auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET, RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())

app=linkedin.LinkedInApplication(auth)
app.get_profile()
# for Oauth2 print auth.authorization_url

#store data in file 
connections=app.get_connections()
connections_data='../Dev.0.0/data/In_raw'

f2=open(connections_data,'w')
f2.write(json.dumps(connections,indent=1))
f2.close()

#have the connections info in a JSON, use prettytable to show name,location
from prettytable import PrettyTable # pip install prettytable
pt = PrettyTable(field_names=['Name', 'Location'])
pt.align = 'l'
[ pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name']))
for c in connections['values']
if c.has_key('location')]
print pt
print connections[0].keys

pretty_data='../Dev.0.0/data/pretty_In'
f3=open(pretty_data,'w')
f3.write('Connections of:' + str(app.get_profile()['firstName'])+'\n\n')
f3.write(str(pt))
f3.close()
