import os
from django.conf import settings
from django import template
from django.template import Node, TemplateSyntaxError, loader, Context, Template, TemplateSyntaxError

register = template.Library()

def load_component_from_file(component_name):
    # Define base components folder — can be absolute or relative
    base_path = os.path.join(settings.BASE_DIR, "openui", "components", component_name)

    # Build full file path
    file_path = os.path.join(base_path, "template.html")

    if not os.path.exists(file_path):
        raise TemplateSyntaxError(f"Component file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        template_code = f.read()

    return Template(template_code)  # ⬅️ Now you can render with Context()

class ComponentNode(Node):
    def __init__(self, component_name, kwargs, nodelist, slots):
        self.component_name = component_name
        self.kwargs = kwargs
        self.nodelist = nodelist
        self.slots = slots

    def render(self, context):
        component = self.component_name.resolve(context)
        props = {key: val.resolve(context) for key, val in self.kwargs.items()}

        # Prepare slot content
        rendered_slots = {}
        for slot_name, nodelist in self.slots.items():
            rendered_slots[slot_name] = nodelist.render(context)

        # Default slot
        if self.nodelist:
            rendered_slots["default"] = self.nodelist.render(context)

        # Inject slots into context
        render_context = Context({**props, "slots": rendered_slots}, autoescape=context.autoescape)

        print(render_context)

        try:
            tmpl = load_component_from_file(component)
        except Exception as e:
            raise TemplateSyntaxError(f"Component template 'openui/{component}/template.html' not found: {e}")

        return tmpl.render(render_context)


@register.tag("dj")
def do_dj(parser, token):
    tokens = token.split_contents()    
    tag_name = tokens[0]

    if len(tokens) < 2:
        raise TemplateSyntaxError(f'"{tag_name}" tag requires at least a component name.')

    component_name = parser.compile_filter(tokens[1])
    kwargs = {}

    for arg in tokens[2:]:
        if "=" not in arg:
            raise TemplateSyntaxError(f'Malformed argument "{arg}". Use key="value" format.')
        key, val = arg.split("=", 1)
        kwargs[key] = parser.compile_filter(val)

    nodelist = parser.parse(('enddj', 'slot'))
    slots = {}

    while True:
        token = parser.next_token()
        if token.contents == 'enddj':
            break
        elif token.contents.startswith('slot'):
            slot_name = token.split_contents()[1].strip('"')
            slot_nodelist = parser.parse(('endslot',))
            parser.delete_first_token()
            slots[slot_name] = slot_nodelist

    return ComponentNode(component_name, kwargs, nodelist, slots)


# Optional: Register slot/enddj as no-ops to avoid errors
@register.tag
def slot(parser, token):
    return template.Node()  # Placeholder: handled in main loop

@register.tag
def endslot(parser, token):
    return template.Node()

@register.tag
def enddj(parser, token):
    return template.Node()
