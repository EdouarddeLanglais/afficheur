import supervisor
supervisor.disable_autoreload()

import gc
import board
import busio
import json
import img as i
import displayio
import time

from digitalio import DigitalInOut
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_button import Button
import adafruit_touchscreen
###############################################################################
###############################################################################
###############################################################################
display = board.DISPLAY
screen_width = 320
screen_heigth = 240

calqueAcc = displayio.Group(x=0, y=0)
calqueBus = displayio.Group(x=0, y=0)
calqueMet = displayio.Group(x=0, y=0)

Vue_Acc = 1
Vue_Bus = 0
Vue_Met = 0

actu = None

calqueAcc.append(i.accueil_sprite)
calqueBus.append(i.bus_img_sprite)

visible = displayio.Group()

TEXT_URL = "http://192.168.0.37"
###############################################################################
###############################################################################
###############################################################################
try:
    from secrets import secrets
except ImportError:
    print("Cles Wi-FI manquantes dans secrets.py")
    raise

esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

requests.set_socket(socket, esp)

if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("ESP32 found and in idle mode")
print("Firmware vers.", esp.firmware_version)

print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("could not connect to AP, retrying: ", e)
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)

###############################################################################
###############################################################################
###############################################################################
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(320, 240))
###############################################################################
###############################################################################
###############################################################################
def actualisation(url):
    gc.collect()
    print("Fetching text from", url)
    r = requests.get(url)
    data = json.loads(r.text)

    i.temperature = data['temp'] + " C"
    i.icone = str(data['icone'])
    i.meteo = data['meteo']
    i.heure = data['heure']
    i.date = data['date']
    
    for j in range(18):
        if i.icone == i.met1[j]:
            try:
                gc.collect()
                calqueMet.append(i.met2[j])
            except ValueError:
                pass
    
    if i.icone[2:3] == "n": i.couleur = 0xFFFFFF
    else: i.couleur = 0x000000
     
    i.label_heure.text = i.heure
    i.label2_heure.text = i.heure
    i.label_aheure.text = i.heure
    i.label_date.text = i.date
    i.label_temp.text = i.temperature
    i.label_meteo = i.meteo
    
    for j in range(6):
        gc.collect()
        i.bus[j]=str(data['bus'][j])
        i.labels_bus[j].text = i.bus[j]
            
    print(i.heure)
    print(i.bus)
    
        
def hideLayer(j):
    try:
        visible.remove(j)
    except ValueError:
        pass

#Fonction pour afficher un calque
def showLayer(j):
    try:
        visible.append(j)
    except ValueError:
        pass

###############################################################################
###############################################################################
###############################################################################
gc.collect()
start_mem = gc.mem_free()
print( "Point 8 Available memory: {} bytes".format(start_mem))

calqueBus.append(i.label_heure)
for j in range(6):
    calqueBus.append(i.labels_bus[j])

calqueAcc.append(i.label_date)
calqueAcc.append(i.label_aheure)

calqueMet.append(i.label2_heure)
calqueMet.append(i.label_temp)
calqueMet.append(i.label_meteo)
###############################################################################
###############################################################################
###############################################################################
boutons = []

#Boutons lateraux gauche
boutonG_width = 120
boutonG_heigth = 80

#Bouton lateral gauche "Accueil"
bouton_accueil = Button(x=0, y=0,
                    width=boutonG_width, height=boutonG_heigth,
                    label="Accueil", label_font=i.font16, label_color=0xffffff,
                    fill_color=0x5c5b5c, outline_color=0x000000,
                    selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                    selected_label=0x525252)
boutons.append(bouton_accueil)

#Bouton lateral gauche "Horaires bus"
bouton_horaires = Button(x=0, y=80,
                    width=boutonG_width, height=boutonG_heigth,
                    label="Horaires bus", label_font=i.font16, label_color=0xffffff,
                    fill_color=0x5c5b5c, outline_color=0x000000,
                    selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                    selected_label=0x525252)
boutons.append(bouton_horaires)

#Bouton lateral gauche "Meteo"
bouton_meteo = Button(x=0, y=160,
                    width=boutonG_width, height=boutonG_heigth,
                    label="Meteo", label_font=i.font16, label_color=0xffffff,
                    fill_color=0x5c5b5c, outline_color=0x000000,
                    selected_fill=0x1a1a1a, selected_outline=0x2e2e2e,
                    selected_label=0x525252)
boutons.append(bouton_meteo)
###############################################################################
###############################################################################
###############################################################################
showLayer(calqueAcc)

for j in boutons:
    showLayer(j)

board.DISPLAY.show(visible)
   
while True:
    try :
        touch = ts.touch_point
        
        if touch:
            time.sleep(0.5)
            for j, b in enumerate(boutons):
                if b.contains(touch):
                    print("Bouton " + str(j) + " presse")

                    if j == 0 and Vue_Acc != 1:
                        time.sleep(0.5)
                        Vue_Acc = 1
                        Vue_Bus = 0
                        Vue_Met = 0
                    
                        gc.collect()
                        hideLayer(calqueMet)
                        hideLayer(calqueBus)

                        gc.collect()
                        showLayer(calqueAcc)
                        
                        start_mem = gc.mem_free()
                        print( "Point Acc Available memory: {} bytes".format(start_mem) )
                        
                        
                    if j == 1 and Vue_Bus != 1:
                        time.sleep(0.5)
                        Vue_Acc = 0
                        Vue_Bus = 1
                        Vue_Met = 0
                    
                        gc.collect()
                        hideLayer(calqueAcc)
                        hideLayer(calqueMet)

                        gc.collect()
                        showLayer(calqueBus)

                        start_mem = gc.mem_free()
                        print( "Point Bus Available memory: {} bytes".format(start_mem) )
                        
                        
                    if j == 2 and Vue_Met != 1:
                        time.sleep(0.5)
                        Vue_Acc = 0
                        Vue_Bus = 0
                        Vue_Met = 1
                    
                        gc.collect()
                        hideLayer(calqueAcc)
                        hideLayer(calqueBus)

                        gc.collect()
                        showLayer(calqueMet)
                        
                        start_mem = gc.mem_free()
                        print( "Point Met Available memory: {} bytes".format(start_mem) )
                        
                    while ts.touch_point:
                        pass
        
        if (not actu) or (time.monotonic() - actu) > 60:
            try:
                gc.collect()
                print("Place libre avant actualisation : " + str(gc.mem_free()) + " octets")
                actualisation(TEXT_URL)
                actu = time.monotonic()
                gc.collect()
                print("Place libre après actualisation : " + str(gc.mem_free()) + " octets")
            except RuntimeError as e:
                print("Some error occured, retrying! -", e)
        continue
            
    except KeyboardInterrupt:
        break