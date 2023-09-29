# bt_fa_api

Register at http://188.120.244.199/
After that, log in.

Click the get token button.
Send the received token to the telegram bot
https://t.me/factory_t_bot

Enter your message in the message form and send it.
The bot should write you a message:
{Username}, I received a message from you:
{Message}

To work via API


**POST**
To register: http://188.120.244.199/api/v1/register/
```json
{
  "name": "<your_name>",
  "login": "<your_login>",
  "password": "<your_password>"
}
```



**POST**
For login: http://188.120.244.199/api/v1/login/.
Returns a login token.
```json
{
  "login": "<your_login>",
  "password": "<your_password>"
}
```

**GET**
To receive a token for bot: http://188.120.244.199/api/v1/token/
Authorization occurs using the header: Authorization Token <your token from login>
```json
{
  "token": "<your_token>",
  "user": <your_id>
}
```


**POST**
To send a message: http://188.120.244.199/api/v1/message/
```json
{
  "mesage": "<your_mesage>"
}
```

