class BaseComponent:
    name = "base"
    props = {}
    slots = []
    template_path = ""
    css_path = ""
    js_path = ""

    def __init__(self, **kwargs):
        self.attributes = {**self.get_default_props(), **kwargs}
        self.slots = {}

    def get_default_props(self):
        return self.props

    def render(self, context=None):
        # Load template, inject props, manage slots
        # Call hooks before/after
        pass
