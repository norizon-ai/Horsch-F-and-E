#!/usr/bin/env python3
"""
Test that reranker models can be loaded correctly.

Usage:
    python evaluation/test_reranker_models.py

This verifies:
1. sentence-transformers CrossEncoder can load each model
2. Models can perform inference on a sample query-passage pair
3. Reports model sizes and load times
"""

import sys
import time
from pathlib import Path

# Add paths for imports
TECHMECH_DIR = Path(__file__).parent.parent
PRODUCTS_DIR = TECHMECH_DIR.parent
REPO_ROOT = PRODUCTS_DIR.parent
sys.path.insert(0, str(REPO_ROOT / "services" / "custom-deepresearch"))

# Models to test
RERANKER_MODELS = {
    "english": "cross-encoder/ms-marco-MiniLM-L-6-v2",
    "multilingual": "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1",
    "german": "deepset/gbert-base-germandpr-reranking",
    # Note: bge-m3 is a larger model, uncomment to test
    # "bge-m3": "BAAI/bge-reranker-v2-m3",
}

# Sample German query-passage pairs for testing
SAMPLE_PAIRS = [
    (
        "Wie funktioniert die Druckluftversorgung der RC-3000?",
        "Die RC-3000 Schneidanlage erfordert eine Druckluftversorgung von mindestens 6 bar. "
        "Der Anschluss erfolgt über einen 3/4 Zoll Schnellkupplung an der Rückseite der Maschine."
    ),
    (
        "Welche Wartungsintervalle gelten für den Antriebsmotor?",
        "Der Antriebsmotor sollte alle 500 Betriebsstunden gewartet werden. "
        "Dies beinhaltet die Überprüfung der Kohlebürsten und die Schmierung der Lager."
    ),
    (
        "Was ist die maximale Schnittgeschwindigkeit?",
        "Die maximale Schnittgeschwindigkeit beträgt 25 m/min bei Standardmaterialien. "
        "Bei gehärteten Stählen reduziert sich diese auf 15 m/min."
    ),
]


def test_model(model_name: str, model_path: str) -> dict:
    """
    Test loading and inference for a single model.

    Returns:
        Dict with test results
    """
    from sentence_transformers import CrossEncoder

    result = {
        "model_name": model_name,
        "model_path": model_path,
        "load_success": False,
        "inference_success": False,
        "load_time_s": 0,
        "inference_time_ms": 0,
        "sample_scores": [],
        "error": None,
    }

    try:
        # Load model
        print(f"\n{'='*60}")
        print(f"Testing: {model_name}")
        print(f"Path: {model_path}")
        print("-" * 60)

        start = time.time()
        model = CrossEncoder(model_path)
        result["load_time_s"] = time.time() - start
        result["load_success"] = True
        print(f"Load time: {result['load_time_s']:.2f}s")

        # Run inference
        start = time.time()
        scores = model.predict(SAMPLE_PAIRS, show_progress_bar=False)
        result["inference_time_ms"] = (time.time() - start) * 1000
        result["inference_success"] = True
        result["sample_scores"] = [float(s) for s in scores]

        print(f"Inference time: {result['inference_time_ms']:.1f}ms for {len(SAMPLE_PAIRS)} pairs")
        print(f"Sample scores: {[f'{s:.4f}' for s in scores]}")
        print("Status: OK")

    except Exception as e:
        result["error"] = str(e)
        print(f"Error: {e}")
        print("Status: FAILED")

    return result


def main():
    print("=" * 60)
    print("Reranker Model Loading Test")
    print("=" * 60)

    results = []

    for model_name, model_path in RERANKER_MODELS.items():
        result = test_model(model_name, model_path)
        results.append(result)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    success_count = sum(1 for r in results if r["load_success"] and r["inference_success"])
    total_count = len(results)

    print(f"\nModels tested: {total_count}")
    print(f"Successful: {success_count}")
    print(f"Failed: {total_count - success_count}")

    print(f"\n{'Model':<15} {'Load(s)':<10} {'Infer(ms)':<12} {'Status':<10}")
    print("-" * 50)

    for r in results:
        status = "OK" if r["load_success"] and r["inference_success"] else "FAILED"
        load_time = f"{r['load_time_s']:.2f}" if r["load_success"] else "N/A"
        infer_time = f"{r['inference_time_ms']:.1f}" if r["inference_success"] else "N/A"
        print(f"{r['model_name']:<15} {load_time:<10} {infer_time:<12} {status:<10}")

    if success_count == total_count:
        print("\nAll models loaded successfully!")
        return 0
    else:
        print("\nSome models failed to load. Check errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
