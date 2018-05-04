import urllib2, json, base64
accesstoken = "98QTBXA28N6NUY36QY2M"
institution="10007772"
course= "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
    institution,
    course
    )
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
        )
response = urllib2.urlopen(request)
data = json.load(response)

'''print json.dumps(data,indent=2)'''

for c in data:
    if c['Code']=="SALARY":
       '''print c['Details']'''
       i=c['Details']
       for a in i:
           if(a['Code']=="MED"):
              print "Answer 1 is "+ str(a['Value'])
        
    
for c in data:
    if c['Code']=="SALARY":
       '''print c['Details']'''
       i=c['Details']
       for a in i:
           if(a['Code']=="LDMED"):
              print "Answer 2 is "+ str(a['Value'])


for c in data:
    if c['Code']=="NSS":
       '''print c['Details']'''
       i=c['Details']
       for a in i:
           if(a['Code']=="Q1"):
              print "Answer 3 is "+ str(a['Value'])
