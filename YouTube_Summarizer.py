"""
Project Overview
The YouTube Transcript Summarizer is a Python-based application that fetches the transcript of a YouTube video using the YouTube Transcript API and then applies Natural Language Processing (NLP) techniques to generate a concise and meaningful summary. This tool helps users quickly understand the core content of long YouTube videos without watching them entirely.

Key Features
   - Fetch YouTube Transcripts: Uses the youtube-transcript-api to retrieve the video’s transcript.
   - Text Preprocessing: Cleans and prepares the transcript for analysis using spaCy or NLTK.
   - Summarization:
      - Extractive Summarization (selecting key sentences) using sumy or NLTK.
      - Abstractive Summarization (generating new summaries) using transformers from Hugging Face.
         - Named Entity Recognition (NER): Highlights key names, locations, and events using spaCy.
         - User Input: Users provide a YouTube video URL, and the system returns a structured summary.
"""