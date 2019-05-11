"""Custom response type for REST requests"""
import json
from typing import List, Any

class Response:
    """Generates a custom object with overloaded getattr method to handle jsons"""

    def __init__(self, resp: dict, throw: bool = True):
        """
        Generates a response object from a dictionary response
        resp -> object to get attributes from
        throw -> read __getattr__ method for information on throw
        """
        self.obj = resp
        self.throw = throw

    def __get_value(self, name) -> ("Response", "Primitive types", KeyError, None):
        """
        Gets value with key <name> from self.obj, throws a KeyError if <name> is not in self.obj
        """
        return self.obj[name] if \
            not isinstance(self.obj[name], dict) else Response(self.obj[name])

    def __getattr__(self, name: str) -> ("Response", "Primitive types", KeyError, None):
        """
        Gets attribute from self.obj
        if throw is set to True it will throw a KeyError if <name> is not in self.obj
        if throw is set to False it will return a NoneType if <name> is not in self.obj
        """
        if self.throw:
            return self.__get_value(name)
        return self.__get_value(name) if name in self.obj else None

    def index(self, index_num: int) -> (List[Any], "Response", IndexError):
        """
        Returns a possible List of any type, or a Response object, from index <index_num>.
        Throws IndexError if out of range.
        """
        if isinstance(self.obj[index_num], list):
            return self.obj[index_num]
        elif isinstance(self.obj[index_num], dict):
            return Response(self.obj[index_num])

    def __str__(self) -> str:
        """
        Returns a json.dump() from self.obj
        """
        return json.dumps(self.obj)

    def __repr__(self):
        """
        String representation in format:
        <Response at {address} length={keycount}>
        """
        return f"<Response at {hex(id(self))} length={len(self.obj)}>"

    def __len__(self):
        """
        Returns length of self.obj
        """
        return len(self.obj)


if __name__ == '__main__':
    import requests
    RESPONSE = Response(requests.get(
        "http://api.github.com/users/Yuhanun/events/public").json())
    print(RESPONSE)
    print(RESPONSE.index(0))
