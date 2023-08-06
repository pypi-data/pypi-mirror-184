# mobile AAT setup
> This module helps change the application id of the mobile AAT


```
#| hide
from mobile_aat_setup.change_id import *
```

## How to use?
### Change package name
The function below replaces the middle part of the Android Project's package ID (the default is hilmarzech in com.hilmarzech.mobileaat). Replacing this middle part should be sufficient to avoid conflicts with existing installations and to upload your own version of the app to the playstore.

```
PATH_TO_THE_ANDROID_STUDIO_PROJECT = "example/path"
NEWNAME = "examplename"
change_package_name(PATH_TO_THE_ANDROID_STUDIO_PROJECT, NEWNAME)
```

### Link to Firebase
After changing the package name, add an Android App with the new package name (e.g. "com.examplename.mobileaat") to Firebase. Next download the google-services.json and place it into mobileaat/app.
