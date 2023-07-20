import boto3
import os

s3 = boto3.resource('s3')

# Get the absolute path of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get list of objects for indexing
images = [
      (os.path.join(script_directory, 'images', '1.jpg'), 'APJ Kalam'),
      (os.path.join(script_directory, 'images', '4.png'), 'Albert Einstein'),
      (os.path.join(script_directory, 'images', '3.jpg'), 'David Bekhm'),
      (os.path.join(script_directory, 'images', '2.jpg'), 'CV Raman'),  
      (os.path.join(script_directory, 'images', '5.jpg'), 'Isaac Newton'),
      (os.path.join(script_directory, 'images', '6.png'), 'Lionel Messi'),
      (os.path.join(script_directory, 'images', '7.jpeg'), 'Nikola Tesla'),
      (os.path.join(script_directory, 'images', '8.jpg'), 'Cristiano Ronaldo'),
      (os.path.join(script_directory, 'images', '9.jpg'), 'Sunil Chhetri'),
      (os.path.join(script_directory, 'images', '10.jpg'), 'Elon Musk')
      (os.path.join(script_directory, 'images', '11.jpeg'), 'Barak Obama')
      (os.path.join(script_directory, 'images', '12.jpeg'), 'Angelina Jolie') ,
      (os.path.join(script_directory, 'images', '13.jpeg'), 'Jeff Bezos'),
      (os.path.join(script_directory, 'images', '14.jpeg'), 'Narendra Modi'),
      (os.path.join(script_directory, 'images', '15.jpeg'), 'Taylor Swift'),
      (os.path.join(script_directory, 'images', '16.jpeg'), 'Bill Gates'),
      (os.path.join(script_directory, 'images', '17.jpeg'), 'Kim Kardashian'),
      (os.path.join(script_directory, 'images', '18.jpeg'), 'Emma Watson'),
      (os.path.join(script_directory, 'images', '19.jpeg'), 'Donald Trump'),
      (os.path.join(script_directory, 'images', '20.jpeg'), 'Serena Williams'),
      (os.path.join(script_directory, 'images', '21.jpeg'), 'Mark Zuckerberg'),
      (os.path.join(script_directory, 'images', '22.jpeg'), 'Adele'),
      (os.path.join(script_directory, 'images', '23.jpeg'), 'Dalai Lama'),
      (os.path.join(script_directory, 'images', '24.jpeg'), 'Vladimir Putin'),
      (os.path.join(script_directory, 'images', '25.jpeg'), 'Ellen_DeGeneres'),
      (os.path.join(script_directory, 'images', '26.jpeg'), 'Rodger Ferderer'),
      (os.path.join(script_directory, 'images', '27.jpeg'), 'Rihanna'),
      (os.path.join(script_directory, 'images', '28.jpeg'), 'Waren Buffett'),
      (os.path.join(script_directory, 'images', '29.jpeg'), 'Queen Elizabeth'),
      (os.path.join(script_directory, 'images', '30.jpeg'), 'LeBron James'),
      (os.path.join(script_directory, 'images', '31.jpeg'), 'Kanye West'),
      (os.path.join(script_directory, 'images', '32.jpeg'), 'Bill Clinton'),
      (os.path.join(script_directory, 'images', '33.jpeg'), 'David Beckham'),
      (os.path.join(script_directory, 'images', '34.jpeg'), 'Tom Hanks'),
      (os.path.join(script_directory, 'images', '35.jpeg'), 'Malala Yousafzai'),
      (os.path.join(script_directory, 'images', '36.jpeg'), 'Oprah Winfrey'),
      (os.path.join(script_directory, 'images', '37.jpeg'), 'JK Rowling'),
      (os.path.join(script_directory, 'images', '38.jpeg'), 'Michael Jordan'),
      (os.path.join(script_directory, 'images', '39.jpeg'), 'Billie Eilish'),
      (os.path.join(script_directory, 'images', '40.jpeg'), 'Shah Rukh Khan'),
      (os.path.join(script_directory, 'images', '41.jpeg'), 'Nakul Mehta'),
      (os.path.join(script_directory, 'images', '42.jpeg'), 'Nakul Mehta'),
      (os.path.join(script_directory, 'images', '43.jpeg'), 'Nakul Mehta'),
      (os.path.join(script_directory, 'images', '44.jpeg'), 'Nakul Mehta')



]

# Iterate through list to upload objects to S3
for image in images:
    file_path = image[0]
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            object = s3.Object('facecollectionbucket123', 'index/' + os.path.basename(file_path))
            ret = object.put(
                Body=file,
                Metadata={'FullName': image[1]}
            )
    else:
        print(f"File not found: {file_path}")
