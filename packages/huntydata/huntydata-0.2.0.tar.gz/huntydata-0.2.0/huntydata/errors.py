
class Errors(Exception):
    """Still an exception raised when uncommon things happen"""
    def __init__(self, method, payload):
        self.message = f"[Error] -  With the Function:{method}"
        self.payload = payload

    def __str__(self):
        return str({'message':self.message,"payload":self.payload})










