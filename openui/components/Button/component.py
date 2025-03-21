from django.conf import settings
from django.template import TemplateSyntaxError, Template

import os

def render():
    file_path = os.path.join(settings.BASE_DIR, "openui", "components", "Button", "template.html")

    if not os.path.exists(file_path):
        raise TemplateSyntaxError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        template_code = f.read()
    
    return template_code