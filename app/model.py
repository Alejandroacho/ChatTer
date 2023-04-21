import os

from llama_cpp import Llama


def get_model_type() -> str:
    print("You can use the LIGHT or the HEAVY model (in terms of cpu usage).")
    while True:
        model_type: str = input("Do you want to use the LIGHT or the HEAVY: ")
        if model_type not in ["light", "heavy"]:
            print("Invalid model type, please try again.")
        else:
            break
    return model_type

def get_current_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))

def get_model() -> Llama:
    model_type: str = get_model_type()
    model_path: str = f"{get_current_path()}/models/{model_type}.bin"
    model: Llama = Llama(model_path=model_path, verbose=False)
    return model
