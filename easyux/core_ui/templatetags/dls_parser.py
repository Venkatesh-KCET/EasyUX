# coreui/templatetags/dls_parser.py

import re

def convert_dls_to_coreui(html):
    pattern = r'<dj-(\w+)([^>]*)\/?>'
    def replacer(match):
        tag = match.group(1)
        attrs = match.group(2)
        props = ""
        for attr in re.findall(r'(\w+)=["\']([^"\']+)["\']', attrs):
            props += f'{attr[0]}="{attr[1]}" '
        return f'{{% CoreUI "{tag.capitalize()}" {props.strip()} %}}{{% endCoreUI %}}'
    return re.sub(pattern, replacer, html)
