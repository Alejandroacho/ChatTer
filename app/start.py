from llama_cpp import Llama

from chat import chat_with_the_model
from models import download_models_if_needed
from models import get_model


if __name__ == '__main__':
    download_models_if_needed()
    model: Llama = get_model()
    chat_with_the_model(model)
