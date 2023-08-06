class KpiClientException (Exception):
    def __init__(self, httpStatusCode, message):
        self.httpStatusCode = httpStatusCode
        self.message = message
    def __str__(self):
        return self.message
