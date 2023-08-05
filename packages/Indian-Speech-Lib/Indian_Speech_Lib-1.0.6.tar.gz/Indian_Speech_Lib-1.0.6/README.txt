This package is a useful library dealing with speech and text in Hindi
For installing package:
sudo pip install Indian-Speech-Lib==1.0.5

Once you have installed then just write up a tester script, for eg. test.py
Then put this line in test.py:
from Indian_Speech_Lib import utils
and then call the below utility functions.

Utility functions:

utils.remove_silence(input_audio):
	given an input audio in WAV format, this function will remove silence periods from it
	and make an audio file named input_audio_rmsilence.wav
	
utils.get_gender(input_url, input_audio = None):
	given an input_url(or input_audio) of a file, this function will try to predict its gender
	It will return 0 for male and 1 for female
	
utils.get_automatic_transcript(input_url, path_to_key, bucket_name, input_audio = None, silence_removal = None):
	this function will return the text corresponding to the input_url(or input_audio) file
	The output will be available in a file named, "AutomaticTranscript.txt"
	path_to_key is the path of the service account key for gcloud and bucket_name is where the audio chunks will be stored
	
utils.get_quality(input_url, input_audio = None):
	given an input url(or input_audio) of a file in wav format, this function will try to predict its gender
	It will return 0 if audio is rejected(poor quality) and 1 if audio is accepted(good quality)


NOTE:
For using automatic transcript utility(function), you need to have google cloud access.
1. Create account on google cloud.
2. Enable google cloud speech api: Go to Navigation menu and select APIs and Services->Library->Speech API(search) and enable it
3. Create a project and a service account for it by navigating to IAM and admin(on Navigation drop down menu) and then go to Service accounts.
4. Generate service account key for the service account created and download the key.
5. This key's path is to be provided in the utility function.
6. Also create a bucket on the Storage menu of Navigation(Drop down menu) and change its settings to public.
7. You also need to set the bucket's permissions for accessing it, i.e. you need to associate your service account with it by enabling your account with Storage Object Admin section of Bucket permissions.
Feel free to contact us at: cs1150341@cse.iitd.ac.in

