import tensorflow as tf
import numpy as np

model_audio_features = None
session_audio_features = None


def normalize(arr):
  for i in range(len(arr)):
    arr[i] = arr[i] * 2 - 1


def denormalize(nparr):
  arr = nparr.tolist()
  for i in range(len(arr)):
    arr[i] = round((arr[i] + 1) / 2, 2)
    arr[i] = max(0, arr[i])
    arr[i] = min(1, arr[i])
  return arr


def load_model_audio_features():
  global model_audio_features, session_audio_features
  session_audio_features = tf.compat.v1.Session()
  tf.compat.v1.keras.backend.set_session(session_audio_features)
  model_audio_features = tf.keras.models.load_model(
      './audio_features/musicnn_to_spotify_audio_features.h5')


def convert_spotify_audio_features(taggram):
    global model_audio_features, session_audio_features

    tags_likelihood_mean = np.mean(taggram, axis=0).tolist()
    normalize(tags_likelihood_mean)

    tf.compat.v1.keras.backend.set_session(session_audio_features)
    input_data = np.array([tags_likelihood_mean])
    predictions = model_audio_features.predict(input_data)

    output_data = denormalize(predictions[0])
    output_labels = ['danceability', 'energy', 'speechiness',
                     'acousticness', 'instrumentalness', 'valence']
    output_metadata = {}
    for i in range(len(output_labels)):
      output_metadata[output_labels[i]] = output_data[i]

    return output_metadata
