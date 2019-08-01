import json,urllib.request,time

#modified from https://scratch.mit.edu/discuss/topic/305427/?page=1#post-3225735

url = "https://clouddata.scratch.mit.edu/logs?projectid=	◯  &limit=10000&offset=0"#replace the circle and surrounding
#                                                                                    spaces with your project id

changes=[]
x=0

while True:
  time.sleep(0.1)
  clouddata = urllib.request.urlopen(url).read()
  clouddata = json.loads(clouddata)
  for i in clouddata:
    if i not in changes:
      if x==1: 
        
        print(i['value'])# prints the contents of the variable when it is updated
        #add whatever code you want here
        #add whatever code you want here
      changes.append(i)
  x=1
