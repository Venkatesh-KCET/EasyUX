from django import template
from coreui_django_component.components.button import Button  # Example import

register = template.Library()

@register.simple_tag
def render_button(label="Click Me", style="primary"):
    # button = Button(label=label, style=style)
    return "<h1>asadasd</h1>"