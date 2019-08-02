import json,urllib.request,time,replit
replit.clear()

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890><|,;.:-_#\'+~*°^!"§$%&/()=?\{}[]@ '
charcodes='010203040506070809101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596'

charlist=[charcodes[q:q+2] for q in range(0, len(charcodes), 2)]# https://stackoverflow.com/questions/9475241/split-string-every-nth-character

def decode(x):
  n=[x[f:f+2] for f in range(0, len(x), 2)]#https://stackoverflow.com/questions/9475241/split-string-every-nth-character

  global chars,charlist
  decoded=''

  for i in range (len(n)):
    for j in range(96):
      if n[i]==charlist[j]:
        decoded+=chars[j]

  return decoded

print('\033[1;32m==============================\n')
print('\n\n\n==============================')
print('\033[1;34mLooks like you haven\'t typed in a message on the scratch project yet...')
print('\n\n\n\n\n\n\n\n\n'+'\033[35mHosted on repl.it\nDNS Forwarding by freedns.afraid.org')
#modified from https://scratch.mit.edu/discuss/topic/305427/?page=1#post-3225735

url = "https://clouddata.scratch.mit.edu/logs?projectid=322674932&limit=10000&offset=0"
changes=[]
x=0
replit.clear()

while True:
  time.sleep(0.1)
  clouddata = urllib.request.urlopen(url).read()#sends the request
  clouddata = json.loads(clouddata)#turns it into a dictionary

  for i in clouddata:
    if i not in changes:
      if x==1: 
        replit.clear()# clears console
        print('\033[1;32m==============================\n')
        print(str(decode(i['value']))+'\n\n=============================='+'\n\n\n\n\n\n\n\n\n\n'+'\033[35mHosted on repl.it\nDNS Forwarding by freedns.afraid.org')
        #add whatever code you want here
      changes.append(i)
  x=1
