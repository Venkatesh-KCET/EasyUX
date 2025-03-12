# engine/utils/helpers.py

from django.template import Node, TemplateSyntaxError

def parse_slots(nodelist, context):
    """
    Parses slot content from a given nodelist.
    Currently returns default slot content; extend this
    to support named slots if necessary.
    """
    return {"default": nodelist.render(context)}

def parse_props(token):
    """
    Parses properties from a token string.
    Expected format: key="value" pairs.
    Returns a dict of prop keys and values.
    """
    try:
        bits = token.split()
        props = {}
        for bit in bits[1:]:
            if '=' in bit:
                key, value = bit.split('=', 1)
                # Remove quotes from the value
                props[key] = value.strip('"').strip("'")
        return props
    except Exception as e:
        raise TemplateSyntaxError(f"Error parsing props: {e}")
