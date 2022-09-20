from button import make_button
from buzzer_music import play_song
from songs.aadams_family import song as aadams_family
import time
import board


button = make_button(board.D1)
while True:
    if not button.value:
        play_song(aadams_family)
    else:
        time.sleep(0.1)
