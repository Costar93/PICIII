import requests

def get_data():
    for a in ["posts", "comments", "albums", "photos", "todos", "users"]:
        s = []
        s = requests.get("http://jsonplaceholder.typicode.com/%s/" % (a))
        if s.status_code != 200:
            raise Exception('POST /posts/ %s' % (r.status_code))
        r = s.json()
        for x in range(0, 5):
            print r[x],"\n"

get_data()
