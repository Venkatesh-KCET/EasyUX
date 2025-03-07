from django_viewcomponent import Component

class Button(Component):
    def __init__(self, text="Click Me", variant="primary", size="md"):
        self.text = text
        self.variant = variant
        self.size = size

    def context(self):
        return {
            "text": self.text,
            "variant": self.variant,
            "size": self.size,
        }
