import re
import os
import base64
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
# Path to your image
image_path = "costumes_user_a/IMG_4707.jpg"
show_theme = "Disney"

# Getting the Base64 string
base64_image = encode_image(image_path)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                { "type": "text", "text": "what acts could the performer create with this costume for a " + show_theme + "-themed show?" },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
)

print(completion.choices[0].message.content)
