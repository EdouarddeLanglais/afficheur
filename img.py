import  displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import bitmap_label

c4_gc = 0
c4_za = 0
b14 = 0
rp14 = 0
b32 = 0
t32 = 0

label_c4gc = "0"
label_c4za = "0"
label_14b = "0"
label_14rp = "0"
label_b32 = "0"
label_t32 = "0"

temperature = 0
icone = 0
meteo = 0
heure = 0
date = 0
couleur = 0

memo = 0

bus = [c4_gc, c4_za, b14, rp14, b32, t32]
labels_bus = [label_c4gc, label_c4za, label_14b, label_14rp, label_b32, label_t32]

#Arial 16px
font16 = bitmap_font.load_font("/fonts/Arial-16.bdf")
font16.load_glyphs(b'abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890- ()')

#Arial 24bpx
font24b = bitmap_font.load_font("/fonts/Arial-Bold-24.bdf")
font24b.load_glyphs(b'abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890- ()')

file_01d = open("/images/01d.bmp", "rb")
d01 = displayio.OnDiskBitmap(file_01d)
d01_sprite = displayio.TileGrid(d01, pixel_shader=getattr(d01, 'pixel_shader', displayio.ColorConverter()))

file_01n = open("/images/01n.bmp", "rb")
n01 = displayio.OnDiskBitmap(file_01n)
n01_sprite = displayio.TileGrid(n01, pixel_shader=getattr(n01, 'pixel_shader', displayio.ColorConverter()))

file_02d = open("/images/02d.bmp", "rb")
d02 = displayio.OnDiskBitmap(file_02d)
d02_sprite = displayio.TileGrid(d02, pixel_shader=getattr(d02, 'pixel_shader', displayio.ColorConverter()))

file_02n = open("/images/02n.bmp", "rb")
n02 = displayio.OnDiskBitmap(file_02n)
n02_sprite = displayio.TileGrid(n02, pixel_shader=getattr(n02, 'pixel_shader', displayio.ColorConverter()))

file_03d = open("/images/03d.bmp", "rb")
d03 = displayio.OnDiskBitmap(file_03d)
d03_sprite = displayio.TileGrid(d03, pixel_shader=getattr(d03, 'pixel_shader', displayio.ColorConverter()))

file_03n = open("/images/02n.bmp", "rb")
n03 = displayio.OnDiskBitmap(file_03n)
n03_sprite = displayio.TileGrid(n03, pixel_shader=getattr(n03, 'pixel_shader', displayio.ColorConverter()))

file_04d = open("/images/04d.bmp", "rb")
d04 = displayio.OnDiskBitmap(file_04d)
d04_sprite = displayio.TileGrid(d04, pixel_shader=getattr(d04, 'pixel_shader', displayio.ColorConverter()))

file_04n = open("/images/02n.bmp", "rb")
n04 = displayio.OnDiskBitmap(file_04n)
n04_sprite = displayio.TileGrid(n04, pixel_shader=getattr(n04, 'pixel_shader', displayio.ColorConverter()))

file_09d = open("/images/09d.bmp", "rb")
d09 = displayio.OnDiskBitmap(file_09d)
d09_sprite = displayio.TileGrid(d09, pixel_shader=getattr(d09, 'pixel_shader', displayio.ColorConverter()))

file_09n = open("/images/09n.bmp", "rb")
n09 = displayio.OnDiskBitmap(file_09n)
n09_sprite = displayio.TileGrid(n09, pixel_shader=getattr(n09, 'pixel_shader', displayio.ColorConverter()))

file_10d = open("/images/10d.bmp", "rb")
d10 = displayio.OnDiskBitmap(file_10d)
d10_sprite = displayio.TileGrid(d10, pixel_shader=getattr(d10, 'pixel_shader', displayio.ColorConverter()))

file_10n = open("/images/10n.bmp", "rb")
n10 = displayio.OnDiskBitmap(file_10n)
n10_sprite = displayio.TileGrid(n10, pixel_shader=getattr(n10, 'pixel_shader', displayio.ColorConverter()))

file_11d = open("/images/11d.bmp", "rb")
d11 = displayio.OnDiskBitmap(file_11d)
d11_sprite = displayio.TileGrid(d11, pixel_shader=getattr(d11, 'pixel_shader', displayio.ColorConverter()))

file_11n = open("/images/11n.bmp", "rb")
n11 = displayio.OnDiskBitmap(file_11n)
n11_sprite = displayio.TileGrid(n11, pixel_shader=getattr(n11, 'pixel_shader', displayio.ColorConverter()))

file_13d = open("/images/13d.bmp", "rb")
d13 = displayio.OnDiskBitmap(file_13d)
d13_sprite = displayio.TileGrid(d13, pixel_shader=getattr(d13, 'pixel_shader', displayio.ColorConverter()))

file_13n = open("/images/13n.bmp", "rb")
n13 = displayio.OnDiskBitmap(file_13n)
n13_sprite = displayio.TileGrid(n13, pixel_shader=getattr(n13, 'pixel_shader', displayio.ColorConverter()))

file_50d = open("/images/50d.bmp", "rb")
d50 = displayio.OnDiskBitmap(file_50d)
d50_sprite = displayio.TileGrid(d50, pixel_shader=getattr(d50, 'pixel_shader', displayio.ColorConverter()))

file_50n = open("/images/50n.bmp", "rb")
n50 = displayio.OnDiskBitmap(file_50n)
n50_sprite = displayio.TileGrid(n50, pixel_shader=getattr(n50, 'pixel_shader', displayio.ColorConverter()))

met1 = ["01d", "01n", "02d", "02n", "03d", "03n", "04d", "04n", "09d", "09n", "10d", "10n", "11d", "11n", "13d", "13n", "50d", "50n"]
met2 = [d01_sprite, n01_sprite, d02_sprite, n02_sprite, d03_sprite, n03_sprite, d04_sprite, n04_sprite, d09_sprite, n09_sprite, d10_sprite, n10_sprite, d11_sprite, n11_sprite, d13_sprite, n13_sprite, d50_sprite, n50_sprite]

file_accueil = open("/images/accueil.bmp", "rb")
accueil = displayio.OnDiskBitmap(file_accueil)
accueil_sprite = displayio.TileGrid(accueil, pixel_shader=getattr(accueil, 'pixel_shader', displayio.ColorConverter()))

file_bus_img = open("/images/bus.bmp", "rb")
bus_img = displayio.OnDiskBitmap(file_bus_img)
bus_img_sprite = displayio.TileGrid(bus_img, pixel_shader=getattr(bus, 'pixel_shader', displayio.ColorConverter()))

#Style de label horaires de bus
TAB_BUS_X = 250
#Les coordonnées Y dépendent de chaque bus
TAB_BUS_Y = [72, 92, 132, 152, 192, 212]

for j in range(6):
    labels_bus[j] = bitmap_label.Label(font16, text=str(bus[j]), color=0x000000)
    labels_bus[j].x = TAB_BUS_X
    labels_bus[j].y = TAB_BUS_Y[j]

label_date = bitmap_label.Label(font16, text=str(date), color=0x000000)
label_date.x = 160
label_date.y = 90


label_aheure = bitmap_label.Label(font24b, text=str(heure), color=0x000000)
label_aheure.x = 172
label_aheure.y = 120

label_heure = bitmap_label.Label(font16, text=str(heure), color=0x000000)
label_heure.x = 122
label_heure.y = 230

label2_heure = bitmap_label.Label(font16, text=str(heure), color=couleur)
label2_heure.x = 122
label2_heure.y = 230

label_temp = bitmap_label.Label(font24b, text=str(temperature), color=couleur)
label_temp.x = 210
label_temp.y = 125


label_meteo = bitmap_label.Label(font24b, text=str(meteo), color=couleur)
label_meteo.x = 180
label_meteo.y = 200
