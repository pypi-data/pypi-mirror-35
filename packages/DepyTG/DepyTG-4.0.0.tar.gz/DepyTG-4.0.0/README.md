# DepyTG

The only Python3 Telegram bot library that does *nothing*.

### Wait, what?

Well of course it doesn't do *nothing* at all. However, it does nothing compared to many other Telegram bot libraries, and that's a design goal.

### Design goals

The main goal is to KISS — Keep It Simple, Stupid.

Other than being simple, DepyTG tries to:

 - Have a 1:1 correspondence with Telegram's official API specs. The only documentation you need is Telegram's.
 - Be compatible with any HTTP library you may want to use — Requests, Flask, JSON+Urllib, anything
 - Make sure 99.9999% of its objects are JSON-serializable
 - Provide a simple (but totally optional) API to do the network stuff
 - Heavily integrate with IDEs that support code insights by type-hinting everything that can be type-hinted
 - Not try to reinvent the wheel. Telegram's API is quite simple, we're not going to implement simplified "send_message" methods.
 
 
 # Big note
 
 This is a work in progress! I wrote this from scratch to write my own Telegram bots. I haven't tested it very much. I'll test it as I work on them. I'll write some tests and add CI soon.
 
 
 ### Quick intro
 
 ##### Creating an object
 
 - Manually
 
 ```python
 >>> types.Document(
        file_id='doc_id',
        file_name='ciao.pdf',
        thumb=PhotoSize(
                  file_id='thumb_id',
                  width=100, 
                  height=50
              )
     )
  Document({'file_id': 'doc_id', 'thumb': PhotoSize({'file_id': 'thumb_id', 'width': 100, 'height': 50}), 'file_name': 'ciao.pdf'})
 ```
 
 - From dict/JSON
 ```python
 >>> types.Document.from_json({'file_id': 'doc_id',
 'file_name': 'ciao.pdf', 'thumb': {'file_id': 'thumb_id', 'height': 50, 'width': 100}})
 Document({'file_id': 'doc_id', 'thumb': PhotoSize({'file_id': 'thumb_id', 'width': 100, 'height': 50}), 'file_name': 'ciao.pdf'})
 
# Notice how the type of "thumb" (PhotoSize) is automatically detected.
 ```
 
 #### Calling methods
 
 Methods are regular Python objects. "Call" them once to generate the parameters' dictionary, then twice (passing the API token) to actually send the request.
 
 - With the built-in API
 ```python
 #                     ↓ Pass fields here              ↓ Pass token here 
 >>> methods.setWebhook("https://my.super.webhook.com")("my_bot_token")
 True
 >>> methods.getWebhookInfo()("my_bot_token")
WebhookInfo({'url': 'https://my.super.webhook.com', 'has_custom_certificate': False, 'pending_update_count': 0})
 ```
 
 - With an external library
 ```python
 #   ↓ Store to variable        ↓ Only pass fields
 >>> method = methods.setWebhook("https://my.super.webhook.com")
 >>> r = requests.post("https://api.telegram.org/botmy_bot_token/setWebhook", json=method)
 >>> method.read_result(r.json())
 True
 
 >>> r = requests.get("https://api.telegram.org/botmy_bot_token/getWebhookInfo")
 #   ↓ "read_result" is specific for each method
 >>> methods.getWebhookInfo.read_result(r.json())
 WebhookInfo({'url': 'https://my.super.webhook.com', 'has_custom_certificate': False, 'pending_update_count': 0})
 ```
 
 ##### Note:
 Methods that take `InputFile` objects are a bit special. First of all, any field that takes `InputFile` is made optional, even if Telegram's API references says the opposite.
 
 `InputFile` is the only object that is not JSON-serializable and as such, it needs special handling. If you use a custom HTTP library, you will need to upload the files yourself as described in Telegram's documentation.
 
 The built-in requests API will handle `InputFile` objects automatically and send the fields as `multipart/form-data`. If `requests-toolbelt` is installed it will be used to stream the file.
 
 
 
 ### Possible questions
 
 ##### Why the hell did you define *every* possible object in the API?
 
 Because one of my goals was to have code completion.
 
 All Telegram API objects and methods are children of `TelegramObjectBase`, which is a subclass of `dict`. This means everything (except for `InputFile`) is JSON-serializable and can be used outside of this library.
 
 `dict` has been extended to check field types and to access them with the standard dot notation, so that IDEs like PyCharm can warn you if you do something wrong.
 
 The reason they were "rewritten" is to allow for type checking.