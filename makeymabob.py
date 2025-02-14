makey_bot = {
'wave_pattern':[0,0,0,0,0,0],
'eyes_rgb_status':0,
'rgb_eye_color_1':0,
'rgb_eye_color_2':0,
'7seg_value':0,
'led_1_status':0,
'led_1_blink':0,
'led_2_status':0,
'led_2_blink':0,
'led_3_status':0,
'led_3_blink':0
}
def oaudfbs(thingymabob):
  for bazinger in thingymabob:
    print (bazinger,"=",thingymabob[bazinger])
  key = input("which value do you want to access? ")
  if key in makey_bot:
    print("the value of",key,"is",thingymabob[key])
    change = input("what do you want to change the value to? ")
    thingymabob[key] = change
  else:
    print("that's not in the dictionary.")
while True:
  oaudfbs(makey_bot)
