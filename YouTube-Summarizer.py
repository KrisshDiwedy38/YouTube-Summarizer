import youtube_transcript_api

def get_video_id(video_link):
   pass

def get_video_transcript(video_id):
   pass

def get_video_summary(video_transcript):
   pass

def main():
   video_link = input("Enter YouTube video link: ").strip()
   video_id = get_video_id(video_link)
   video_transcript = get_video_transcript(video_id)
   video_sumamry = get_video_summary(video_transcript)
   return video_sumamry


if __name__ == "__main__":
   main()
