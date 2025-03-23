import re
from youtube_transcript_api import YouTubeTranscriptApi

youtube_url = "https://www.youtube.com/watch?v=Pwh8wcHTL2E"

# extract video ID with regex
video_id_regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
match = re.search(video_id_regex, youtube_url)



# extract transcript
transcript = YouTubeTranscriptApi.get_transcript(match.group(1))
text_list = [transcript[i]['text'] for i in range(len(transcript))]
transcript_text = '\n'.join(text_list)

print(transcript_text)