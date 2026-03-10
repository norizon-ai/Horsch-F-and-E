import json
from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.config_manager import config_manager
from pii_deid_service.pipeline import run_pipeline

def main():
    print("\n🔬 TEST: Flair + Transformer English Pipeline\n" + "="*40)
    # Load pipeline config from file
    config_path = "user_configs/pipelines/flair_with_transformer_pipeline.json"
    pipeline_config = config_manager.load_pipeline_config(config_path)
    builder = PluginBasedPipelineBuilder()
    builder.initialize()
    pipeline = builder.build_pipeline(pipeline_config)

    sample_text = "Omar ist ein Mitarbeiter von Tier0 und hat die nummer 0176/23124515"
    print(f"Original: {sample_text}")
    anonymized = run_pipeline(pipeline, sample_text)
    print(f"Anonymized: {anonymized}")

if __name__ == "__main__":
    main() 