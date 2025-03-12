import threading


class ComponentRegistry:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self._components = {}

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = ComponentRegistry()
        return cls._instance

    def register(self, name, component_class):
        if name in self._components:
            raise ValueError(f"Component '{name}' is already registered.")
        self._components[name] = component_class
        if hasattr(component_class, 'on_register'):
            component_class.on_register()

    def get(self, name):
        return self._components.get(name)

    def all(self):
        return self._components

    def exists(self, name):
        return name in self._components

    def run_global_hook(self, hook_name):
        for component in self._components.values():
            hook = getattr(component, hook_name, None)
            if callable(hook):
                try:
                    hook()
                except Exception as e:
                    print(f"[CoreUI] Hook '{hook_name}' failed in {component.__class__.__name__}: {e}")
