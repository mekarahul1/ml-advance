import boto3

BUCKET = "imagesofme"
KEY = "rahul4.JPG"
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

def detect_faces(bucket, key, attributes=['ALL'], region="us-west-2"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_faces(
	    Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
	    Attributes=attributes,
	)
	return response['FaceDetails']

for face in detect_faces(BUCKET, KEY):
	print("Face ({Confidence}%)".format(**face))
	# emotions
	for emotion in face['Emotions']:
		print ("  {Type} : {Confidence}%".format(**emotion))
	# quality
	for quality, value in face['Quality'].items():
		print ("  {quality} : {value}".format(quality=quality, value=value))
	# facial features
#	for feature, data in face.items():
#		if feature in FEATURES_BLACKLIST:
#                      print ("  {feature}({data[Value]}) : {data[Confidence]}%".format(feature=feature, data=data))