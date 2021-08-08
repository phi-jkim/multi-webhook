# multi-webhook 

This is an app created using flask that can serve as a webhook by tracking POST requests to a server. Everytime, webhook.py is run, data from an api or etc. is 
locally stored into the json file in the static directory. The content of this json file can be accessed by entering the address /webhook. 

To run the app locally, 
> flask run 

This will run the file run.py and start the server.
