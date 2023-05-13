import subprocess
import time
import os

# Global variable to store the VLC process
vlc_process = None  

# check if file exitst

streamTxtFile = 'streams.txt'
print(streamTxtFile)
print(os.path.isfile(streamTxtFile))
print("Verify Streams.txt is in the same directory, formatted as only the url in a new a line")

# Obtain time in x from user 
print("Time in sec per seconds")
windowTimeInput = input()
windowTime = int(windowTimeInput)

# function to open and close vlc streams
def display_stream(name, rtspstream):
    global vlc_process

    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"  # Path to VLC executable
    stream_url = rtspstream

    # Terminate the previous VLC process if it exists
    if vlc_process is not None:
        vlc_process.terminate()

    # Construct the VLC command
    vlc_command = [vlc_path, "--network-caching=1000", "--rtsp-tcp", stream_url]

    # Open the stream using VLC
    vlc_process = subprocess.Popen(vlc_command)
    
    print(f"Displaying stream: {name}")
    print(f"RTSP Stream URL: {stream_url}")
    print("Ctrl+C to stop playback.")

    try:
        # Wait for x seconds
        time.sleep(windowTime)
    except KeyboardInterrupt:
        # If Ctrl+C is pressed, terminate VLC process
        subprocess.Popen.terminate()
        print("Stream playback stopped.")

# Read the streams.txt file and extract the stream information
with open(streamTxtFile, 'r') as file:
    stream_lines = file.readlines()

# Infinite loop to continuously switch between streams
while True:
# Process each line in the streams.txt file
    for stream in stream_lines:
        stream = stream.strip()
        name = stream  # Use the entire line as the name
        rtspstream = stream  # Use the entire line as the rtspstream
        display_stream(name.strip(), rtspstream.strip())  # Call the display_stream function