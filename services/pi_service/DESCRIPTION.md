# PII De-identification Service - Complete Project Guide

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Design Philosophy](#design-philosophy)
4. [How It Works](#how-it-works)
5. [Core Components](#core-components)
6. [Configuration System](#configuration-system)
7. [Plugin System](#plugin-system)
8. [Pipeline Architecture](#pipeline-architecture)
9. [Usage Guide](#usage-guide)
10. [Adding New Components](#adding-new-components)
11. [Troubleshooting](#troubleshooting)
12. [Best Practices](#best-practices)

---

## 🎯 Project Overview

### What is this project?
This is a **modular PII (Personally Identifiable Information) de-identification service** that can detect and anonymize sensitive information in text data. Think of it as a smart system that can find personal information like names, emails, phone numbers, and replace them with safe alternatives.

### What does it do?
- **Detects PII**: Finds personal information in text (names, emails, phone numbers, addresses, etc.)
- **Anonymizes Data**: Replaces sensitive information with safe alternatives
- **Modular Design**: Easy to add new detection methods or anonymization techniques
- **Configurable**: Can be customized for different use cases

### Why is this useful?
- **Privacy Protection**: Keeps personal data safe
- **Compliance**: Helps meet data protection regulations (GDPR, HIPAA, etc.)
- **Flexibility**: Can be adapted for different industries and requirements
- **Extensibility**: Easy to add new capabilities

---

## 📁 Project Structure

```
pii-deid-service-main/
├── configs/                          # Configuration files
│   ├── sample_pipeline_plugin.json   # Example pipeline configuration
│   └── service_config.json           # Main service configuration
├── examples/                         # Usage examples and sample data
│   ├── data/                         # Sample data files
│   │   ├── sample_ticket.json        # Sample ticket data
│   │   ├── sample_email.json         # Sample email data
│   │   └── sample_text.json          # Sample text data
│   ├── basic_usage.py                # Basic usage example
│   ├── intermediate_usage.py         # Intermediate usage example
│   ├── advanced_usage.py             # Advanced usage example
│   └── README.md                     # Examples documentation
├── pii_deid_service/                 # Main package directory
│   ├── config/                       # Configuration management
│   │   ├── config_manager.py         # Manages all configurations
│   │   ├── plugin_schemas.py         # Data models for configurations
│   │   └── service_schemas.py        # Service configuration models
│   ├── factories/                    # Factory pattern implementation
│   │   ├── model_factory.py          # Creates model instances
│   │   ├── recognizer_factory.py     # Creates recognizer instances
│   │   └── operator_factory.py       # Creates operator instances
│   ├── plugins/                      # Plugin system
│   │   ├── manager.py                # Manages all plugins
│   │   ├── registry.py               # Registers and stores plugins
│   │   └── builtin/                  # Built-in plugins
│   │       ├── models/               # Built-in model plugins
│   │       ├── recognizer_plugins/          # Built-in recognizer plugins
│   │       └── operators/            # Built-in operator plugins
│   ├── pipeline/                     # Pipeline architecture
│   │   ├── builder.py                # Builds processing pipelines
│   │   ├── plugin_validator.py       # Validates pipeline configurations
│   │   └── monitor.py                # Monitors pipeline performance
│   └── tests/                        # Test files
│       ├── test_complete_system.py   # Comprehensive system test
│       ├── test_plugin_system.py     # Plugin system test
│       ├── test_pipeline_architecture.py # Pipeline architecture test
│       └── results/                  # Test results
├── user_interface.py                 # User-friendly interface
├── requirements.txt                  # Python dependencies
├── pyproject.toml                    # Project configuration
├── README.md                         # Basic project information
├── PROJECT_STRUCTURE.md              # Detailed structure overview
└── DESCRIPTION.md                    # This comprehensive guide
```

---

## 🏗️ Design Philosophy

### 1. **Modularity**
The project is built using a **modular architecture**, which means:
- Each component is independent and can be replaced or modified without affecting others
- New features can be added without changing existing code
- Components can be reused in different combinations

### 2. **Plugin-Based System**
Everything is a **plugin**:
- **Models**: Different AI/ML models for text processing
- **Recognizers**: Different methods to detect PII
- **Operators**: Different methods to anonymize detected PII

### 3. **Configuration-Driven**
The system is **configuration-driven**, meaning:
- Behavior is controlled by configuration files (JSON)
- No code changes needed to change behavior
- Easy to create different setups for different use cases

### 4. **Factory Pattern**
Uses the **Factory Pattern** for creating components:
- Centralized component creation
- Easy to manage dependencies
- Consistent component initialization

---

## ⚙️ How It Works

### Step-by-Step Process

1. **Configuration Loading**
   ```
   User creates config → System loads config → Validates config
   ```

2. **Plugin Discovery**
   ```
   System scans plugins → Registers available plugins → Validates plugins
   ```

3. **Pipeline Building**
   ```
   Config specifies components → Factory creates instances → Pipeline assembles
   ```

4. **Text Processing**
   ```
   Input text → Recognizer detects PII → Operator anonymizes → Output text
   ```

### Data Flow Example

Let's say you have this text: *"Hello, my name is John Doe and my email is john@example.com"*

1. **Input**: Text goes into the pipeline
2. **Recognition**: Recognizer finds "John Doe" (PERSON) and "john@example.com" (EMAIL)
3. **Anonymization**: Operator replaces with "[PERSON]" and "[EMAIL]"
4. **Output**: *"Hello, my name is [PERSON] and my email is [EMAIL]"*

---

## 🔧 Core Components

### 1. **Configuration Manager** (`pii_deid_service/config_management/config_manager.py`)

**Purpose**: Manages all system configurations

**What it does**:
- Loads configuration files
- Validates configurations
- Provides configuration information to other components

**Key Methods**:
```python
# Load service configuration
service_config = config_manager.get_service_config()

# Load pipeline configurations
pipelines = config_manager.get_all_pipeline_configs()

# Validate configurations
errors = config_manager.validate_configuration()
```

### 2. **Plugin Manager** (`pii_deid_service/plugins/manager.py`)

**Purpose**: Manages all plugins in the system

**What it does**:
- Discovers available plugins
- Registers plugins
- Creates plugin instances
- Validates plugins

**Key Methods**:
```python
# Initialize plugin system
plugin_manager.initialize()

# Get available plugins
plugins = plugin_manager.get_available_plugins()

# Create plugin instance
instance = plugin_manager.create_plugin("presidio_recognizer")
```

### 3. **Pipeline Builder** (`pii_deid_service/pipeline/builder.py`)

**Purpose**: Builds processing pipelines from configurations

**What it does**:
- Reads pipeline configurations
- Creates component instances
- Assembles them into working pipelines
- Validates pipeline integrity

**Key Methods**:
```python
# Initialize builder
builder.initialize()

# Build pipeline from config
pipeline = builder.build_pipeline(config)

# Get available components
components = builder.get_available_components()
```

### 4. **Factories** (`pii_deid_service/factories/`)

**Purpose**: Create instances of different component types

**What they do**:
- **Model Factory**: Creates AI/ML model instances
- **Recognizer Factory**: Creates PII detection instances
- **Operator Factory**: Creates anonymization instances

**Example**:
```python
# Create a recognizer
recognizer = recognizer_factory.create("presidio_recognizer")

# Create an operator
operator = operator_factory.create("presidio_operator")
```

---

## ⚙️ Configuration System

### Configuration Files

#### 1. **Service Configuration** (`user_configs/service_config.json`)
```json
{
  "service_name": "PII De-identification Service",
  "version": "1.0.0",
  "description": "Modular PII detection and anonymization service",
  "config_paths": {
    "pipelines": "user_configs/pipelines",
    "models": "user_configs/models",
    "recognizers": "user_configs/recognizers",
    "operators": "user_configs/operators"
  }
}
```

#### 2. **Pipeline Configuration** (`user_configs/sample_pipeline_plugin.json`)
```json
{
  "name": "sample_pipeline",
  "description": "Sample pipeline for PII detection and anonymization",
  "models": [],
  "recognizers": [
    {
      "name": "presidio_recognizer",
      "config": {
        "language": "en",
        "entities": ["PERSON", "EMAIL", "PHONE_NUMBER", "LOCATION"],
        "confidence_threshold": 0.3
      }
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

### Configuration Structure

- **name**: Unique identifier for the pipeline
- **description**: Human-readable description
- **models**: List of AI/ML models to use
- **recognizers**: List of PII detection methods
- **operators**: List of anonymization methods

Each component has:
- **name**: Plugin name to use
- **config**: Component-specific configuration

---

## 🔌 Plugin System

### What is a Plugin?

A **plugin** is a self-contained component that can be:
- **Added** to the system without changing existing code
- **Removed** from the system without breaking other components
- **Configured** independently
- **Reused** in different combinations

### Plugin Types

#### 1. **Model Plugins**
**Purpose**: Provide AI/ML models for text processing

**Built-in Models**:
- `flair_model`: Uses Flair NLP library
- `spacy_model`: Uses spaCy NLP library

**Example Model Plugin**:
```python
class FlairModelPlugin:
    def __init__(self):
        self.name = "flair_model"
        self.version = "1.0.0"
        self.description = "Flair NLP model for text processing"
    
    def create_model(self, config):
        # Create and return model instance
        return model_instance
```

#### 2. **Recognizer Plugins**
**Purpose**: Detect PII in text

**Built-in Recognizers**:
- `presidio_recognizer`: Uses Microsoft Presidio

**Example Recognizer Plugin**:
```python
class PresidioRecognizerPlugin:
    def __init__(self):
        self.name = "presidio_recognizer"
        self.version = "1.0.0"
        self.description = "Microsoft Presidio for PII detection"
    
    def create_recognizer(self, config):
        # Create and return recognizer instance
        return recognizer_instance
```

#### 3. **Operator Plugins**
**Purpose**: Anonymize detected PII

**Built-in Operators**:
- `presidio_operator`: Uses Microsoft Presidio anonymization

**Example Operator Plugin**:
```python
class PresidioOperatorPlugin:
    def __init__(self):
        self.name = "presidio_operator"
        self.version = "1.0.0"
        self.description = "Microsoft Presidio for PII anonymization"
    
    def create_operator(self, config):
        # Create and return operator instance
        return operator_instance
```

### Plugin Registration

Plugins are automatically registered when the system starts:

1. **Built-in plugins** are registered from the `builtin/` directory
2. **External plugins** can be discovered from custom directories
3. **Plugin validation** ensures plugins are compatible

---

## 🔄 Pipeline Architecture

### What is a Pipeline?

A **pipeline** is a sequence of processing steps that:
1. Takes input text
2. Processes it through multiple stages
3. Produces output text

### Pipeline Components

```
Input Text → [Models] → [Recognizers] → [Operators] → Output Text
```

#### 1. **Models Stage**
- **Purpose**: Pre-process text or provide AI capabilities
- **Example**: Language detection, text normalization
- **Optional**: Can be empty if not needed

#### 2. **Recognizers Stage**
- **Purpose**: Detect PII entities in text
- **Required**: At least one recognizer needed
- **Example**: Find names, emails, phone numbers

#### 3. **Operators Stage**
- **Purpose**: Anonymize detected entities
- **Required**: At least one operator needed
- **Example**: Replace names with [PERSON], emails with [EMAIL]

### Pipeline Building Process

1. **Load Configuration**: Read pipeline config file
2. **Validate Configuration**: Check if config is valid
3. **Create Components**: Use factories to create instances
4. **Assemble Pipeline**: Put components together
5. **Validate Pipeline**: Ensure pipeline can work
6. **Return Pipeline**: Ready-to-use pipeline

### Pipeline Usage

```python
# Build pipeline
pipeline = builder.build_pipeline(config)

# Process text
text = "Hello, my name is John Doe"
result = process_with_pipeline(pipeline, text)
# Result: "Hello, my name is [PERSON]"
```

---

## 📖 Usage Guide

### Quick Start

#### 1. **Basic Usage** (Using the User Interface)

```bash
# Run the user interface
python user_interface.py
```

This will:
- Show available components
- Create a simple pipeline
- Process sample data
- Display results

#### 2. **Programmatic Usage**

```python
from pii_deid_service.plugins.manager import PluginManager
from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.plugin_schemas import PluginPipelineConfig

# Initialize plugin system
plugin_manager = PluginManager()
plugin_manager.initialize()

# Create pipeline configuration
config = PluginPipelineConfig(
    name="my_pipeline",
    description="My custom pipeline",
    models=[],
    recognizers=[
        {
            "name": "presidio_recognizer",
            "config": {
                "language": "en",
                "entities": ["PERSON", "EMAIL"]
            }
        }
    ],
    operators=[
        {
            "name": "presidio_operator",
            "config": {
                "anonymization_method": "replace"
            }
        }
    ]
)

# Build pipeline
builder = PluginBasedPipelineBuilder()
builder.initialize()
pipeline = builder.build_pipeline(config)

# Process text
text = "Hello, my name is John Doe and my email is john@example.com"
result = process_text(pipeline, text)
print(result)  # "Hello, my name is [PERSON] and my email is [EMAIL]"
```

#### 3. **Using Examples**

```bash
# Run basic example
python examples/basic_usage.py

# Run intermediate example
python examples/intermediate_usage.py

# Run advanced example
python examples/advanced_usage.py
```

### Configuration Examples

#### Simple Pipeline
```json
{
  "name": "simple_pipeline",
  "description": "Basic PII detection",
  "models": [],
  "recognizers": [
    {
      "name": "presidio_recognizer",
      "config": {
        "language": "en",
        "entities": ["PERSON", "EMAIL"]
      }
    }
  ],
  "operators": [
    {
      "name": "presidio_operator",
      "config": {
        "anonymization_method": "replace"
      }
    }
  ]
}
```

#### Advanced Pipeline
```json
{
  "name": "advanced_pipeline",
  "description": "Advanced PII detection with multiple components",
  "models": [
    {
      "name": "spacy_model",
      "config": {
        "model": "en_core_web_sm"
      }
    }
  ],
  "recognizers": [
    {
      "name": "presidio_recognizer",
      "config": {
        "language": "en",
        "entities": ["PERSON", "EMAIL", "PHONE_NUMBER", "LOCATION"],
        "confidence_threshold": 0.5
      }
    }
  ],
  "operators": [
    {
      "name": "presidio_operator",
      "config": {
        "anonymization_method": "mask",
        "mask_char": "*"
      }
    }
  ]
}
```

---

## ➕ Adding New Components

### How to Add a New Recognizer

#### Step 1: Create the Recognizer Plugin

Create a new file: `pii_deid_service/plugins/builtin/recognizer_plugins/my_recognizer.py`

```python
from typing import List, Dict, Any
from pii_deid_service.plugins.base import BaseRecognizerPlugin

class MyRecognizerPlugin(BaseRecognizerPlugin):
    def __init__(self):
        super().__init__()
        self.name = "my_recognizer"
        self.version = "1.0.0"
        self.description = "My custom PII recognizer"
    
    def create_recognizer(self, config: Dict[str, Any]):
        """Create and return a recognizer instance."""
        return MyRecognizer(config)
    
    def validate_config(self, config: Dict[str, Any]) -> List[str]:
        """Validate configuration and return any errors."""
        errors = []
        # Add your validation logic here
        return errors

class MyRecognizer:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        # Initialize your recognizer here
    
    def recognize(self, text: str) -> List[Dict[str, Any]]:
        """Detect PII entities in text."""
        entities = []
        
        # Add your recognition logic here
        # Example: Find email addresses
        import re
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        matches = re.finditer(email_pattern, text)
        
        for match in matches:
            entities.append({
                'entity_type': 'EMAIL',
                'start': match.start(),
                'end': match.end(),
                'text': match.group(),
                'confidence': 0.9
            })
        
        return entities
```

#### Step 2: Register the Plugin

The plugin will be automatically registered when the system starts, but you can also register it manually:

```python
from pii_deid_service.plugins.registry import plugin_registry
from pii_deid_service.plugins.builtin.recognizer_plugins.my_recognizer import MyRecognizerPlugin

# Register the plugin
plugin_registry.register_plugin("recognizer", MyRecognizerPlugin())
```

#### Step 3: Use the New Recognizer

Create a configuration that uses your new recognizer:

```json
{
  "name": "my_custom_pipeline",
  "description": "Pipeline using my custom recognizer",
  "models": [],
  "recognizers": [
    {
      "name": "my_recognizer",
      "config": {
        "custom_setting": "value"
      }
    }
  ],
  "operators": [
    {
      "name": "presidio_operator",
      "config": {
        "anonymization_method": "replace"
      }
    }
  ]
}
```

### How to Add a New Operator

#### Step 1: Create the Operator Plugin

Create a new file: `pii_deid_service/plugins/builtin/operators/my_operator.py`

```python
from typing import List, Dict, Any
from pii_deid_service.plugins.base import BaseOperatorPlugin

class MyOperatorPlugin(BaseOperatorPlugin):
    def __init__(self):
        super().__init__()
        self.name = "my_operator"
        self.version = "1.0.0"
        self.description = "My custom anonymization operator"
    
    def create_operator(self, config: Dict[str, Any]):
        """Create and return an operator instance."""
        return MyOperator(config)
    
    def validate_config(self, config: Dict[str, Any]) -> List[str]:
        """Validate configuration and return any errors."""
        errors = []
        # Add your validation logic here
        return errors

class MyOperator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        # Initialize your operator here
    
    def apply(self, text: str, entities: List[Dict[str, Any]]) -> str:
        """Apply anonymization to text based on detected entities."""
        result = text
        
        # Sort entities by start position (reverse order to avoid index issues)
        sorted_entities = sorted(entities, key=lambda x: x['start'], reverse=True)
        
        for entity in sorted_entities:
            start = entity['start']
            end = entity['end']
            entity_type = entity['entity_type']
            
            # Replace with anonymized version
            replacement = f"[{entity_type}]"
            result = result[:start] + replacement + result[end:]
        
        return result
```

#### Step 2: Use the New Operator

```json
{
  "name": "my_custom_pipeline",
  "description": "Pipeline using my custom operator",
  "models": [],
  "recognizers": [
    {
      "name": "presidio_recognizer",
      "config": {
        "language": "en",
        "entities": ["PERSON", "EMAIL"]
      }
    }
  ],
  "operators": [
    {
      "name": "my_operator",
      "config": {
        "custom_setting": "value"
      }
    }
  ]
}
```

### How to Add a New Model

#### Step 1: Create the Model Plugin

Create a new file: `pii_deid_service/plugins/builtin/models/my_model.py`

```python
from typing import Dict, Any
from pii_deid_service.plugins.base import BaseModelPlugin

class MyModelPlugin(BaseModelPlugin):
    def __init__(self):
        super().__init__()
        self.name = "my_model"
        self.version = "1.0.0"
        self.description = "My custom AI model"
    
    def create_model(self, config: Dict[str, Any]):
        """Create and return a model instance."""
        return MyModel(config)
    
    def validate_config(self, config: Dict[str, Any]) -> List[str]:
        """Validate configuration and return any errors."""
        errors = []
        # Add your validation logic here
        return errors

class MyModel:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        # Initialize your model here
    
    def process(self, text: str) -> str:
        """Process text using the model."""
        # Add your model processing logic here
        return text
```

### Best Practices for Adding Components

1. **Follow the Plugin Pattern**: Always inherit from the appropriate base class
2. **Validate Configurations**: Always validate input configurations
3. **Handle Errors Gracefully**: Provide meaningful error messages
4. **Document Your Component**: Include clear descriptions and examples
5. **Test Your Component**: Create tests to ensure it works correctly
6. **Use Type Hints**: Make your code more readable and maintainable

---

## 🔧 Configuration Management

### Understanding Configuration Files

#### Service Configuration
The service configuration (`user_configs/service_config.json`) controls the overall behavior of the system:

```json
{
  "service_name": "PII De-identification Service",
  "version": "1.0.0",
  "description": "Modular PII detection and anonymization service",
  "config_paths": {
    "pipelines": "user_configs/pipelines",
    "models": "user_configs/models",
    "recognizers": "user_configs/recognizers",
    "operators": "user_configs/operators"
  },
  "logging": {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  }
}
```

#### Pipeline Configuration
Pipeline configurations define how text processing should work:

```json
{
  "name": "my_pipeline",
  "description": "My custom pipeline",
  "models": [
    {
      "name": "spacy_model",
      "config": {
        "model": "en_core_web_sm"
      }
    }
  ],
  "recognizers": [
    {
      "name": "presidio_recognizer",
      "config": {
        "language": "en",
        "entities": ["PERSON", "EMAIL", "PHONE_NUMBER"],
        "confidence_threshold": 0.5
      }
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

### Configuration Validation

The system automatically validates configurations:

1. **Schema Validation**: Ensures configuration follows the correct structure
2. **Component Validation**: Checks if specified components exist
3. **Dependency Validation**: Ensures all required dependencies are available
4. **Value Validation**: Validates configuration values are within acceptable ranges

### Dynamic Configuration

You can change configurations without restarting the system:

```python
# Load new configuration
with open("new_pipeline_config.json", "r") as f:
    new_config = json.load(f)

# Build new pipeline
pipeline = builder.build_pipeline(new_config)

# Use new pipeline
result = process_text(pipeline, text)
```

---

## 🧪 Testing and Validation

### Running Tests

#### 1. **Complete System Test**
```bash
python -m pii_deid_service.tests.test_complete_system
```

This test:
- Tests all phases of the system
- Validates configurations
- Tests plugin system
- Tests pipeline building
- Tests complete integration

#### 2. **Plugin System Test**
```bash
python -m pii_deid_service.tests.test_plugin_system
```

This test:
- Tests plugin discovery
- Tests plugin registration
- Tests plugin validation
- Tests plugin creation

#### 3. **Pipeline Architecture Test**
```bash
python -m pii_deid_service.tests.test_pipeline_architecture
```

This test:
- Tests pipeline building
- Tests pipeline validation
- Tests pipeline monitoring
- Tests pipeline processing

### Creating Your Own Tests

#### Example Test Structure
```python
def test_my_component():
    """Test my custom component."""
    print("Testing my component...")
    
    try:
        # Test component creation
        component = create_my_component()
        print("✅ Component created successfully")
        
        # Test component functionality
        result = component.process("test text")
        print(f"✅ Component processed text: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Run all tests."""
    tests = [
        test_my_component,
        # Add more tests here
    ]
    
    results = {}
    for test in tests:
        results[test.__name__] = test()
    
    # Print results
    for test_name, success in results.items():
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    return all(results.values())

if __name__ == "__main__":
    main()
```

### Validation Best Practices

1. **Test Component Creation**: Ensure components can be created with valid configs
2. **Test Error Handling**: Ensure components handle errors gracefully
3. **Test Edge Cases**: Test with empty text, very long text, special characters
4. **Test Performance**: Ensure components perform reasonably well
5. **Test Integration**: Ensure components work with the rest of the system

---

## 🚀 Advanced Usage

### Custom Processing Logic

You can create custom processing logic by extending the pipeline:

```python
def custom_text_processor(pipeline, text):
    """Custom text processing with additional logic."""
    
    # Pre-processing
    text = text.strip()
    text = text.lower()
    
    # Use pipeline for PII detection and anonymization
    result = process_with_pipeline(pipeline, text)
    
    # Post-processing
    result = result.upper()
    
    return result

# Use custom processor
pipeline = builder.build_pipeline(config)
result = custom_text_processor(pipeline, "Hello, my name is John Doe")
```

### Batch Processing

Process multiple texts efficiently:

```python
def batch_process(pipeline, texts):
    """Process multiple texts in batch."""
    results = []
    
    for i, text in enumerate(texts):
        try:
            result = process_with_pipeline(pipeline, text)
            results.append({
                'index': i,
                'original': text,
                'processed': result,
                'success': True
            })
        except Exception as e:
            results.append({
                'index': i,
                'original': text,
                'error': str(e),
                'success': False
            })
    
    return results

# Use batch processing
texts = [
    "Hello, my name is John Doe",
    "Contact me at john@example.com",
    "My phone number is 555-123-4567"
]

results = batch_process(pipeline, texts)
for result in results:
    if result['success']:
        print(f"✅ {result['processed']}")
    else:
        print(f"❌ Error: {result['error']}")
```

### Performance Monitoring

Monitor pipeline performance:

```python
from pii_deid_service.pipeline.monitor import PipelineMonitor

def process_with_monitoring(pipeline, text):
    """Process text with performance monitoring."""
    
    # Create monitor
    monitor = PipelineMonitor("my_pipeline")
    monitor.start_processing(1)
    
    try:
        # Process text
        result = process_with_pipeline(pipeline, text)
        
        # Update progress
        monitor.update_progress(entities_found=5)  # Example
        
        # Complete processing
        monitor.complete_processing()
        
        # Get summary
        summary = monitor.get_summary()
        print(f"Processing time: {summary['processing_time']:.2f}s")
        print(f"Entities detected: {summary['entities_detected']}")
        
        return result
        
    except Exception as e:
        monitor.mark_failed(str(e))
        raise
```

---

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 1. **Import Errors**
**Problem**: `ModuleNotFoundError: No module named 'pii_deid_service'`

**Solution**:
```bash
# Make sure you're in the project root directory
cd pii-deid-service-main

# Install the package in development mode
pip install -e .

# Or add the project root to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

#### 2. **Configuration Not Found**
**Problem**: `FileNotFoundError: No such file or directory: 'config.json'`

**Solution**:
- Check if configuration files exist in the correct location
- Verify file paths in your code
- Use absolute paths or relative paths correctly

#### 3. **Plugin Not Found**
**Problem**: `PluginNotFoundError: Plugin 'my_plugin' not found`

**Solution**:
- Ensure the plugin is properly registered
- Check if the plugin file exists in the correct directory
- Verify the plugin class name matches the registration

#### 4. **Pipeline Build Failure**
**Problem**: `PipelineBuildError: Failed to build pipeline`

**Solution**:
- Check pipeline configuration syntax
- Verify all specified components exist
- Check component configuration values
- Review validation errors in logs

#### 5. **Performance Issues**
**Problem**: Processing is very slow

**Solution**:
- Check if large models are being loaded unnecessarily
- Consider using lighter models for simple tasks
- Implement caching for repeated operations
- Monitor memory usage

### Debugging Tips

#### 1. **Enable Debug Logging**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### 2. **Check Component Status**
```python
# Check if plugin manager is initialized
print(f"Plugin manager initialized: {plugin_manager.is_initialized()}")

# Check available plugins
plugins = plugin_manager.get_available_plugins()
print(f"Available plugins: {plugins}")

# Check pipeline builder status
print(f"Pipeline builder initialized: {builder.is_initialized()}")
```

#### 3. **Validate Configurations**
```python
# Validate service configuration
errors = config_manager.validate_configuration()
if errors:
    print(f"Configuration errors: {errors}")

# Validate pipeline configuration
validator = PluginPipelineValidator()
warnings = validator.validate_pipeline(pipeline)
if warnings:
    print(f"Pipeline warnings: {warnings}")
```

#### 4. **Test Individual Components**
```python
# Test recognizer directly
recognizer = recognizer_factory.create("presidio_recognizer")
entities = recognizer.recognize("Hello, my name is John Doe")
print(f"Detected entities: {entities}")

# Test operator directly
operator = operator_factory.create("presidio_operator")
result = operator.apply("Hello, my name is John Doe", entities)
print(f"Anonymized text: {result}")
```

---

## 📚 Best Practices

### 1. **Configuration Management**
- Use descriptive names for pipelines
- Document configuration options
- Validate configurations before use
- Use version control for configurations

### 2. **Plugin Development**
- Follow the established plugin pattern
- Provide clear documentation
- Include comprehensive tests
- Handle errors gracefully
- Use type hints for better code clarity

### 3. **Performance Optimization**
- Load models only when needed
- Implement caching for expensive operations
- Use appropriate confidence thresholds
- Monitor memory usage
- Consider batch processing for large datasets

### 4. **Security Considerations**
- Validate all input data
- Sanitize configuration values
- Use secure default settings
- Log security-relevant events
- Handle sensitive data appropriately

### 5. **Maintenance**
- Keep dependencies updated
- Monitor for deprecated features
- Maintain comprehensive documentation
- Regular testing and validation
- Performance monitoring

---

## 🎯 Conclusion

This PII De-identification Service is designed to be:
- **Modular**: Easy to add, remove, or modify components
- **Configurable**: Behavior controlled by configuration files
- **Extensible**: Simple to add new capabilities
- **Reliable**: Comprehensive testing and validation
- **User-friendly**: Clear interfaces and documentation

The system provides a solid foundation for PII detection and anonymization while remaining flexible enough to adapt to specific requirements. Whether you're processing customer data, medical records, or any other sensitive information, this system can help ensure privacy and compliance.

By following this guide, you should be able to:
- Understand how the system works
- Use the system effectively
- Add new components as needed
- Troubleshoot common issues
- Maintain and extend the system

Remember that this is a living system - as your needs evolve, the system can evolve with you through its modular design and plugin architecture. 