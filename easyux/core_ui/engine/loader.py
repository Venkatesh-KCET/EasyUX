import os
import importlib.util
from django.conf import settings
from pathlib import Path
from registry import ComponentRegistry


class ComponentLoader:

    def __init__(self):
        self.registry = ComponentRegistry.get_instance()
        self.component_dir = Path(__file__).resolve().parent.parent / "components"

    def load_all_components(self):
        for path in self.component_dir.iterdir():
            if path.is_dir():
                self._load_component_from_dir(path)

    def _load_component_from_dir(self, path: Path):
        module_path = path / "component.py"
        if not module_path.exists():
            return

        module_name = f"coreui.components.{path.name}.component"
        spec = importlib.util.spec_from_file_location(module_name, str(module_path))

        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Look for a class named after the folder (e.g., Button -> Button class)
            class_name = path.name
            component_class = getattr(module, class_name, None)

            if component_class:
                self.registry.register(class_name, component_class)
