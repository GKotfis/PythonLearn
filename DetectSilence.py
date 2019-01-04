import sys
import datetime
from pydub import AudioSegment
from pydub import silence

min_silence_len = 2000
audio_file_name = sys.argv[1]

print('Reading audio file ...')
audio_segment = AudioSegment.from_mp3(audio_file_name)

if len(sys.argv) == 3:
    min_silence_len = sys.argv[2]

print('Detecting silence ...')
audio_chunks = silence.detect_silence(audio_segment, min_silence_len, -48)

if not audio_chunks:
    print('No silence detected', 'green')
else:
    for audio_chunk in audio_chunks:
        # print(audio_chunk)
        print('Detected silence at: {} - {}'.format(datetime.timedelta(milliseconds=audio_chunk[0]), datetime.timedelta(milliseconds=audio_chunk[1])))