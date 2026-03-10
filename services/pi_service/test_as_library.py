import json
from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.plugin_schemas import PluginPipelineConfig
from pii_deid_service.pipeline import run_pipeline


def test_anonymization_as_library():
    # Path to the pipeline config (can be changed to any available config)
    config_path = "user_configs/pipelines/flair_with_custom_phone_pipeline.json"
    with open(config_path, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    config = PluginPipelineConfig(**config_data)

    # Build the pipeline
    builder = PluginBasedPipelineBuilder()
    builder.initialize()
    pipeline = builder.build_pipeline(config)

    # Example German text with PII
    text = "Hallo, mein Name ist Hans Müller. Meine Telefonnummer ist +49-30-123-4567. Ich wohne in Berlin."

    # Run the pipeline
    anonymized_text = run_pipeline(pipeline, text)

    print("Original:", text)
    print("Anonymized:", anonymized_text)


if __name__ == "__main__":
    from flair.models import SequenceTagger
    model = SequenceTagger.load("flair/ner-german-large")
    model_dir = "user_configs/models/"
    model.save(model_dir + "ner-german-large.pt")
    test_anonymization_as_library() 