import requests

class TKEndPoint:
  def __init__(self, url, end_point):
    self.url = url + "/" + end_point
  
  def get(self, id=None):
    if id is None:
      return requests.get(self.url)
    else:
      return requests.get(self.url + "/" + id)
  
  def post(self, data):
    return requests.post(self.url, json=data)

  def put(self, data):
    return requests.put(self.url, json=data)

  def delete(self, id):
    return requests.delete(self.url + '/' + id)

class TKRest:
  def __init__(self, url):
    self.url = url
  
  def __getattr__(self, attr):
    return TKEndPoint(self.url, attr)

if __name__ == "__main__":
  t = TKRest("https://tk-lms.herokuapp.com/api")
  print(t.classrooms.get("5b6ecf5d956b8800271c2ec6").json())
