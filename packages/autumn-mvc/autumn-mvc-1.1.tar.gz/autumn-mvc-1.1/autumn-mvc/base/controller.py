import pickle


class content_type:
    html = 1
    json = 2
    string = 3


class controller:
    def __init__(self):
        self.config = {}
        self.request = None
        self.response = None

    def html(self, input):
        return {
            "template": input,
            "type": content_type.html
        }

    def view(self):
        path = self.config["view"]["path"] # NOQA
        action = self.request.router.action # NOQA
        suffix = self.config["view"]["suffix"] # NOQA
        file = "{path}/{action}.{suffix}".format(**locals())
        template = None 
        with open(file, 'r') as f:
            template = f.read()
        return self.html(template)

    def json(self, input):
        return {
            "template": str(pickle.dumps(input)),
            "type": content_type.json
        }

    def assign(self, key, value):
        if not hasattr(self.response, "views"):
            self.response.views = {}
        self.response.views[key] = value

    @property
    def cookie(self):
        return self.response.cookie

    @property
    def session(self):
        return self.response.session
