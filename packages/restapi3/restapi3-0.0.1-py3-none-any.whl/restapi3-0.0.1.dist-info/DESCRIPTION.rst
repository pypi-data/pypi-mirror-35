# Formatted APIs presentation for testing
Can be used as part of RESTful API test framework

# Install
sudo pip3 install restapi3

# Usage
1. 'Get' : 'query_strings'
1. 'Post' : 'data', 'files', 'json'
1. 'Put' : 'data', 'json'
1. 'Delete'

```Python
from restapi3.api import BaseAPIs, API

class Video_Model(BaseAPIs):

  def __init__(self):
      BaseAPIs.__init__(self, "http://XXXX")
      self.headers = {'X-Device-ID': 'YA'}

  @API
  def get_video(self):
      return {
          'path': '/v1/A/C/X',
          'headers': self.headers,
          'method': 'Get',
          'query_strings': {
              'first_str': 'val space, yee',
              'second_str': 123
          },
          'json': {
              'a': 123,
              'b': ['123', '234']
          },
          'files': {
              'image': open('/Users/tedchen/Desktop/test.png', 'rb')
          }
      }


r = Video_Model().get_video() # Return for requests Response object

if r.status_code != 200:
   raise Exception("Fail to call API")
r_json = r.json()
```


