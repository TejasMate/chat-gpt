import subprocess

def play_audio_file():
    try:
        subprocess.run(["mpg321", "response.mp3"])
    except FileNotFoundError:
        print("Error: mpg321 command not found or not in PATH")
