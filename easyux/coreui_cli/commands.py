#!/usr/bin/env python
# coreui_cli/commands.py

"""
CLI tool for django-coreui.
Provides a command to scaffold a new component.
"""

import os
import sys
import json
import click
from pathlib import Path

BASE_COMPONENT_TEMPLATE = """from base_component import BaseComponent

class {component_class}(BaseComponent):
    name = "{component_name}"
    template_path = "coreui/components/{component_class}/template.html"
    css_path = "coreui/components/{component_class}/style.css"
    js_path = "coreui/components/{component_class}/script.js"

    props = {
        "label": "Click Me",
        "color": "primary",  # e.g., primary, danger
        "size": "md",        # sm, md, lg
        "type": "button",    # submit, reset, button
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
"""

TEMPLATE_HTML = """<button
    type="{{ props.type }}"
    id="{{ props.id }}"
    class="{{ props.class }}"
>
    {% if props.icon %}
        <i class="{{ props.icon }}"></i>
    {% endif %}
    {{ props.label }}
    {% if slots.default %}
        {{ slots.default }}
    {% endif %}
</button>
"""

STYLE_CSS = """/* Style for {component_class} component */
.coreui-btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background-color 0.2s ease;
}}
.coreui-btn-primary {{
    background-color: #3b82f6;
    color: #fff;
}}
"""

SCRIPT_JS = """// JavaScript for {component_class} component
document.addEventListener('DOMContentLoaded', () => {{
    console.log('{component_class} component loaded.');
}});
"""

META_JSON = """{{
  "name": "{component_name}",
  "version": "1.0.0",
  "description": "A reusable {component_name} component.",
  "props": {{
    "label": {{
      "type": "string",
      "default": "Click Me",
      "description": "Button text"
    }},
    "color": {{
      "type": "string",
      "default": "primary",
      "description": "Color theme (primary, danger, etc.)"
    }},
    "size": {{
      "type": "string",
      "default": "md",
      "description": "Size of the button (sm, md, lg)"
    }},
    "type": {{
      "type": "string",
      "default": "button",
      "description": "HTML button type"
    }},
    "icon": {{
      "type": "string",
      "default": null,
      "description": "Optional icon class"
    }},
    "id": {{
      "type": "string",
      "default": "",
      "description": "HTML id attribute"
    }},
    "class": {{
      "type": "string",
      "default": "",
      "description": "Additional CSS classes"
    }},
    "onclick": {{
      "type": "string",
      "default": "",
      "description": "Click handler"
    }}
  }}
}}
"""

@click.group()
def cli():
    """CLI tool for django-coreui"""
    pass

@cli.command()
@click.argument('component_name')
def create(component_name):
    """
    Create a new component scaffold.
    Example:
        coreui create Button
    """
    component_class = component_name.capitalize()
    base_dir = Path(os.getcwd()) / "coreui" / "components" / component_class
    try:
        if base_dir.exists():
            click.echo(f"Component {component_class} already exists.")
            sys.exit(1)

        # Create directories
        base_dir.mkdir(parents=True)
        click.echo(f"Creating component directory: {base_dir}")

        # Write component.py
        with open(base_dir / "component.py", "w") as f:
            f.write(BASE_COMPONENT_TEMPLATE.format(
                component_class=component_class,
                component_name=component_name.lower()
            ))

        # Write template.html
        with open(base_dir / "template.html", "w") as f:
            f.write(TEMPLATE_HTML)

        # Write style.css
        with open(base_dir / "style.css", "w") as f:
            f.write(STYLE_CSS.format(component_class=component_class))

        # Write script.js
        with open(base_dir / "script.js", "w") as f:
            f.write(SCRIPT_JS.format(component_class=component_class))

        # Write meta.json
        with open(base_dir / "meta.json", "w") as f:
            f.write(META_JSON.format(component_class=component_class, component_name=component_name.lower()))

        click.echo(f"Component {component_class} scaffold created successfully!")
    except Exception as e:
        click.echo(f"Error creating component scaffold: {e}")

if __name__ == "__main__":
    cli()
