import json
import pickle
import numpy as np
import random
import streamlit as st
from streamlit_chat import message
from keras.models import load_model
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

model = load_model("../models/model.h5")
intents = json.loads(open("../data/intents.json").read())
words = pickle.load(open("../models/words.pkl", "rb"))
classes = pickle.load(open("../models/classes.pkl", "rb"))


from typing import List, Dict, Any


def clean_up_sentence(sentence: str) -> List[str]:
    """
    Tokenizes and lemmatizes the input sentence.

    Args:
    sentence: A string representing the input sentence.

    Returns:
    A list of lemmatized words from the input sentence.
    """
    # Tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # Lemmatize each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence: str, words: List[str], show_details: bool = True) -> np.ndarray:
    """
    Creates a bag of words representation for the input sentence.

    Args:
    sentence: A string representing the input sentence.
    words: A list of words in the vocabulary.
    show_details: A boolean indicating whether to print details during processing.

    Returns:
    A binary array indicating the presence of each word in the vocabulary within the input sentence.
    """
    # Tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # Bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # Assign 1 if the current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print(f"Found in bag: {w}")
    return np.array(bag)


def predict_class(sentence: str, model: Any) -> List[Dict[str, str]]:
    """
    Predicts the intent of the input sentence using the provided model.

    Args:
    sentence: A string representing the input sentence.
    model: The trained model for intent classification.

    Returns:
    A list of dictionaries containing the predicted intent and its probability.
    """
    # Filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # Sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints: List[Dict[str, str]], intents_json: Dict[str, Any]) -> str:
    """
    Retrieves a response based on the predicted intent.

    Args:
    ints: A list of dictionaries containing the predicted intent and its probability.
    intents_json: A dictionary containing intent data.

    Returns:
    A response corresponding to the predicted intent.
    """
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result


def chatbot_response(text: str) -> str:
    """
    Generates a response from the chatbot for the input text.

    Args:
    text: A string representing the input text.

    Returns:
    A response from the chatbot based on the input text.
    """
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res


def send_message(input_message):
    msg = input_message.strip()
    if msg != "":
        message(msg, is_user=True)
        res = chatbot_response(msg)
        message(res)


def main():
    st.title("Chat with Bot")
    input_message = st.text_input("Enter message:", "")
    if st.button("Send"):
        send_message(input_message)


if __name__ == "__main__":
    main()
