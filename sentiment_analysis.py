import joblib
from flask import Flask, render_template
from form import TextForm
import joblib
import pandas as pd
import preprocess
import tensorflow as tf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd14a49dd8532da38ad496aea147cd060'
histories = {}


@app.route('/', methods=['post', 'get'])
def sentiment_analysis():
    form = TextForm()

    if not form.validate_on_submit():

        text = str(form.text.data)
        output = {
            0: "mixed",
            1: "negative",
            2: "neutral",
            3: "positive"
        }

        model = joblib.load("nb_model.pkl")

        text = preprocess.normalize_char_level_mismatch(text)
        text = preprocess.clean_text(text)

        tokenizer = tf.keras.preprocessing.text.Tokenizer(
            num_words=100, oov_token='<OOV>')
        tokenizer.fit_on_texts([text])
        sequences = tokenizer.texts_to_sequences([text])
        padded = tf.keras.preprocessing.sequence.pad_sequences(
            sequences, padding='post', maxlen=100)

        print(model.predict(padded))
        histories[text] = output[model.predict(padded)[0]]

        return render_template("sentiment-analysis.html", form=form, histories=histories)


if __name__ == "__main__":
    app.run(debug=True)
