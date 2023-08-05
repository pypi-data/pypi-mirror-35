import os

import yaml


class API:
    ID = 'NotImplemented'

    def __init__(self, config):
        path = os.path.dirname(os.path.abspath(__file__))
        self.key_id, self.key_secret = None, None
        if not config:
            config = "config.yaml"
        
        try:
            with open(os.path.join(path, config), 'r') as fp:
                data = yaml.load(fp)
                self.key_id = data[self.ID.lower()]['key_id']
                self.key_secret = data[self.ID.lower()]['key_secret']
        except:
            pass