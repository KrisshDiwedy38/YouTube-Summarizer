# YouTube Video Summarizer

This tool automatically generates concise summaries of YouTube videos by processing their transcripts. It uses natural language processing to extract the key points and important details from videos, saving you time when researching or browsing content.

## Features

- Extract and process transcripts from YouTube videos
- Generate summaries with customizable length
- Handle videos in multiple languages (prioritizes English)
- Process longer videos by breaking them into manageable chunks
- Adaptively adjust summary length based on original content

## Requirements

- Python 3.6+
- youtube_transcript_api
- transformers
- PyTorch

## Installation

1. Clone this repository or download the script
2. Install required dependencies:

```bash
pip install youtube_transcript_api transformers torch
```

3. Download the BART model (will happen automatically on first run)

## Usage

### Basic Usage

Run the script and enter a YouTube URL when prompted:

```bash
python youtube_summarizer.py
```

### Import as Module

You can also import the main function in your own Python scripts:

```python
from youtube_summarizer import main

video_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
summary = main(video_link)
print(summary)
```

## How It Works

1. **Transcript Extraction**: The tool uses the YouTube Transcript API to fetch the video's transcript
2. **Text Chunking**: Longer transcripts are split into manageable sections
3. **Summarization**: Each chunk is summarized using Facebook's BART-large-CNN model
4. **Consolidation**: For multi-chunk videos, a final summary combines the individual chunk summaries

## Limitations

- Requires videos to have available transcripts
- Performance depends on transcript quality and content type

## Error Handling

The tool handles several potential issues:
- Disabled transcripts
- Missing transcripts
- Unavailable videos (private/deleted)
- Invalid URL formats
- General processing errors

## Acknowledgments

- Uses Meta AI's BART model for text summarization
- Built with the YouTube Transcript API for transcript retrieval