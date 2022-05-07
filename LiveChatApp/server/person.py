class Person:
    """
    Represents a person hold it's name socket cliend and ip address
    """
    def __int__(self, addr, name, client):
        self.addr = addr
        self.client = client
        self.name = None
    def setName(self, name):
        """
        sets person's name
        :param name: str
        :return: non
        """
        self.name = name
    def __repr__(self):
        return f"Person({self.addr}, {self.name})"

