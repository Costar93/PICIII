import requests
import sys

user_id=sys.argv[1]
id1=sys.argv[2]
title=sys.argv[3]
body=sys.argv[4]
data = {
    "userId": user_id,
    "id": id1,
    "title": title,
    "body": body
        }

def post_data(data):
    s = requests.post("http://jsonplaceholder.typicode.com/posts/", data=data)
    if s.status_code != 201:
        raise Exception('POST /posts/ %s' % (s.status_code))
    print "created task .ID: %s" % (s.json()["id"])

post_data(data)
