import requests

user = "AndrewSC208"
word = "Birdie215"

r = requests.get('https://api.github.com', auth=('user', 'word'))

print r.status_code
print r.headers['content-type']