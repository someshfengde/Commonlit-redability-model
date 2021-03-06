import tensorflow as tf
import streamlit as st
import gdown
import os
import tensorflow_text as text
import tensorflow_hub as hub
EXTERNAL_DEPENDENCIES = {
    "bert_model.h5": {
        "url": "https://drive.google.com/uc?id=1hGICINTrArHII2D7PIv9GCwlWk0MCpqY",
        "size": 429016
    }
}


def download_file(file_path):
    # Don't download the file twice. (If possible, verify the download using the file length.)
    if os.path.exists(file_path):
        print(os.path.getsize('./' + file_path) ==
              EXTERNAL_DEPENDENCIES[file_path]["size"])

        if os.path.getsize(file_path) >= EXTERNAL_DEPENDENCIES[file_path]["size"]-29016:
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
    base_layer = hub.KerasLayer(
        'https://tfhub.dev/google/experts/bert/wiki_books/sst2/2', trainable=False)
    download_file(file_path='bert_model.h5')
    model = tf.keras.models.load_model("/app/commonlit-redability-model/bert_model.h5",
                                       custom_objects={
                                           "KerasLayer": base_layer
                                       })
    return model


def get_prediction(textual_data, model):
    predictions = model.predict([textual_data])
    return predictions


def run_app():
    print('runapp called')
    textual_data = st.text_area(
        label="enter the passage here", max_chars=500, height=400)
    model = load_model()
    prediction = get_prediction(textual_data, model)
    verdict = ""
    if prediction <= -2:
        verdict = "really complex passage you should pay more attention"
    elif prediction <= -1:
        verdict = "It's hard but hold on you can do it"
    elif prediction <= 0:
        verdict = "It's not much hard"
    elif prediction > 0:
        verdict = "Simple passage you got this! "
    st.title(verdict)
    return prediction
