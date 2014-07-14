#Extending Linkedin0.py to allow access by any user
#Reading Oauth file from the ../auth/in_auth file
from linkedin import linkedin
import json
import oauth2 as oauth#sudo pip
import urlparse 
 
credentials='../auth/In_auth'#add your authentication data 
f=open(credentials,'r')
keys=f.readlines()
f.close()
 
#Read credentials keys
API_KEY=keys[0].strip()
API_SECRET=keys[1].strip()

#For production environments
#RETURN_URL = 'http://localhost:8000'
#authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
#print authentication.authorization_url  # open this url on your browser
#application = linkedin.LinkedInApplication(authentication)
#
#f=open('../auth/oauth','r')
#oauth_code=f.read().strip()
#f.close()
#oauth_code=''
#authentication.authorization_code = oauth_code
#authentication.get_access_token()


#for quick checking: Logout of Linkedin and copy inthe url u get on screen. After you authenticate
#your account, it will carry forward
from linkedin import server
application = server.quick_api(API_KEY, API_SECRET)
application.get_profile()

#
app=application

#store data in file 
connections=app.get_connections()
connections_data='../Dev.0.0/data/In_new_raw'

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

pretty_data='../Dev.0.0/data/pretty_In_new'
f3=open(pretty_data,'w')
f3.write('Connections of:' + str(app.get_profile()['firstName'])+'\n\n')
f3.write(str(pt))
f3.close()

#extend the same to show




