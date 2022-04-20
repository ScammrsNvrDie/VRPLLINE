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
    '''
        adding various span type and including a second argument for this function tp define a header span,
        a button span, or frame span so that this function can be more flexible in its naming schema
    '''
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

        "tabs": {

            "empty":true,
            "filled":false

    },

        "frames": {

            "full":0,
            "sub":1,
            "select":2

    }
}"""
    element = json.loads(jsonElements)
    return element[ele][call]

def elemPos(quad, pos):

    jsonPos = """{
    
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

    posXY = json.loads(jsonPos)
    return posXY[quad][pos]

 
print(elemPos("top","right"))
display.set_pen(holoBlue)
    
display.rectangle(elemPos("top","center"),elemPos("top","y") ,span("quarter"),element("header","bold"))
display.update()    