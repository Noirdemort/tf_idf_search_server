import requests
import time
import random
import string
from tqdm import tqdm

start = time.time()

count=0
for _ in tqdm(range(10000)):
    letters = string.ascii_lowercase
    v = ''.join(random.choice(letters) for i in range(random.randint(7,9)))
    r = requests.post('http://localhost:5000/login', json={"hey": "{}".format(v)})
    #if r.json:
    count+=1
print(time.time()-start)
print(count)
'''count=0
start = time.time()
for _ in tqdm(range(10000)):
    letters = string.ascii_lowercase
    v = "".join(random.choice(letters) for i in range(random.randint(7,9)))
    s = requests.post("http://localhost:8000/login", json={"hey":"{}".format(v)})
    if s.json:
        count+=1
print(time.time()-start)
print(count)'''
