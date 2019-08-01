import json,urllib.request,time,replit
replit.clear()
print('\033[1;32m==============================\n')
print('\n\n\n==============================')
print('\033[1;34mLooks like you haven\'t typed in a number on the scratch project...')
print('\n\n\n\n\n\n\n\n\n'+'\033[35mHosted on repl.it\nDNS Forwarding by freedns.afraid.org')
#modified from https://scratch.mit.edu/discuss/topic/305427/?page=1#post-3225735
url = "https://clouddata.scratch.mit.edu/logs?projectid=322674932&limit=10000&offset=0"
changes=[]
x=0
replit.clear()
while True:
  time.sleep(0.1)
  clouddata = urllib.request.urlopen(url).read()
  clouddata = json.loads(clouddata)
  for i in clouddata:
    if i not in changes:
      if x==1: 
        replit.clear()#
        print('\033[1;32m==============================\n')
        print(str(i['value'])+'\n\n=============================='+'\n\n\n\n\n\n\n\n\n\n'+'\033[35mHosted on repl.it\nDNS Forwarding by freedns.afraid.org')#
        #add whatever code you want here
      changes.append(i)
  x=1
