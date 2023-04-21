from llama_cpp import Llama

from chat import chat_with_the_model
from model import get_model


if __name__ == '__main__':
    model: Llama = get_model()
    chat_with_the_model(model)
