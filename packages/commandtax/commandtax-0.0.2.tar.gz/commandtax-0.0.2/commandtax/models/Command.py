from apitaxcore.models.Options import Options
from apitaxcore.flow.requests.ApitaxRequest import ApitaxRequest
from apitaxcore.models.Credentials import Credentials


class Command:
    def __init__(self, command: list = None, request: ApitaxRequest = ApitaxRequest(), parameters: dict = {},
                 options: Options = Options(), credentials: Credentials = Credentials()):
        self.command = command
        self.options = options
        self.request = request
        self.parameters = parameters
        self.credentials = credentials
