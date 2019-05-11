# RESJect
Custom Python object for handling REST responses

## How to set this up ##
Simply download the following files:
```
RESTJect.py
```

Add it either to your sys.path, or move it to where you want to use it.

Usage:
```py
from RESTJect import Response
Response(requests.get("http://www.api.some_website.com/endpoint").json())
```

For example usage, check RESTJect.py

```py
if __name__ == '__main__':
    import requests
    RESPONSE = Response(requests.get(
        "http://api.github.com/users/Yuhanun/events/public").json())
    print(RESPONSE)
    print(RESPONSE.index(0))

```

## Feel free to pull request any changes / improvements you make :) ##

# License #
This project is licensed under the MIT License (yay, free code) - see the [LICENSE](https://github.com/Yuhanun/RESJect/blob/master/LICENSE) file for details

# Acknowledgments #
Thanks to Guido for creating the language :)

### Buy me a coffee ;) (BTC) ###
32dcJ31dsxj8BMD5oD3mWKTDFSzpFHuHP1
