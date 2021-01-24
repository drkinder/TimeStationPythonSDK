

class Reports:

    def __init__(self, client):
        self.client = client
        self.url = self.client.options.get('base_url')
