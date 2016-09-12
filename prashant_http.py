
import requests
import time
import json
import sys

def read_file():
    '''
    reads file for urls
    :return:
    '''
    latency_list = []
    with open ('urlrepo.txt','r') as urlfd:
        for url in urlfd:
            latency_list.append({'url':url.rstrip(),'latency_ms':round(send_get(url.rstrip())*100,2)})
    jfile = make_json(latency_list)
    return jfile

def write_file(jstr):
    '''
    appends to a json file
    :param jstr:
    :return:
    '''
    with open ('urllatency.json','a') as jfd:
    #with open ("urllatency.json"."w") as jfd: # uncomment to write instead of appending
        jfd.write(jstr)

def send_get(url):
    '''
    send get request and waits for response
    :param queried URL: URL as in http:// ....
    :return:a get request response
    '''
    headers = {'user-agent':'my_app/0.0.1'}

    try:
        start_time = time.clock()
        #print 1,url
        response = requests.get(url)
        #print 2,response
        if response.status_code != 200: # if not a successful response then forget the shit
            return 10000 #and return 0
        end_time = time.clock()
        latency = measure_time(start_time,end_time)
    except:
        e = sys.exc_info()[0]
        #raise
        print "unsuccessful attempt. Just don't laze around, do something about the exception %s" %e
        latency = 10000

    return latency

def measure_time(start_time,end_time):
    '''
    measure latency
    :param start time of request, end time of request:
    :return: latency
    '''
    return (end_time - start_time)

def make_json(jdict):
    '''
    :param jdict: a python obj (dictionary with url and corresponding response times)
    :return: json string
    '''
    return json.dumps(jdict)

def read_json(jstring):
    '''
    accepts
    :param jstring:  json string
    :return: python object
    '''
    return json.loads(jstring)

js = read_file()  # prints the final json
print js
print read_json(js)
write_file(js)
