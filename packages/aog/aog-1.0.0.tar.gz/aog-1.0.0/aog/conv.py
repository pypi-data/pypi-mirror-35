#Created by Bibin benny 
#bibinbenny@icloud.com


#Custom Errorrs

class ValueMissing(Exception):
	pass

class ValueNotFound(Exception):
	pass

class indexErr(Exception):
	pass

def isfrom(req=None,intent=None):
	
	if req is None:
		raise ValueMissing('req and intent can not be empty')
	if intent is None:
		raise ValueMissing('req and intent can not be empty')
	string=req.get("queryResult").get("intent").get("displayName")
	if string == intent:
		return True
	else:
		return False


def ask(speech=None,displayText=None):

	if displayText is None:
			displayText=speech
	if speech is None:
			raise ValueMissing('speech can not be empty')

	return  {
				"payload": {
				"google": {
				"expectUserResponse": True,
				"richResponse": {
				"items": [
				{
				"simpleResponse":
				{
				"textToSpeech": speech,
				"displayText":displayText 
				}
				}
				]
				} 

				}
				}


				}



def close(speech=None):


	if speech is None:
			raise ValueMissing('speech can not be empty')

	return  {
  "payload": {
    "google": {
      "expectUserResponse": False,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": speech
            }
          }
        ]
      }
    }
  }
}



# B A S I C  C A R D 

def basic_card(speech=None,title=None,formatted_text=None,subtitle=None,card_image=None,image_scale=None,image_text=None,link_title=None,link_url=None,response=True):

	if speech is None:
		raise ValueMissing("Speech can not be empty")
	if (card_image and formatted_text is None):
		raise ValueMissing("Either Fomrmatted  text or Image Url should be used")
	if title is None:
		print("title should not be empty")


	#return None
	if image_scale is None:
		image_scale="CROPPED"
	return {
		"payload": {
		"google": {
		"expectUserResponse": response,


		"richResponse": {
		"items": [
		{
		"simpleResponse": {
		"textToSpeech": speech
		}
		},
		{
		"basicCard": {
		"title": title,
		"subtitle":subtitle,
		"formattedText": formatted_text,
		"image": {
		"url": card_image,
		"accessibilityText": "Image"
		},
		"buttons": [
		{
		"title": link_title,
		"openUrlAction": {
		"url": link_url
		}
		}
		],
		"imageDisplayOptions": image_scale
		}
		}
		]

		}
		}


		}
		}


def list(title=None,speech=None,items=None):
	if len(items) < 2:
		raise indexErr("at least two items should be present") 
	if items is None:
		raise ValueMissing("Items can not be empty")
	if speech is None:
		raise ValueMissing("speech can not be empty")
	temps=[]
	for i in items:
		temps.append({"optionInfo":{"key":i.get('key'),"synonyms":i.get('synonyms')},"title":i.get('title'),\
				"description":i.get('description'),"image":{"url":i.get('image_url'),\
				"accessibilityText":i.get('image_text')}})
		if i.get('title') is None:
			raise ValueMissing("title can not be emtpy (item{})".format(i))
		if i.get('key') is None:
			raise ValueMissing("key can not be empty ( item{})".format(i) )

	return{
			"payload": {
			"google": {
			"expectUserResponse": True,
			"richResponse": {
			"items": [
			{
			"simpleResponse": {
			"textToSpeech": speech
			}
			}
			]
			},
			"systemIntent": {
			"intent": "actions.intent.OPTION",
			"data": {
			"@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
			"listSelect": {
			"title": title, 
			"items":temps
			}
			}
			}
			}
			}
			}


def carousels(title=None,speech=None,items=None):
	if len(items) < 2:
		raise indexErr("at least two items should be present") 
	if items is None:
		raise ValueMissing("Items can not be empty")
	if speech is None:
		raise ValueMissing("speech can not be empty")
	temps=[]
	for i in items:
		temps.append({"optionInfo":{"key":i.get('key'),"synonyms":i.get('synonyms')},"title":i.get('title'),\
				"description":i.get('description'),"image":{"url":i.get('image_url'),\
				"accessibilityText":i.get('image_text')}})
		if i.get('title') is None:
			raise ValueMissing("title can not be emtpy (item{})".format(i))
		if i.get('key') is None:
			raise ValueMissing("key can not be empty ( item{})".format(i) )

	return{
			"payload": {
			"google": {
			"expectUserResponse": True,
			"richResponse": {
			"items": [
			{
			"simpleResponse": {
			"textToSpeech": speech
			}
			}
			]
			},
			"systemIntent": {
			"intent": "actions.intent.OPTION",
			"data": {
			"@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
			"carouselSelect": {
			"title": title, 
			"items":temps
			}
			}
			}
			}
			}
			}

def list_item_selectd(req):
	key=req.get("originalDetectIntentRequest").get("payload").get("inputs")[0].get('arguments')[0].get("textValue")
	return(key)


def get_parameters(req,name=None):
	if name is None:
		raise ValueMissing("name of the entity is requred")
	param=req.get("queryResult").get("parameters").get(name)
	if param is None:
		raise ValueNotFound("parameter with name {} is not found".format(name))
	return param


def ask_permission(permissions=None,context=None):

  if permissions is None:
  	raise ValueMissing("at least one permission is required")	
  return {
  "payload": {
  "google": {
  "expectUserResponse": True,
  "richResponse": {
  "items": [
  {
  "simpleResponse": {
  "textToSpeech": "placeholder"
  }
  }
  ]
  },
  "systemIntent": {
  "intent": "actions.intent.PERMISSION",
  "data": {
  "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec",
  "optContext": context,
  "permissions":permissions

  }
  }
  }
  }


  }

def permission_granted(req):

  for i in range (0,4):
    temp=req.get("queryResult").get("outputContexts")[i]
    if "parameters" in temp:
      if req.get("queryResult").get("outputContexts")[i].get("parameters").get("PERMISSION") == True:
        value= True
      elif req.get("queryResult").get("outputContexts")[i].get("parameters").get("PERMISSION") == False:
        value= False
  return value


def get_username(req):
	name=req.get("originalDetectIntentRequest").get("payload").get("user").get("profile")
	if name is None:
		raise ValueNotFound("Name parameeter not found. make sure you have requested for this permission using ask_permission(NAME)")
	return name 


def get_userlocation(req):
	location=lat=req.get("originalDetectIntentRequest").get("payload").get("device").get("location").get("coordinates")
	if location is None:
		raise ValueNotFound("Name parameeter not found. make sure you have requested for this permission using ask_permission(NAME)")
	return location



def ask_datetime(initial=None,date=None,time=None):
	if initial is None:
		initial="When do you want to come in?"
	if date is None:
		date="What is the best date to schedule your appointment?"
	if time is None:
		time="What time of day works best for you?"

	return {
  "payload": {
  "google": {
  "expectUserResponse": True,
  "richResponse": {
  "items": [
  {
  "simpleResponse": {
  "textToSpeech": "placeholder"
  }
  }
  ]
  },
  "systemIntent": {
  "intent": "actions.intent.DATETIME",
          "data": {
            "@type": "type.googleapis.com/google.actions.v2.DateTimeValueSpec",
            "dialogSpec": {
              "requestDatetimeText": initial,
              "requestDateText": date,
              "requestTimeText": time

  }
  }
  }
  }


  }
  }

def get_datetime(req):
  	date=req.get("originalDetectIntentRequest").get("payload").get("inputs")[0].get('arguments')[0].get("datetimeValue").get("date")
  	time=req.get("originalDetectIntentRequest").get("payload").get("inputs")[0].get('arguments')[0].get("datetimeValue").get("time")
  	if date is None:
  		raise ValueNotFound("Date is not found. make sure you have asked date permission using 'ask_datetime()'")
  	if time is None:
  		raise ValueNotFound("Date is not found. make sure you have asked date permission using 'ask_datetime()'")
  	
  	return date,time




def ask_signin():
	return {
  "payload": {
  "google": {
  "expectUserResponse": True,
  "richResponse": {
  "items": [
  {
  "simpleResponse": {
  "textToSpeech": "PLACEHOLDER_FOR_SIGN_IN"
  }
  }
  ]
  },
  "systemIntent": {
  "intent": "actions.intent.SIGN_IN",
  "inputValueData": {}
          
  }
  }
  }
  }


  
def suggestion_chips(speech=None,displayText=None,suggestions=None):
  if suggestions is None:
    raise ValueMissing("Suggestions can not be empty")
  lists=[]
  for i in suggestions:
    lists.append({"title":i}) 
  return  {
    "payload": {
    "google": {
      "expectUserResponse": True,
      "richResponse": {
         "items": [
            {
              "simpleResponse":
              {
                "textToSpeech": speech,
                "displayText":displayText 
              }
                }
                  ],
                  "suggestions": lists,
              } 

              }
                }


              }





def ask_confirmation(speech):

	return {
  "payload": {
  "google": {
  "expectUserResponse": True,
  "richResponse": {
  "items": [
  {
  "simpleResponse": {
  "textToSpeech": "placeholder"
  }
  }
  ]
  },
  "systemIntent": {
  "intent": "actions.intent.CONFIRMATION",
          "data": {
            "@type": "type.googleapis.com/google.actions.v2.ConfirmationValueSpec",
            "dialogSpec": {
              "requestConfirmationText": speech

  }
  }
  }
  }


  }
  }


def get_confirmation(req):
	arguments=req.get("originalDetectIntentRequest").get("payload").get("inputs")[0].get('arguments')
	conf=None
	for i in arguments:
		print(i.get('name'))
		if i.get('name') == 'CONFIRMATION':
			conf=i.get('boolValue')
			print(conf)
	if conf is None:
		raise ValueNotFound("Confirmation value is not found. make sure you have asked for confirmation using using 'ask_confirmation()")
	return conf


def has_capability(req,capability):
	data=req.get("originalDetectIntentRequest").get("payload").get("surface").get('capabilities')
	flag=False
	for i in data:
		if i.get('name') == capability:
			flag=True
	return flag


def get_userid(req):
	req.get("payload").get("google").append(value)
	return req

def get_lastseen(req):
	user=req.get("originalDetectIntentRequest").get("payload").get("user")
	if 'lastSeen' in user:
		return user['lastSeen']
	else:
		return None
def get_userid(req):
	user_id=req.get("originalDetectIntentRequest").get("payload").get("user").get('userId')
	return user_id




