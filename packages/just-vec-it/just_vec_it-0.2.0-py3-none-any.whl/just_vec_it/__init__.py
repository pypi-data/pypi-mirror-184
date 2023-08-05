__version__ = '0.2.0'
import tensorflow_hub
import tensorflow_text

model = {}

def load_model(dir="/home/andrew/Models/universal-text"):
    model["text"] = tensorflow_hub.load(dir)


def get_vecs(texts):
    return model["text"](texts)
