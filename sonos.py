from soco import SoCo
import soco
speakers = list(soco.discover())

for speaker in speakers:
  print(speaker.player_name, speaker.ip_address)

speakers[0].play()
speakers[0].volume=40
