
aog
===

A simple and easy to use python client library for Actions on google webhook.



Installation
============

Fast install:

```
pip install aog
```



Example
=======

```python
import json
import os
from flask import Flask
from flask import request
from flask import make_response
from aog import conv

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/', methods=['POST'])
def fullfillment():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeFullfillment(req)
    res = json.dumps(res, indent=4)
    #print(res)
    final = make_response(res)
    final.headers['Content-Type'] = 'application/json'
    return final

def makeFullfillment(req):
  # Wrte your python code here
  #isfrom function is used to check from which dialogflow intent request came from.
  if conv.isfrom(req,'ask_intent'): 
    # ask method expect a reply from user. after the message mic will be open for user to reply.
    res=conv.ask("You made me ask this","You made me print this")
    return res
      # F I N A L  R E S P O N S E
  if conv.isfrom(req,'final response'):
    
    # Close is for terminating the conversation with a message.
    res=conv.close('Closing')
    return res


```    
   