from llama_cpp import Llama


def chat_with_the_model(model: Llama) -> None:
    context: str = None
    while True:
        question: str = input("You: ")
        answer: str = get_model_response(model, question, context)
        print("Bot:", answer)
        context: str = f"{context} {question} {answer}"


def get_model_response(model: Llama, question: str, context: str) -> str:
    response: dict = model(
        f"Context: {context} Question: {question} Answer:",
        echo=True,
        stop=["\n", "Question:", "Q:", "Context:"],
        max_tokens=100,
        temperature=0.7
    )
    answer: str = response["choices"][0]["text"].split("Answer:")[1].strip()
    return answer
