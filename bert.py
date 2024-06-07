import tensorflow_hub as hub
import tensorflow_text as text

# Local pretrained model's URL
preprocess_url = "C:/Users/Minh/Downloads/bert-tensorflow2-en-uncased-preprocess-v3"
encoder_url = "C:/Users/Minh/Downloads/bert-tensorflow2-bert-en-uncased-l-12-h-768-a-12-v2"

bert_preprocess_model = hub.KerasLayer(preprocess_url)
bert_model = hub.KerasLayer(encoder_url)


def preprocess(sentence):
    # Tokenize a sentence
    return bert_preprocess_model(sentence)


def word_piece(preprocess_sentence):
    # Return the attribute vector of a sentence
    return bert_model(preprocess_sentence)['pooled_output']
