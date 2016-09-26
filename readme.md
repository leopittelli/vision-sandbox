# Google Cloud Vision API example.
App engine demo using Google Cloud Vision API for OCR on an image. Demo: https://vision-sandbox.appspot.com

## Playing with the API
https://developers.google.com/apis-explorer/#search/vision/vision/v1/vision.images.annotate

You can use a JSON with this structure:
```JSON
{
    "requests": [
        {
            "image": {
                "content": "USE CONTENT FROM img-samples folder"
            }
        },
        {
            "features": [ 
                {
                    "type": "USE A TYPE FROM BELOW"
                }
            ]
        }
    ]
}
```

### Feature types:
| Type                  | Explanation                                                                           |
|-----------------------|---------------------------------------------------------------------------------------|
| TYPE_UNSPECIFIED	    | Unspecified feature type.                                                             |
| FACE_DETECTION	    | Run face detection.                                                                   |
| LANDMARK_DETECTION    | Run landmark detection.                                                               |
| LOGO_DETECTION        | Run logo detection.                                                                   |
| LABEL_DETECTION	    | Run label detection.                                                                  |
| TEXT_DETECTION	    | Run OCR.                                                                              |
| SAFE_SEARCH_DETECTION	| Run various computer vision models to compute image safe-search properties.           |
| IMAGE_PROPERTIES	    | Compute a set of properties about the image (such as the image's dominant colors).    |


## Run the App Engine demo

1. Install gcloud: https://cloud.google.com/sdk/docs/overview
2. Create project and and download your service credentials.json file from the project's console: https://cloud.google.com/vision/docs/quickstart
3. Add the library as explained in: https://cloud.google.com/appengine/docs/python/tools/using-libraries-python-27#vendoring
⋅⋅1. Create `lib` folder.
⋅⋅2. Run `pip install -t lib --upgrade google-api-python-client`
4. Run the app `dev_appserver.py .`