import ffmpeg
import os

def convert_audio(input_file, output_file, bitrate='320k'):
    """
    Convert audio file to the specified bitrate.

    :param input_file: Path to the input audio file.
    :param output_file: Path to the output audio file.
    :param bitrate: Desired audio bitrate (default is '320k').
    """
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, audio_bitrate=bitrate)
            .run(overwrite_output=True)  # Overwrite output file if it exists
        )
        print(f"Conversion successful: {input_file} -> {output_file} at {bitrate}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")

# Example usage
if __name__ == "__main__":
    # List all audio files in the repository
    for filename in os.listdir('.'):
        if filename.endswith('.wav'):  # Change this if you have different audio formats
            output_filename = f"{os.path.splitext(filename)[0]}.wav"  # Change extension to .wav
            convert_audio(filename, output_filename, bitrate='320k')
