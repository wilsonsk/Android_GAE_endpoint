# Android_GAE_endpoint
### [REST_API](https://android-endpoint.appspot.com/home)

---
## Routes

---
### GET
#### GET https://android-endpoint.appspot.com/home/{userId}
###### Makes a GET request for all homes for user with `userId`

#### GET https://android-endpoint.appspot.com/home/{userId}/{homeId}
###### Makes a GET request for home with `homeId` for user with `userId`
---

---
### POST
#### POST https://android-endpoint.appspot.com/home/{userId}
###### Makes a POST request for user with `userId`
---

---
### PATCH
#### PATCH https://android-endpoint.appspot.com/home/{userId}/{homeId}
###### Makes a PATCH request for home with `homeId` for user with `userId`
---

---
### DELETE
#### DELET https://android-endpoint.appspot.com/home/{userId}/{homeId}
###### Makes a DELETE request for home with `homeId` for user with `userId`
---
---

## To Run Locally 
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
	https://github.com/wilsonsk/ReactNativeGAE_RestApi.git
   ```
3. Install Python dependencies in the project's lib directory and install Node dev dependencies.
   Note: App Engine can only import libraries from inside your project directory.

   ```
   cd ReactNativeGAE_RestApi
   pip install -r requirements.txt -t lib
   ```
   
8. Run local server from the command line:

   ```
   dev_appserver.py .
   ```
   Visit the application [http://localhost:8080](http://localhost:8080)

   or

   ```
   python main.py
   ```
   And visit the application on [http://localhost:5000](http://localhost:5000)


See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create a
   project/app id. (App id and project id are identical)
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   gcloud app deploy --project <PROOJECT_ID>
   ```
1. Congratulations!  Your application is now live at your-app-id.appspot.com

### Relational Databases and Datastore
To add persistence to your models, use
[NDB](https://developers.google.com/appengine/docs/python/ndb/) for
scale.  Consider
[CloudSQL](https://developers.google.com/appengine/docs/python/cloud-sql)
if you need a relational database.

### Installing Libraries
See the [Third party
libraries](https://developers.google.com/appengine/docs/python/tools/libraries27)
page for libraries that are already included in the SDK.  To include SDK
libraries, add them in your app.yaml file. Other than libraries included in
the SDK, only pure python libraries may be added to an App Engine project.


