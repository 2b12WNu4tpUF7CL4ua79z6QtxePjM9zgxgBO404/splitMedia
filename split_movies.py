import os
import subprocess
from moviepy.editor import VideoFileClip

# Check if moviepy is installed
try:
    import moviepy
except ImportError:
    # Install moviepy package
    subprocess.run(['pip3', 'install', 'moviepy'])

# Rest of the code...
input_folder = 'files'
output_folder = 'splitFiles'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all media files in the input folder
media_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

for file in media_files:
    # Check if the file is a video file
    if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv'):
        # Load the video file
        video = VideoFileClip(os.path.join(input_folder, file))
        
        # Calculate the duration of the video in seconds
        duration = video.duration
        
        # Split the video into 1-minute segments
        for i in range(0, int(duration), 60):
            start_time = i
            end_time = min(i + 60, duration)
            
            # Extract the segment from the video
            segment = video.subclip(start_time, end_time)
            
            # Generate the output file name
            output_file = os.path.splitext(file)[0] + f'_split_{i}.mp4'
            
            # Save the segment to the output folder
            segment.write_videofile(os.path.join(output_folder, output_file), codec='libx264')
            
        # Close the video file
        video.close()
