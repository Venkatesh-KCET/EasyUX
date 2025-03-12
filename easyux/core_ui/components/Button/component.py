from base_component import BaseComponent

class ButtonComponent(BaseComponent):
    name = "button"
    template_path = "coreui/components/Button/template.html"
    css_path = "coreui/components/Button/style.css"
    js_path = "coreui/components/Button/script.js"

    props = {
        "label": "Click Me",
        "color": "primary",   # Bootstrap-style: primary, danger, etc.
        "size": "md",         # sm, md, lg
        "type": "button",     # submit, reset, button
        "icon": None,
        "id": "",
        "class": "",
        "onclick": "",
    }

    def get_context_data(self):
        return {
            "props": self.attributes,
            "slots": self.slots,
        }

    def before_render(self):
        classes = [
            "coreui-btn",
            f"coreui-btn-{self.attributes.get('color', 'primary')}",
            f"coreui-btn-{self.attributes.get('size', 'md')}",
            self.attributes.get("class", "")
        ]
        self.attributes["class"] = " ".join(filter(None, classes))
        if self.attributes.get("onclick"):
            self.attributes["x-on:click"] = self.attributes["onclick"]
