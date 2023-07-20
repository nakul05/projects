import boto3   #: The AWS SDK for Python, used to interact with various AWS services.
import io    # Input/output module for handling streams of data.
from PIL import Image   #Python Imaging Library, used for working with images.

# Initializing the AWS services:
rekognition = boto3.client('rekognition', region_name='ap-south-1') 
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')


# Opening and preparing the image:
image = Image.open("C:/Users/Nakul/OneDrive/Desktop/face recognition/testimage/Kid.jpeg")


stream = io.BytesIO()  # temporarily store the image data.
image.save(stream, format="JPEG")
image_binary = stream.getvalue()


# Performing face recognition:
try:
    response = rekognition.search_faces_by_image(
        CollectionId='family_collection',
        Image={'Bytes': image_binary}
    )

    for match in response['FaceMatches']:
        print(match['Face']['FaceId'], match['Face']['Confidence'])

        face = dynamodb.get_item(
            TableName='family_collection',
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )

        if 'Item' in face:
            print("The face identified is:", face['Item']['FullName']['S'])
        else:
            print('No match found in person lookup')
except Exception as e:
    print("Error:", e)
