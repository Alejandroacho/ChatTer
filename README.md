# ChatTer
This is a simple terminal interface to interact with [Vicuna model](https://vicuna.lmsys.org/). This interface uses both:
- [echeada model](https://huggingface.co/eachadea/ggml-vicuna-13b-1.1).
- [anon8231489123 model](https://huggingface.co/anon8231489123/vicuna-13b-GPTQ-4bit-128g).

## Requirements
- [Python](https://www.python.org/downloads/).
- [Make](https://www.gnu.org/software/make/manual/make.html) (recommended but not needed).

## Instructions
1. Create your python environment.

2. Run this to install the requirements:
    ````
    make install-requirements
    `````

3. Run:
    ````
    make chat
    `````

