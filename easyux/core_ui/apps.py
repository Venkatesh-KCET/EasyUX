from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules
import logging

logger = logging.getLogger(__name__)


class CoreUIConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "coreui"
    verbose_name = "Django CoreUI"

    def ready(self):
        from .engine.registry import ComponentRegistry
        from .engine.loader import ComponentLoader

        # Step 1: Autodiscover user-defined component.py files
        try:
            autodiscover_modules('component')
            logger.info("[CoreUI] Successfully autodiscovered components.")
        except Exception as e:
            logger.exception(f"[CoreUI] Component autodiscovery failed: {e}")

        # Step 2: Register base components into registry
        try:
            ComponentLoader().load_all_components()
            logger.info("[CoreUI] Loaded all CoreUI components.")
        except Exception as e:
            logger.exception(f"[CoreUI] Component loading failed: {e}")

        # Step 3: Register lifecycle hooks or preload assets if needed
        try:
            registry = ComponentRegistry.get_instance()
            registry.run_global_hook("on_register")
        except Exception as e:
            logger.warning(f"[CoreUI] Lifecycle hook execution failed: {e}")
