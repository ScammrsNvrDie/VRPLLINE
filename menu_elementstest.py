import picodisplay as display
import json

width = display.get_width()
height = display.get_height()

display.init(bytearray(width * height * 2))

white = display.create_pen(255,255,255)
black = display.create_pen(0,0,0)
holoBlue = display.create_pen(144,222,255)

print(width, height)
def span(call):
    jsonSpan = """{
   "full":240
   "three_quarter":180,
   "half": 120,
   "quarter": 60
}"""
    span = json.loads(jsonSpan)
    return span[call]

def element(ele, call):
    jsonElements = """{
   "header": {
       "bold":23,
       "medium":13,
       "light":3
   },
   "name": "john wick",
   "class": 8,
   "percentage": 75,
   "email": "jhon@pynative.com"
}"""
    element = json.loads(jsonElements)
    return element[ele][call]


 

display.set_pen(white)
    
display.rectangle(0,4,span("quarter"),element("header","bold"))
display.update()    