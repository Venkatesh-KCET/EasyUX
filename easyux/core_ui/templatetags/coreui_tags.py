# coreui/templatetags/coreui_tags.py

from django import template
from django.template.loader import render_to_string
from coreui.engine.registry import ComponentRegistry
from coreui.engine.utils import parse_slots, parse_props

register = template.Library()

@register.tag(name="CoreUI")
def coreui_tag(parser, token):
    try:
        tokens = token.split_contents()
        tag_name = tokens[0]
        component_name = parser.compile_filter(tokens[1])
        kwargs = template.Token(token.contents.replace(tokens[0], "").strip()).kwargs
    except Exception as e:
        raise template.TemplateSyntaxError(f"Error parsing CoreUI tag: {e}")

    nodelist = parser.parse(('endCoreUI',))
    parser.delete_first_token()
    return CoreUIComponentNode(component_name, kwargs, nodelist)


class CoreUIComponentNode(template.Node):
    def __init__(self, component_name, kwargs, nodelist):
        self.component_name = component_name
        self.kwargs = kwargs
        self.nodelist = nodelist

    def render(self, context):
        name = self.component_name.resolve(context)
        resolved_kwargs = {k: v.resolve(context) for k, v in self.kwargs.items()}
        slots = parse_slots(self.nodelist, context)

        component_class = ComponentRegistry.get_instance().get(name)
        if not component_class:
            return f"<!-- CoreUI: Component '{name}' not found -->"

        try:
            component = component_class(**resolved_kwargs, slots=slots)
            component.before_render()
            output = component.render(context)
            component.after_render()
            return output
        except Exception as e:
            return f"<!-- CoreUI: Error rendering '{name}' — {e} -->"
