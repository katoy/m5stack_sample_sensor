from m5stack import *
from m5ui import *
from uiflow import *
import espnow
import wifiCfg
import json

import hat

setScreenColor(0x111111)

hat_BeetleC9 = hat.get(hat.BEETLEC)


espnow.init()
title0 = M5Title(title="Title", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(8, 56, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(43, 57, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
label2 = M5TextBox(26, 86, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
rectangle0 = M5Rect(28, 105, 20, 20, 0xFFFFFF, 0xFFFFFF)

color = None
addr = None
data = None
message = None
left = None
right = None

def set_led():
  global color, addr, data, message, left, right
  color = message['color']
  label2.setText(str(color))
  if color == 'red':
    rectangle0.setBgColor(0xff0000)
    hat_BeetleC9.SetRGB(1, 0xff0000)
  else:
    rectangle0.setBgColor(0xffffff)
    hat_BeetleC9.SetAllRGB(0x000000)

def set_dirction():
  global color, addr, data, message, left, right
  left = message['left']
  right = message['right']
  label0.setText(str(left))
  label1.setText(str(right))
  hat_BeetleC9.SetPulse(0, left)
  hat_BeetleC9.SetPulse(1, right)



def recv_cb(_):
  global color,addr,data,message,left,right
  addr, _, data = espnow.recv_data(encoder='str')
  message = json.loads(data)
  set_dirction()
  set_led()

  pass
espnow.recv_cb(recv_cb)



lcd.setBrightness(1)
setScreenColor(0x000000)
title0.setBgColor(0x330099)
title0.setTitle('Beetcle-C')
