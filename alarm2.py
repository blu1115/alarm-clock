import datetime as dt
import simpleaudio as sa

file = ('mixkit-city-alert-siren-loop-1008.wav')
hour = int(input('Enter the hour: '))
min = int(input('Enter the minute: '))
a_p = input('Am or Pm: ')

if a_p == ('pm', 'Pm'):
    hour += 12

print('Alarm started')

while True:
    if hour == dt.datetime.now().hour and min == dt.datetime.now().minute:
        print('Wake up')
        w_object = sa.WaveObject.from_wave_file(file)
        p_object = w_object.play()
        p_object.wait_done()
        break

