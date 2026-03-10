# Guide: Adding a New Recognizer to the Anonymization Tool

Welcome! This guide will walk you through the process of adding a new PII recognizer to your anonymization tool, using a real-world example (detecting user IDs like `uc46epev`).

---

## 🧩 What is a Recognizer?
A **recognizer** is a component that detects specific types of sensitive information (PII) in text, such as names, emails, or custom patterns (like user IDs). Recognizers are the "eyes" of your anonymization pipeline—they find what needs to be anonymized!

### Where do Recognizers fit in the Project?
- **Recognizer logic** lives in: `pii_deid_service/entity_recognizer/`
- **Plugin wrappers** (which make recognizers usable in the pipeline) live in: `pii_deid_service/plugins/builtin/recognizer_plugins.py`
- **Registration** is handled by the plugin system.
- **Pipeline config** (JSON) tells the system which recognizers to use.

**Diagram:**
```mermaid
flowchart TD
    subgraph Entity Recognizer
        A[UserIdRecognizer (PatternRecognizer)]
    end
    subgraph Plugin System
        B[UserIdRecognizerPlugin (RecognizerPlugin)]
    end
    subgraph Pipeline
        C[Pipeline Config: "user_id_recognizer"]
    end
    A --> B --> C
```

---

## 🚀 Why Add a Custom Recognizer?
- **Detect custom PII** (e.g., user IDs, internal codes, etc.)
- **Extend the tool** for your organization's unique needs
- **Plug-and-play**: Once added, your recognizer works with the whole anonymization pipeline!

---

## ❓ Why Do We Need a Plugin Wrapper?

### What is the Role of the Plugin Wrapper?
- The plugin wrapper acts as a **bridge** between your recognizer logic (e.g., `UserIdRecognizer`) and the rest of the anonymization system.
- It provides a **standard interface** so the pipeline can use any recognizer in a consistent way, regardless of its internal implementation.
- It allows the system to **dynamically load, configure, and use** recognizers based on the pipeline configuration (JSON).

### What Happens If We Don't Wrap It?
- The pipeline and plugin system **won't know about your recognizer**—it won't be available for use in configs.
- You would have to manually instantiate and call your recognizer, breaking the modular, plug-and-play design.
- You lose the ability to **mix and match** recognizers, or to easily swap them out without changing code.

### How is Wrapping Useful?
- **Automatic registration:** The system can discover and use your recognizer just by its name in the config.
- **Configuration:** You can pass different settings to your recognizer via the config file.
- **Extensibility:** Anyone can add new recognizers as plugins, making the system flexible and future-proof.
- **Consistency:** All recognizers, no matter how they work internally, are used in the same way by the pipeline.

**In summary:**
The plugin wrapper is what makes your recognizer a "first-class citizen" in the anonymization tool. Without it, your recognizer is invisible to the pipeline and cannot be used in a modular, configurable way.

---

# Step-by-Step: Add a User ID Recognizer

We'll add a recognizer for user IDs matching the pattern: `uc46epev` (i.e., `uc` followed by 6 lowercase letters or digits).

---

## **Step 1: Implement the Recognizer Logic**

Create a new file: `pii_deid_service/entity_recognizer/user_id_recognizer.py`

```python
import re
from presidio_analyzer import Pattern, PatternRecognizer

class UserIdRecognizer(PatternRecognizer):
    PATTERNS = [
        Pattern("User ID", r"uc[a-z0-9]{6}", 0.5)
    ]
    def __init__(self):
        super().__init__(
            supported_entity="USER_ID",
            patterns=self.PATTERNS,
            supported_language="en"
        )
```

**What this does:**
- Uses a regex to match user IDs like `uc46epev`.
- Inherits from Presidio's `PatternRecognizer` for easy integration.

---

## **Step 2: Create a Plugin Wrapper**

Edit `pii_deid_service/plugins/builtin/recognizer_plugins.py` and add:

```python
from ..base import RecognizerPlugin, PluginMetadata, PluginType
from ...entity_recognizer.user_id_recognizer import UserIdRecognizer

class UserIdRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="user_id_recognizer",
            version="1.0.0",
            description="Detects user IDs like uc46epev",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            config_schema={}
        )
    def initialize(self):
        self.recognizer = UserIdRecognizer()
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="en"):
        return self.recognizer.analyze(text, language=language, entities=["USER_ID"] or [])
```

**What this does:**
- Wraps your recognizer in a plugin so the pipeline can use it.
- Registers it under the name `user_id_recognizer`.

---

## **Step 2.5: Register the Plugin (Make it Available to the System)**

After you create your plugin class, you must register it so the system can use it. There are two main ways:

### **A. Register All Plugins Automatically**
At the end of `pii_deid_service/plugins/builtin/recognizer_plugins.py`, add:
```python
from pii_deid_service.plugins.registry import plugin_registry
plugin_registry.register(YourPluginClass)
```
Do this for every plugin you want available. Example:
```python
plugin_registry.register(UserIdRecognizerPlugin)
plugin_registry.register(CurrencyRecognizerPlugin)
# ...and so on
```

### **B. Register Plugins Manually (One by One)**
If you only want to register some plugins, or want to do it in your own code:
```python
from pii_deid_service.plugins.registry import plugin_registry
from pii_deid_service.plugins.builtin.recognizer_plugins import UserIdRecognizerPlugin
plugin_registry.register(UserIdRecognizerPlugin)
```

### **How to Check Which Plugins Are Registered**
You can check at runtime:
```python
from pii_deid_service.plugins.registry import plugin_registry, PluginType
print(plugin_registry.get_available_plugins(PluginType.RECOGNIZER))
```
This will list all currently registered recognizer plugins.

---

## **Where and How Should You Register Plugins? (Quick Reference)**

- **builtin_plugins list (in plugin manager):**
  - Used for core plugins that should always be available.
  - Registered automatically when the plugin system is initialized.
  - Add your plugin class to this list if you want it always available.

- **plugin_registry.register (anywhere):**
  - The actual function that registers a plugin.
  - Can be called at the end of `recognizer_plugins.py`, in your own script, or anywhere else.
  - Use this for custom, optional, or dynamically loaded plugins.

- **You only need to register a plugin once!**
  - Register in either place, not both.
  - The important thing is that registration happens before you use the plugin in your pipeline.

---

## **Step 4: Use the Recognizer in Your Pipeline**

Edit your pipeline config (e.g., `user_configs/anonymization_pipeline.json`):

```json
{
  "name": "sample_pipeline",
  "description": "Sample pipeline with user ID recognizer",
  "models": [],
  "recognizers": [
    {
      "name": "user_id_recognizer",
      "config": {}
    }
  ],
  "operators": [
    {
      "name": "presidio_operator",
      "config": {
        "anonymization_method": "replace",
        "language": "en"
      }
    }
  ]
}
```

---

## **Step 5: Test It!**

Run your pipeline (e.g., with `examples/basic_usage.py`) and check that user IDs like `uc46epev` are detected and anonymized.

---

# 📝 How Recognizers Work in the Pipeline
- **Recognizer plugins** are loaded based on your pipeline config.
- When text is processed, each recognizer scans for its target patterns/entities.
- Detected entities are passed to operators for anonymization.
- **You can mix and match recognizers** for different PII types in one pipeline!

---

# 🎯 Summary
- Recognizers are the "finders" of PII in your pipeline.
- Add new ones by:
  1. Implementing the logic
  2. Creating a plugin wrapper
  3. Registering the plugin
  4. Adding it to your pipeline config
- The plugin system makes it easy to extend and customize detection for your needs.

---

**Ready to try? Let's do each step together!** 