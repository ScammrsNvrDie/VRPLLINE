import picodisplay as display
import json
from math import trunc
width = display.get_width()
height = display.get_height()

display.init(bytearray(width * height * 2))

white = display.create_pen(255,255,255)
black = display.create_pen(0,0,0)
holoBlue = display.create_pen(144,222,255)

print(width, height)

def span(types, mod):
    '''
        [x] adding various span type and including a second argument for this function tp define a header span,
        a button span, or frame span so that this function can be more flexible in its naming schema
        
        [] added arguments, and reformatted json for adding the additional span types
    '''
    jsonSpan = """{

        "headerSpans": {

            "full":240
            "three_quarter":180,
            "half": 120,
            "quarter": 60
        },

        "buttonSpans": {

            "buttonSmall": 53,
            "buttonMedium": 67,
            "buttonLarge": 83,
            "y": 23

        }    

}"""
    spanType = json.loads(jsonSpan)
    return spanType[types][mod]

def element(ele, call):
    
    jsonElements = """{

        "headers": {

            "bold":23,
            "medium":13,
            "light":3

    },

        "tabs": {
        
            "width": 13,
            "height": 9,
            "empty":true,
            "filled":false

    },

        "frames": {

            "full":0,
            "sub":1,
            "select":2

    }
}"""
    elements = json.loads(jsonElements)
    return elements[ele][call]

def elemPos(quad, pos):
    
    elemPos = """{
    
        "top": {

            "left": 3,
            "center": 95,
            "right": 200,
            "y": 3

        },

        "middle": {

            "left": 3,
            "center": 60,
            "right": 180,
            "y": 69

        },

        "bottom": {

            "left": 3,
            "center": 60,
            "right": 180,
            "y": 100

        }

}"""
    
    posXY = json.loads(elemPos)
    return posXY[quad][pos]


print(elemPos("top","right"))
display.set_pen(holoBlue)
    
display.rectangle(elemPos("top","left"),elemPos("top","y") ,span("headerSpans", "full"), element("headers","light"))
# button test
display.rectangle(elemPos("middle", "center"), elemPos("middle","y"), span("buttonSpans", "buttonSmall"), span("buttonSpans", "y"))

#def textHandler(quad, pos):
    
#    pass
    
    
#textHandler()
    

    

 

display.update()    