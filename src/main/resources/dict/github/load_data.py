#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
from github import Github

base_url = ci['base_url']
username = ci['username']
password = ci['password']
organization = ci['organization']  # 'xld-petclinic-docker'
repository = ci['repository']  # 'xld-petclinic-docker'
branch = ci['branch']
path = ci['path']  # 'dar/config/log4j.properties'


# First create a Github instance:
print "open a connection to github using the '%s' username" % username
g = Github(username, password, base_url)
print "get '%s' repository" % repository
if organization != "":
    repo = g.get_organization(organization).get_repo(repository)
else:
    repo = g.get_user().get_repo(repository)

print "get content of '%s' in '%s' branch " % (path, branch)
contents = repo.get_contents(path, branch)
# print "decoded_content", contents.decoded_content

for line in contents.decoded_content.split('\n'):
    line = line.rstrip()  # removes trailing whitespace and '\n' chars

    if "=" not in line: continue  # skips blanks and comments w/o =
    if line.startswith("#"): continue  # skips comments which contain =

    k, v = line.split("=", 1)
    entries[k] = v

# print entries
