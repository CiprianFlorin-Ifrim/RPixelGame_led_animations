import simpleaudio as sa

def sound():
    filename = 'attack.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    
    
sound()