# 🔄 Code Flow: From Input to Output

This document provides a high-level overview of how data flows through the modular PII de-identification system—from the moment you provide input text, through pipeline building, entity recognition, post-processing, and final anonymization.

---

## 1. Input Text
- User provides input text (via script, API, or UI).

## 2. Pipeline Building
- The system loads a pipeline configuration (JSON) from `user_configs/pipelines/`.
- The `PluginBasedPipelineBuilder` builds the pipeline:
    - Loads and instantiates all recognizers and operators as plugins.
    - Loads any required models.

## 3. Entity Recognition
- Each recognizer in the pipeline processes the input text.
- Recognizers may use models (e.g., Flair, Transformers) or pattern-based logic.
- All detected entities are collected and merged.

## 4. Post-Processing (Sanitizer)
- The `entity_sanitizer` operator (if present) deduplicates, merges, filters, and prioritizes entities according to config.
- This step ensures clean, non-overlapping, and high-confidence entity results.

## 5. Anonymization
- The final operator (e.g., `presidio_operator`) applies anonymization to the text using the sanitized entities.
- The output is the fully anonymized text.

## 6. Output
- The anonymized text is returned to the user (printed, saved, or sent via API).

---

## 📊 Diagram: High-Level Flow

```mermaid
graph TD
    A[Input Text] --> B[Load Pipeline Config]
    B --> C[Build Pipeline (Plugins)]
    C --> D[Recognizers Detect Entities]
    D --> E[Entity Sanitizer (Post-Processing)]
    E --> F[Anonymization Operator]
    F --> G[Output Anonymized Text]
```

---

## Example: Code Flow in Practice

```python
from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.plugin_schemas import PluginPipelineConfig
from pii_deid_service.pipeline import run_pipeline

# 1. Load pipeline config
config_path = "user_configs/pipelines/flair_with_presidio_phone_pipeline.json"
with open(config_path, "r", encoding="utf-8") as f:
    config_data = json.load(f)
config = PluginPipelineConfig(**config_data)

# 2. Build pipeline
builder = PluginBasedPipelineBuilder()
builder.initialize()
pipeline = builder.build_pipeline(config)

# 3. Run pipeline on input text
text = "John Doe's phone number is +49-30-123-4567 and he lives in Berlin."
anonymized = run_pipeline(pipeline, text)
print(anonymized)
```

---

**For more details, see the [Comprehensive Usage Guide](anonymize_your_text_guide.md) and [Plugin System Details](plugin_details.md).** 