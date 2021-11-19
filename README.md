# Text-to-Speech using gTTS

Example script to convert text-to-speech using the gTTS library and Google's TTS API.

## Installation

```bash
# clone repo
git clone https://github.com/jfrauchi/TTS.git
# navigate to new folder
cd TTS
# create a virtual environment - e.g. using venv
python -m venv venv
# activate virtual environment - example for Windows
venv\Scripts\activate.bat
# pip install all requirements using requirements.txt
(venv) pip install -r requirements.txt
```

## Usage
```bash
python main.py --help

Usage: main.py [OPTIONS]

  Convert text-to-speech using the gTTS library and Googles TTS API.

Options:
  -w, --words TEXT     Enter a string you want to convert to an audio file
  -f, --filename TEXT  Enter file path to text file you want to convert to an
                       audio file
  -o, --output TEXT    Choose filname for output file. E.g. 'output.mp3'
                       [default: my_file.mp3]
  -l, --lang TEXT      Choose language  [default: en]
  -t, --tld TEXT       Choose language accent by entering a Google Top Level
                       Domain. E.g. 'co.uk'  [default: com]
  --slow BOOLEAN       Only set to True when you want the text to be read more
                       slowly  [default: False]
  --help               Show this message and exit.
```

### String to MP3
```bash
python main.py -w "Well, hello there! Nice to meet you." -o "file.mp3"
python main.py --words "Well, hello there! Nice to meet you." --output "file.mp3"
```
### Text file to MP3
```bash
python main.py -f "lotsofwords.txt" -o "file.mp3"
python main.py --filename "lotsofwords.txt" --output "file.mp3"
```
### Change the language
```bash
python main.py -w "Muy buenos días" -o "file.mp3" -l "es"
python main.py --words "Muy buenos días" --output "file.mp3" --lang "es"
```
### Change the accent
```bash
python main.py -w "Well, hello there! Nice to meet you." -o "file.mp3" -l "en" -t "co.in"
python main.py --words "Well, hello there! Nice to meet you." --output "file.mp3" --lang "en" --tld "co.in"
```


