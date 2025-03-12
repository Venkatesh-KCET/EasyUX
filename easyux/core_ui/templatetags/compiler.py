import re
from django.utils.html import escape

DJ_PREFIX = "dj-"

def dls_to_coreui_template(template_str):
    """
    Convert custom DLS-style tags like:
    <dj-button label="Click Me" theme="primary" />
    
    Into:
    {% CoreUI "Button" label="Click Me" theme="primary" %}{% endCoreUI %}
    """

    def dls_tag_replacer(match):
        full_tag = match.group(0)
        tag_name = match.group(1)
        attrs = match.group(2) or ""
        is_self_closing = full_tag.endswith("/>")

        # Convert dash-case to PascalCase (e.g., dj-button -> Button)
        component_name = tag_name.replace(DJ_PREFIX, "").replace("-", " ").title().replace(" ", "")

        # Extract props
        props = re.findall(r'(\w+)=["\']([^"\']+)["\']', attrs)
        props_str = " ".join([f'{key}="{escape(value)}"' for key, value in props])

        open_tag = f'{{% CoreUI "{component_name}" {props_str} %}}'

        if is_self_closing:
            return f"{open_tag}{{% endCoreUI %}}"
        else:
            return open_tag

    # Match DLS-style opening/self-closing tags
    pattern_open = re.compile(r'<(dj-[\w-]+)([^>/]*?)(/?)>', re.IGNORECASE)

    # Match DLS-style closing tags: </dj-button>
    pattern_close = re.compile(r'</(dj-[\w-]+)>', re.IGNORECASE)

    # Replace <dj-button ... />
    template_str = re.sub(pattern_open, dls_tag_replacer, template_str)

    # Replace </dj-button> with {% endCoreUI %}
    template_str = re.sub(pattern_close, '{% endCoreUI %}', template_str)

    return template_str
