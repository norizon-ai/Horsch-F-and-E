# 🔒 Modular PII De-identification Service

A highly modular and extensible system for detecting and anonymizing Personally Identifiable Information (PII) in text data, supporting multiple languages and specialized recognizers.

## 🎯 Overview

This system provides a **fully modular, plugin-based architecture** for PII de-identification that allows users to easily add, remove, or modify components without changing the core codebase. It supports both German and English text processing with specialized phone number detection.

## ✨ Key Features

- **🔌 Plugin System**: Hot-swappable components (models, recognizers, operators)
- **⚙️ Configuration-Driven**: JSON-based pipeline configurations
- **🏭 Factory Pattern**: Dynamic component creation and management
- **🌍 Multi-Language Support**: German and English text processing
- **📱 Specialized Phone Detection**: Custom German and Presidio phone recognizers
- **📊 Monitoring**: Real-time progress tracking and performance metrics
- **🛡️ Validation**: Comprehensive validation at every level
- **📈 Extensible**: Easy to add new components and capabilities

## 🏗️ Architecture

The system is built with a **modular plugin-based architecture**:

### Core Components
- **Configuration Management**: Pydantic-based schemas for validation
- **Plugin Registry**: Dynamic component registration and discovery
- **Pipeline Builder**: Assembles components based on configuration
- **Recognizers**: Detect PII entities (names, phone numbers, emails, etc.)
- **Operators**: Anonymize detected entities

### Available Pipelines

| Pipeline | Description | Best For |
|----------|-------------|----------|
| `flair_only_pipeline.json` | Flair model only (no phone detection) | Basic NER tasks |
| `flair_with_custom_phone_pipeline.json` | Flair + Custom German phone recognizer | German text with phone numbers |
| `flair_with_presidio_phone_pipeline.json` | Flair + Presidio's built-in phone recognizer | International phone number support |

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/TalibDaryabi/Anonymization_tool.git
cd Anonymization_tool

# Install dependencies
pip install -r requirements.txt
```

### 2. Basic Usage

```python
import json
from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.plugin_schemas import PluginPipelineConfig
from pii_deid_service.pipeline import run_pipeline

# Load pipeline configuration
config_path = "user_configs/pipelines/flair_with_presidio_phone_pipeline.json"
with open(config_path, "r", encoding="utf-8") as f:
    config_data = json.load(f)
config = PluginPipelineConfig(**config_data)

# Build pipeline
builder = PluginBasedPipelineBuilder()
builder.initialize()
pipeline = builder.build_pipeline(config)

# Your text to anonymize
text = "Hallo, mein Name ist Hans Müller. Meine Telefonnummer ist +49-30-123-4567."

# Anonymize using the pipeline
anonymized_text = run_pipeline(pipeline, text)

print("Original:", text)
print("Anonymized:", anonymized_text)
```

### 3. Ready-to-Use Examples

```bash
# Test German text with custom phone detection
python test_flair_with_custom_phone_DE.py

# Test German text with Presidio phone detection
python test_flair_with_presidio_phone_DE.py

# Test English text processing
python test_without_phone_EN.py
```

## 📁 Project Structure

```
Anonymization_tool/
├── pii_deid_service/                    # Core system
│   ├── config_management/               # Configuration schemas and validation
│   │   ├── plugin_schemas.py           # Pydantic models for pipeline configs
│   │   └── config_manager.py           # Centralized config management
│   ├── entity_recognizer/              # Recognizer implementations
│   │   ├── flair_recognizer.py         # Flair NER model wrapper
│   │   ├── presidio_recognizer.py      # Presidio recognizer wrapper
│   │   ├── german_phone_recognizer.py  # Custom German phone detection
│   │   └── ...                         # Other recognizers
│   ├── operators/                      # Anonymization operators
│   │   └── presidio_operator.py        # Presidio anonymization wrapper
│   ├── plugins/                        # Plugin system
│   │   ├── base.py                     # Base plugin classes
│   │   ├── manager.py                  # Plugin manager
│   │   ├── registry.py                 # Plugin registry
│   │   └── builtin/                    # Built-in plugins
│   │       ├── recognizer_plugins.py   # Recognizer plugin wrappers
│   │       └── operator_plugins.py     # Operator plugin wrappers
│   ├── pipeline/                       # Pipeline architecture
│   │   ├── builder.py                  # Pipeline builder
│   │   ├── monitor.py                  # Progress monitoring
│   │   └── plugin_validator.py         # Pipeline validation
│   └── factories/                      # Factory pattern implementation
│       ├── model_factory.py            # Model component factory
│       ├── recognizer_factory.py       # Recognizer component factory
│       └── operator_factory.py         # Operator component factory
├── user_configs/                       # Pipeline configurations
│   ├── pipelines/                      # Available pipeline configs
│   │   ├── flair_only_pipeline.json
│   │   ├── flair_with_custom_phone_pipeline.json
│   │   └── flair_with_presidio_phone_pipeline.json
│   ├── models/                         # Model configurations
│   └── recognizers/                    # Recognizer configurations
├── examples/                           # Usage examples
│   ├── basic_usage.py                  # Basic usage example
│   ├── intermediate_usage.py           # Intermediate usage example
│   └── advanced_usage.py               # Advanced usage example
├── test_*.py                          # Test scripts for different scenarios
├── anonymize_your_text_guide.md       # Comprehensive usage guide
└── README.md                          # This file
```

## 🔧 Available Recognizers

### Entity Recognizers
- **Flair Recognizer**: High-accuracy NER for German and English text
- **Presidio Recognizer**: Microsoft's comprehensive PII detection
- **Regex Phone Recognizer**: Basic international phone number detection
- **...**
### Anonymization Operators
- **Presidio Operator**: Advanced anonymization with context awareness

## 📊 Performance & Capabilities

### Detection Capabilities
- ✅ **Person Names**: Hans Müller, John Doe, Dr. Michael Weber
- ✅ **Organizations**: firma.de, Microsoft, krankenhaus.com
- ✅ **Locations**: Berlin, Deutschland, Seattle, München
- ✅ **Phone Numbers**: +49-30-123-4567, 030-987-6543, (030) 123-7890
- ✅ **Email Addresses**: hans.mueller@firma.de, john@email.com
- ✅ **Dates**: 15. März, March 15th
- **MANY MORE**

### Language Support
- **German**: Full support with German Flair model
- **English**: Full support with English Flair model

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Test German text with custom phone detection
python test_flair_with_custom_phone_DE.py

# Test German text with Presidio phone detection
python test_flair_with_presidio_phone_DE.py

# Test English text processing
python test_without_phone_EN.py

# Test English text with phone detection
python test_with_phone_recognizer_EN.py

# Run comprehensive examples
python examples/basic_usage.py
python examples/intermediate_usage.py
python examples/advanced_usage.py
```

## 🔧 Adding New Components

### Adding a New Recognizer

1. **Create the recognizer implementation**:
```python
# pii_deid_service/entity_recognizer/my_recognizer.py
class MyRecognizer:
    def __init__(self, config=None):
        self.config = config or {}
    
    def recognize(self, text, language="en"):
        # Your recognition logic here
        return [{"entity_type": "PERSON", "start": 0, "end": 4, "score": 0.9}]
```

2. **Create a plugin wrapper**:
```python
# pii_deid_service/plugins/builtin/recognizer_plugins.py
from pii_deid_service.plugins.base import RecognizerPlugin, PluginMetadata, PluginType

class MyRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="my_recognizer",
            version="1.0.0",
            description="My custom recognizer",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    
    def initialize(self):
        self.recognizer = MyRecognizer(self.config)
        return True
    
    def recognize(self, text, language="en"):
        return self.recognizer.recognize(text, language)
```

3. **Register the plugin**:
```python
# In pii_deid_service/plugins/builtin/recognizer_plugins.py
plugin_registry.register(MyRecognizerPlugin)
```

4. **Create configuration**:
```json
// user_configs/recognizers/my_recognizer.json
{
  "name": "my_recognizer",
  "config": {}
}
```

5. **Use in pipeline**:
```json
// user_configs/pipelines/my_pipeline.json
{
  "name": "my_pipeline",
  "recognizers": [
    {
      "name": "my_recognizer",
      "config": {},
      "config_path": "user_configs/recognizers/my_recognizer.json"
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

## 📚 Documentation

- **[Comprehensive Usage Guide: Anonymize Your Text](anonymize_your_text_guide.md)**: Step-by-step instructions, templates, and examples for using the system in scripts, as a library, or via API.
- **[Plugin System Details](plugin_details.md)**: In-depth explanation of the plugin architecture, how to add new plugins, and how plugins are registered and used in pipelines.
- **[Project Structure](PROJECT_STRUCTURE.md)**: Detailed architecture overview
- **[Examples](examples/)**: Ready-to-run examples with sample data

## 🔄 Code Flow: From Input to Output

See [code_flow.md](code_flow.md) for a high-level overview and diagram of how data moves through the system—from input text, through pipeline building, recognition, post-processing, and final anonymization output.

## 🎯 Use Cases

### German Text Processing
```python
# Use German Flair model + phone detection
config_path = "user_configs/pipelines/flair_with_presidio_phone_pipeline.json"
text = "Hallo, mein Name ist Hans Müller. Meine Telefonnummer ist +49-30-123-4567."
# language="de"
```

### English Text Processing
```python
# Use English Flair model
config_path = "user_configs/pipelines/flair_only_pipeline.json"
text = "John Doe works at Microsoft in Seattle."
# language="en"
```

### Custom Phone Detection
```python
# Use custom German phone patterns
config_path = "user_configs/pipelines/flair_with_custom_phone_pipeline.json"
text = "Contact me at 030-987-6543 or (030) 123-7890"
# language="de"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your component following the plugin pattern
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**🎉 The modular PII de-identification system is ready for production use!**

The system provides a flexible, extensible architecture for PII detection and anonymization with support for multiple languages and specialized recognizers. Check out the [comprehensive usage guide](anonymize_your_text_guide.md) for detailed instructions and examples.

# Model Download and Configuration

Some features of this library require large external models (e.g., Flair NER models) that are not included in the repository due to their size.

## How to Use External Models

1. **Download the required model** (e.g., `ner-german-large.pt`) from the official source (such as the Flair model hub).
2. **Place the downloaded model file** in the `models` folder of your project (recommended), or any other directory of your choice.
3. **Update your configuration file** (e.g., `user_configs/models/flair_recognizer.json`) to point to the correct model path.

### Example
If you place the model in the `models` folder:
```json
{
  "MODEL_PATH": "models/ner-german-large.pt",
  ...
}
```
If you place the model elsewhere, provide the absolute or relative path:
```json
{
  "MODEL_PATH": "/home/user/my_models/ner-german-large.pt",
  ...
}
```

**Note:** The library will raise a clear error if the model file is not found at the specified path. Please ensure the path is correct and the file exists.

# Pipeline Output Guarantee

The pipeline system is designed to always return the final anonymized string as output, regardless of the number or order of operators (including post-processing steps like EntitySanitizer). This ensures a consistent and user-friendly experience for all users and scripts.

## How to Use the Pipeline

Use the provided `run_pipeline` function for all pipeline executions. This function automatically chains all operators and always returns the anonymized text.

### Example Usage
```python
from pii_deid_service.pipeline import run_pipeline

# Build your pipeline as usual (see above for details)
pipeline = ...  # built using PluginBasedPipelineBuilder

sample_text = "Hello, my name is John Doe and my email is john.doe@company.com."
anonymized_text = run_pipeline(pipeline, sample_text)
print(anonymized_text)  # Always prints the anonymized version of the input text
```

- You do not need to handle operator chaining or output type checking in your code.
- The pipeline will always return the anonymized string, even if you use custom or multiple post-processing operators.

See the rest of this README for details on configuring your pipeline, adding operators, and customizing behavior.

# EntitySanitizer: Post-Processing for Entity Results

The EntitySanitizer operator allows you to flexibly post-process recognized entities before anonymization. It can deduplicate, merge, filter by confidence, prioritize by entity type, and more—all configurable by the user.

## How to Add EntitySanitizer to Your Pipeline

1. **Add EntitySanitizer to the `operators` list in your pipeline config:**

```json
"operators": [
  {
    "name": "entity_sanitizer",
    "config_path": "user_configs/operators/entity_sanitizer.json"
  },
  {
    "name": "presidio_operator",
    "config": { "anonymization_method": "replace", "language": "en" },
    "config_path": null
  }
]
```

2. **Configure EntitySanitizer in `user_configs/operators/entity_sanitizer.json`:**

```json
{
  "name": "entity_sanitizer",
  "config": {
    "strategies": ["deduplicate", "filter_by_confidence", "merge_overlaps"],
    "confidence_threshold": 0.7,
    "entity_priority": ["PERSON", "LOCATION", "ORGANIZATION"],
    "custom_strategies": {}
  }
}
```
- You can use any combination of strategies, in any order.
- Leave any field empty to use the default.
- You can add your own custom strategies if needed.

3. **Result:**
- All recognized entities will be sanitized according to your configuration before anonymization is applied.
- This step is modular and can be used in any pipeline.

See the `user_configs/operators/entity_sanitizer.json` file for a template and more options.