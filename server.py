import json
import logging
from flask import Flask, request, jsonify
from musicnn_keras.extractor import extractor, load_model_musicnn
from audio_features.musicnn_to_spotify_audio_features import load_model_audio_features, convert_spotify_audio_features

load_model_musicnn()
load_model_audio_features()

# test: http://localhost:7777/?path=%2Fapp%2Ffile.mp3

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route("/")
def predict():
    path = request.args.get("path", "invalid")
    taggram, tags = extractor(path)
    audio_features = convert_spotify_audio_features(taggram)
    return jsonify(audio_features)


if __name__ == "__main__":
    app.run(debug=False, port=7777, host='0.0.0.0')
