# Plugin System Details: Architecture, Files, and Roles

> **See also:** The [README](README.md) for a high-level overview and links to usage guides. This file is the authoritative, up-to-date source for plugin architecture, extension, and registration details in this project.

## What is a Plugin?
A **plugin** in this system is a modular, self-contained component that can be dynamically discovered, registered, and used by the PII de-identification pipeline. Plugins provide extensibility for:
- **Recognizers** (detect PII entities)
- **Operators** (anonymize or transform detected entities)
- **Models** (support advanced recognition)

Plugins allow you to add, remove, or update functionality without changing the core codebase.

---

## How Are Plugins Created and Registered?
- **Creation:** You write a class that inherits from a base plugin class (e.g., `RecognizerPlugin`, `OperatorPlugin`, `ModelPlugin`).
- **Registration:**
  - **Built-in plugins** are registered in code (recommended for most use cases).
  - **External plugins** can be discovered if their directory is added to the plugin loader's search path.
- **Configuration:** Each plugin has a JSON config (in `user_configs/recognizers/`, `user_configs/operators/`, etc.) that describes its name, module, class, and config.
- **Usage:** Pipelines reference plugins by name, and the system instantiates and uses them as needed.

---

## Plugin System Directory Structure & File Roles

### `pii_deid_service/plugins/`
- **`base.py`**: Defines the abstract base classes for all plugins (`BasePlugin`, `RecognizerPlugin`, `OperatorPlugin`, `ModelPlugin`) and the `PluginType` enum and `PluginMetadata` dataclass. All plugins must inherit from these to ensure a consistent interface.
- **`registry.py`**: Implements the `PluginRegistry`, a central registry for all plugins. Handles registration, lookup, instantiation, validation, and metadata management. Exposes a global `plugin_registry` instance.
- **`loader.py`**: Implements the `PluginLoader`, which discovers and loads plugins from specified directories. Handles dynamic import, registration, and validation of external plugins.
- **`manager.py`**: Implements the `PluginManager`, which orchestrates plugin initialization, registration of built-in plugins, and provides a high-level API for plugin management. Exposes a global `plugin_manager` instance.
- **`__init__.py`**: Exposes the main classes and global instances for import elsewhere in the codebase.
- **`builtin/`**: Contains the built-in plugin wrappers for recognizers, operators, and models.

### `pii_deid_service/plugins/builtin/`
- **`recognizer_plugins.py`**: Contains plugin wrapper classes for all built-in recognizers (e.g., Presidio, Flair, RegexPhoneRecognizerPlugin, etc.). At the end of the file, all these plugins are registered with the `plugin_registry`.
- **`operators.py`**: Contains plugin wrapper classes for built-in operators (e.g., PresidioOperatorPlugin). Registered similarly to recognizers.
- **`models.py`**: Contains plugin wrapper classes for built-in models (e.g., FlairModelPlugin, SpacyModelPlugin). Registered similarly.
- **`__init__.py`**: Exposes the main built-in plugin classes for import.

---

## Key Classes and Their Roles

### `BasePlugin` (in `base.py`)
- Abstract base for all plugins.
- Requires methods: `get_metadata`, `initialize`, `is_available`.
- Holds config and metadata.

### `RecognizerPlugin`, `OperatorPlugin`, `ModelPlugin` (in `base.py`)
- Extend `BasePlugin` and add required methods for their type:
  - **RecognizerPlugin**: `create_recognizer`, `recognize`
  - **OperatorPlugin**: `create_operator`, `apply`
  - **ModelPlugin**: `load_model`, `predict`

### `PluginMetadata` (in `base.py`)
- Dataclass holding plugin metadata (name, version, description, type, dependencies, config schema).

### `PluginType` (in `base.py`)
- Enum for plugin types: `MODEL`, `RECOGNIZER`, `OPERATOR`.

### `PluginRegistry` (in `registry.py`)
- Central registry for all plugins.
- Handles registration, lookup, instantiation, validation, and metadata.
- Exposes methods like `register`, `unregister`, `get_plugin_class`, `create_instance`, `list_plugins`.
- Global instance: `plugin_registry`.

### `PluginLoader` (in `loader.py`)
- Discovers and loads plugins from directories.
- Handles dynamic import and registration of external plugins.
- Used by the manager to add plugin directories and discover plugins.

### `PluginManager` (in `manager.py`)
- Orchestrates plugin system initialization.
- Registers built-in plugins.
- Provides high-level API for plugin management (get info, validate, create instance, etc.).
- Global instance: `plugin_manager`.

---

## How Plugins Are Used in the Pipeline
1. **Registration:** Built-in plugins are registered in code (e.g., at the end of `recognizer_plugins.py`).
2. **Configuration:** Each plugin has a JSON config describing its name, module, class, and config.
3. **Pipeline Reference:** Pipelines reference plugins by name in their config (e.g., `presidio_recognizer`, `regex_phone_recognizer`).
4. **Instantiation:** When a pipeline is built, the system looks up the plugin by name, instantiates it with the config, and uses it for recognition or anonymization.
5. **Auto-Detection:** Built-in plugins are always available. External plugins are only available if their directory is added to the loader.

---

## Glossary
- **Plugin:** Modular component (recognizer, operator, model) that extends the system.
- **Recognizer:** Detects PII entities in text.
- **Operator:** Anonymizes or transforms detected entities.
- **Model:** Provides advanced recognition capabilities.
- **Registration:** Making a plugin known to the system (usually in code for built-ins).
- **Auto-detection:** System automatically finds and registers plugins that are built-in or in specified directories.
- **Pipeline:** Configuration specifying which plugins to use for a processing task.
- **Plugin Wrapper:** A class that adapts a recognizer/model/operator to the plugin interface.

---

## FAQ
**Q: What files do I edit to add a new plugin?**
- Add your plugin class to the appropriate location (e.g., `entity_recognizer/` for recognizers).
- Add a plugin wrapper to `plugins/builtin/recognizer_plugins.py`, `operators.py`, or `models.py`.
- Register your plugin at the end of the relevant file.
- Add a JSON config in `user_configs/recognizers/`, `user_configs/operators/`, or `user_configs/models/`.

**Q: How does the system know which plugins are available?**
- Built-in plugins are registered in code and always available.
- External plugins are only available if their directory is added to the loader.

**Q: How do I use a plugin in a pipeline?**
- Reference its name in the pipeline config JSON.

**Q: What methods must my plugin implement?**
- See the abstract base class for your plugin type in `base.py`.

---

## Summary Table: Plugin System Files and Roles
| File/Dir | What | Why/Role |
|----------|------|----------|
| base.py | Base classes, metadata, types | All plugins must inherit from these |
| registry.py | Plugin registry | Central management of plugins |
| loader.py | Plugin loader | Discovers/loads plugins from directories |
| manager.py | Plugin manager | Orchestrates registration, validation, info |
| __init__.py | Exports main classes/instances | For easy import elsewhere |
| builtin/recognizer_plugins.py | Built-in recognizer plugins | Plugin wrappers, registration |
| builtin/operators.py | Built-in operator plugins | Plugin wrappers, registration |
| builtin/models.py | Built-in model plugins | Plugin wrappers, registration |
| builtin/__init__.py | Exports built-in plugin classes | For easy import |

---

This document should give you a complete understanding of the plugin system, its files, classes, and how everything fits together in the PII de-identification pipeline. 