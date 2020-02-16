import sys
from moviepy.editor import *
video = VideoFileClip(sys.argv[1])
audio = video.audio
audio.write_audiofile(sys.argv[2])
# write in cmd => '$python extract_audio.py <video_file> <audio_file>'
