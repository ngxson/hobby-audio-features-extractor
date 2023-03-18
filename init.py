import sys
import os
import json
from musicnn_keras.extractor import extractor, load_model_musicnn
from audio_features.musicnn_to_spotify_audio_features import load_model_audio_features, convert_spotify_audio_features

load_model_musicnn()
load_model_audio_features()

files = []

for arg in sys.argv:
  if '.mp3' in arg or '.wav' in arg or '.wma' in arg or '.ogg' in arg:
    if os.path.exists(arg):
      files.append(arg)
    else:
      raise Exception(f"File not exist: {arg}")

if len(files) == 0:
  print('Usage: python init.py /path/to/file1.mp3 /path/to/file2.wav ...')
  exit(0)

for file in files:
  taggram, tags = extractor(file)
  audio_features = convert_spotify_audio_features(taggram)
  print(json.dumps(audio_features))
