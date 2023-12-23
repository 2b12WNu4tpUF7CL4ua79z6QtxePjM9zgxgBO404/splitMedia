# Video Splitter

This Python script splits video files into 1-minute segments. It supports `.mp4`, `.avi`, and `.mkv` video formats.

## Dependencies

The script uses the following Python packages:

- `os`
- `subprocess`
- `moviepy`

If `moviepy` is not installed, the script will automatically install it using `pip3`.

## How to Use

1. Place your video files in a folder named `files` in the same directory as the script.
2. Run the script. It will create a new folder named `splitFiles` (if it doesn't already exist) and place the 1-minute video segments there.
3. Each segment will be named according to the original file name with the addition of `_split_{i}`, where `{i}` is the start time of the segment in the original video.

## Code Explanation

The script first checks if `moviepy` is installed and installs it if necessary. It then creates the `splitFiles` directory and gets a list of all media files in the `files` directory.

For each video file, it loads the video, calculates its duration, and splits it into 1-minute segments. Each segment is then saved to the `splitFiles` directory with a unique name. After all segments have been extracted, the video file is closed to free up resources.

## Note

The script uses the `libx264` codec for output video files. Make sure your system supports this codec.
