import requests
res = requests.post('http://localhost:5000//api/v1/resources/books/save', json={"id":"234","title":"India","author":"Nehru","Year":1993})
if res.ok:
    print(res.json())
else:
    print("Request is failed")