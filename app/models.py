import os

from huggingface_hub import hf_hub_download
from llama_cpp import Llama


MODELS: dict = {
    "light": {
        "repo_id": "eachadea/ggml-vicuna-7b-1.1",
        "file": "ggml-vicuna-7b-1.1-q4_1.bin"
    },
    "heavy": {
        "repo_id": "eachadea/ggml-vicuna-13b-1.1",
        "file": "ggml-vicuna-13b-1.1-q4_1.bin"
    }
}


def get_current_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def download_models_if_needed() -> None:
    if not os.path.exists("models/light.bin"):
        download_model("light")
    if not os.path.exists("models/heavy.bin"):
        download_model("heavy")


def download_model(model_type: str) -> None:
    print(f"Downloading the {model_type} model...")
    hf_hub_download(
        repo_id=MODELS[f"{model_type}"]["repo_id"],
        filename=MODELS[f"{model_type}"]["file"],
        local_dir=f"{get_current_path()}/models"
    )


def get_model_type() -> str:
    print("You can use the LIGHT or the HEAVY model (in terms of cpu usage).")
    while True:
        model_type: str = input("Do you want to use the light or the heavy: ")
        if model_type in ["light", "heavy"]:
            break
        print("Invalid model type, please select 'light' or 'heavy'.")
    return model_type


def get_model() -> Llama:
    model_type: str = get_model_type()
    model_name: str = MODELS[f"{model_type}"]["file"]
    model_path: str = f"{get_current_path()}/models/{model_name}"
    model: Llama = Llama(model_path=model_path, verbose=False)
    return model
