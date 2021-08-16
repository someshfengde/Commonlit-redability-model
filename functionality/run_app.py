import tensorflow as tf
import streamlit as st
import gdown
import os
import tensorflow_text as text
import tensorflow_hub as hub
EXTERNAL_DEPENDENCIES = {
    "bert_model.h5": {
        "url": "https://drive.google.com/uc?id=1hGICINTrArHII2D7PIv9GCwlWk0MCpqY",
        "size": 429009
    }
}


def download_file(file_path):
    # Don't download the file twice. (If possible, verify the download using the file length.)
    if os.path.exists(file_path):
        print(os.path.getsize('./' + file_path) ==
              EXTERNAL_DEPENDENCIES[file_path]["size"])

        if os.path.getsize(file_path) == EXTERNAL_DEPENDENCIES[file_path]["size"]:
            st.warning('model already there haha')
            return

    try:
        weights_warning = st.warning("Downloading %s..." % file_path)
        gdown.download(
            EXTERNAL_DEPENDENCIES[file_path]['url'], output=file_path)
        st.warning('download finished')
        print('downloading the model')
    finally:
        st.write('thanks for the patience')


def load_model():
    print('loading model called')
    download_file(file_path='bert_model.5')
    model = tf.keras.load_model("./bert_model.h5")
    return model


def get_prediction(textual_data, model):
    predictions = model.predict(textual_data)
    return predictions


def run_app():
    print('runapp called')
    textual_data = st.text_input(label="enter the passage here", max_chars=500)
    model = load_model()
    prediction = get_prediction(textual_data, model)

    st.write(prediction)
    return prediction
