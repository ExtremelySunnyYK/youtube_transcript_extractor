from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse as urlparse
from pathlib import Path



def main():
    video_url = input("Please Enter the Link of the Youtube Video you want transcribed: ")
    transcript,video_id = get_transcript(video_url)
    write(transcript,video_id)

def get_transcript(video_url):
    url_data = urlparse.urlparse(video_url)
    query = urlparse.parse_qs(url_data.query)
    video_id = query["v"][0]
    print(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=['en'])
    return transcript,video_id

def extract(transcript):
    print(type(transcript))
    text = ""
    for line in transcript:
        text +=line.get("text")+"\n"
    print(text)

def write(transcript,video_id):
    """Write Transcript to file"""
    Path("./output").mkdir(parents=True, exist_ok=True)
    with open(f"./output/{video_id}","w") as f:
        for line in transcript:
            f.writelines(line.get("text")+"\n")


if  __name__ == "__main__":
    main()