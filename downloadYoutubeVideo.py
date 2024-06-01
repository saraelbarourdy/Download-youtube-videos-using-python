from pytube import YouTube

# Get the URL from the user
url = input('Enter the URL: ')

# Create a YouTube object
video = YouTube(url)

# Get the video title
video_title = video.title
print(f'Title: {video_title}')

# Get the thumbnail URL
video_thumb = video.thumbnail_url
print(f'Thumbnail URL: {video_thumb}')

# Get the highest resolution stream
stream = video.streams.get_highest_resolution()
print(f'Stream: {stream}')

# Download the video
stream.download()
print('Download completed.')
