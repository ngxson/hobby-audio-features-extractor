# Audio features extractor

Extract audio features in [Spotify-based format](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features) from your input track (model run locally). This project extends model from [musicnn](https://github.com/jordipons/musicnn).

Docker image: [ngxson/audio_features_extractor](https://hub.docker.com/r/ngxson/audio_features_extractor)

Github repository: [github.com/ngxson/hobby-audio-features-extractor](https://github.com/ngxson/hobby-audio-features-extractor)

Example:

```
python init.py /path/to/file1.mp3 /path/to/file2.wav ...
```

Output:

```
{"acousticness":0.85,"danceability":0.28,"energy":0.08,"instrumentalness":0.02,"speechiness":0.09,"valence":0.19}
{"acousticness":0.91,"danceability":0.31,"energy":0.17,"instrumentalness":0,"speechiness":0.05,"valence":0.35}
```