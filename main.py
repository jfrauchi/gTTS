#!/usr/bin/env python3

"""
Sample script to translate text to speech
using the gTTS library and Google's TTS API
"""

import os
import sys
import click
from gtts import gTTS


@click.command()
@click.option("-w", "--words", 
              help="Enter a string you want to convert to an audio file")
@click.option("-f", "--filename", 
              help="Enter file path to text file you want to convert to an audio file")
@click.option("-o", "--output", default="my_file.mp3", 
              show_default=True, help="Choose filname for output file. E.g. 'output.mp3'")
@click.option("-l", "--lang", default="en", show_default=True, help="Choose language")
@click.option("-t", "--tld", default="com", show_default=True, 
              help="Choose language accent by entering a Google Top Level Domain. E.g. 'co.uk'")
@click.option("--slow", default=False, show_default=True, 
              help="Only set to True when you want the text to be read more slowly")
def text_to_speech(words="", filename="", output="my_file.mp3", lang="en", tld="com", slow=False):
    """
    Convert text-to-speech using the gTTS library and Google's TTS API.
    """
    # first check whether both input options were given. We only want one.
    if words and filename:
        print("Please only choose one of the input options, '--words' or '--file', but not both.")
        sys.exit(1)
    # if a string was given, send the string as-is to be converted
    elif words:
        convert_to_speech(text=words, output=output, lang=lang, tld=tld, slow=slow)
        play_audio(output)
    # if a filename was given, open and read the file into a string
    # then send it to be converted
    elif filename:
        try:
            with open(filename, "r") as f:
                text = f.read()
            convert_to_speech(text=text, output=output, lang=lang, tld=tld, slow=slow)
            play_audio(output)
        except FileNotFoundError:
            print(f"Sorry, the file {filename} does not exist.")
    # if no input option was given, print a message and exit
    else:
        print("Please choose one of the input options, '--words' or '--file'.")
        print("Use '--help' to see all options.")
        sys.exit(1)


def convert_to_speech(text, output, lang, tld, slow):
    """
    use Google's API to convert the input text to an audio file
    """
    audio_created = gTTS(text=text, lang=lang, tld=tld,
                        slow=slow)
    audio_created.save(output)


def play_audio(audiofile):
    """
    check which operating system the script is executed from
    and the play the audio file using a cli command
    """
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system(f"mpg123 {audiofile}")
    elif sys.platform == "darwin":
        os.system(f"afplay {audiofile}")
    elif sys.platform == "win32":
        os.system(f"start {audiofile}")


if __name__ == "__main__":
    text_to_speech()
 