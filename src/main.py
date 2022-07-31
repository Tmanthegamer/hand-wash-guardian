import time

from audio.constants import FilePaths
from config import digitalio, GP0, GP1, GP2, LED, WaveFile, AudioOut, alarm

amp = digitalio.DigitalInOut(GP2)
amp.set_direction(digitalio.Direction.OUTPUT)

led = digitalio.DigitalInOut(LED)
led.set_direction(digitalio.Direction.OUTPUT)

sensor = digitalio.DigitalInOut(GP0)
sensor.set_direction(digitalio.Direction.INPUT)
sensor.set_pull(digitalio.Pull.DOWN)

last_state = False
def play_sound():
    # amp.set_value(False)
    wave_file = open(FilePaths.ALERT, "rb")
    wave = WaveFile(wave_file)
    audio = AudioOut(GP1)
    audio.play(wave)
    # led.set_value(True)
    # time.sleep(0.2)
    # amp.set_value(True)
    time.sleep(0.4)
    # amp.set_value(False)
    # led.set_value(False)
    audio.deinit()

sensor.set_value(True)
if True:
# while True:
    value = sensor.get_value()
    if value != last_state:
        last_state = value
        if value:
            play_sound()
    # time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 5)
    # alarm.light_sleep_until_alarms(time_alarm)
