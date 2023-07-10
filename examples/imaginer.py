#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui import socket_handler
from ait_ui.components import Element, Elm
from ait_ui.components import Text
from ait_ui.components import Image
from ait_ui.components import Row
from ait_ui.components import Col
from ait_ui.components import Button
from ait_ui.components import Input
from ait_ui.components import TextArea
from ait_ui.components import Dropzone
from ait_ui.components import Option
from ait_ui.components import Select
from ait_ui.components import Header
from ait_ui.components import Video
from ait_ui.components import Slider
from ait_ui.components.accordion import Accordion
from ait_ui.components.file import File
from ait_ui.components import Label

def on_change(id, value):
    print("changed", id, value)
    Elm("input1").value = value

def on_click(id, value):
    print("clicked", id, value)
    Elm("input1").value = value

def change_slider_value(id, value):
    print("changed", id, value)
    Elm("slider-value-"+id).value = value

isAccordionOpen = True




with Element(id = "imaginer-wrapper") as main:
        main.cls("imaginer-wrapper")
        #Header Row
        with Header() as content:
            content.cls("imaginer-header")
            with Element() as content:
                content.cls("imaginer-header-left")
                Text(value = "Imaginer").style("margin", "0")
            with Element() as content:
                content.cls("imaginer-header-right")
                Text(value = "Imaginer").style("margin", "0")
        #Body Row
        with Element() as content:
            content.cls("imaginer-body-top")
            #Left Col
            with Element() as content:
                content.cls("imaginer-body-left-top")
                Text(value = "Models")
                with Select(id="select1") as select:
                    select.on("change", on_change)
                    Option(value="1")
                    Option(value="2")
                    Option(value="3")
            #Right Col
            with Element() as content:
                content.cls("imaginer-body-right-top")
                Text(value = "Prompt")
                with Element() as content:
                    content.cls("imaginer-body-right-input-wrapper")
                    TextArea(id = "input1", placeholder="Type Here ...").on("change", print("changed"))
            with Element() as content:
                content.cls("imaginer-body-buttonwrapper")
                Button(value = "Generate" , id="imaginer-button").on("click", on_click).style("background-color", "green")
                Button(value = "Clear" , id="imaginer-button").on("click", on_click)
        with Element() as content:
            content.cls("imaginer-body-center")
            #Left Col
            with Element() as content:
                content.cls("imaginer-body-left-center")
                Text(value = "Input")
                File(id = "file1").on("input", print("changed"))
                with Label(id="dropzone1" , usefor="file1") as label:
                   Text(value = "Drag and Drop")
                   Text(value = "- or -")
                   Text(value = "Click to Upload")
            #Right Col
            with Element() as content:
                content.cls("imaginer-body-right-center")
                Text(value = "Output")
                with Element() as content:
                    content.cls("imaginer-body-right-input-wrapper")
        with Element() as content:
            content.cls("imaginer-body-bottom")
            #Left Col
            with Element() as content:
                content.cls("imaginer-body-left-bottom")
                with Accordion().on("click",print("clicked")) as accordion:
                  accordion.on("click", lambda : Accordion.open_accordion())
                  with Element(id="accordion-wrapper") as content:
                    with Element(id="accordion-opener") as content:
                     content.on("click", lambda : print("clicked"))
                     Text(value = "Advanced Options" , id="accordion-text")
                    with Element() as content:
                        content.cls("imaginer-body-left-bottom-top-div")
                        with Element() as content:
                            content.cls("imaginer-body-left-bottom-top-div-left")
                            with Element() as content:
                                content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
                                Text(value = "Low Treshold")
                                Text(value = "50" , id="slider-value-1")
                            Slider(id = "1", min = "0", max = "100", value = "50").style("width", "100%").on("input", change_slider_value)
                        with Element() as content:
                            content.cls("imaginer-body-left-bottom-top-div-left")
                            with Element() as content:
                                content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
                                Text(value = "High Treshold")
                                Text(value = "50", id="slider-value-2")
                            Slider(id = "2", min = "0", max = "100", value = "50").style("width", "100%").on("input", change_slider_value)
                    with Element() as content:
                        content.cls("imaginer-body-left-bottom-top-div")
                        with Element() as content:
                            content.cls("imaginer-body-left-bottom-top-div-left")
                            with Element() as content:
                                content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
                                Text(value = "Temperature")
                                Text(value = "50",id="slider-value-3")
                            Slider(id = "3", min = "0", max = "100", value = "50").style("width", "100%").on("input", change_slider_value)
                    with Element() as content:
                        content.cls("imaginer-body-left-bottom-top-div")
                        with Element() as content:
                            content.cls("imaginer-body-left-bottom-top-div-left")
                            with Element() as content:
                                content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
                                Text(value = "Temperature")
                                Text(value = "50",id="slider-value-4")
                            Slider(id = "4", min = "0", max = "100", value = "50").style("width", "100%").on("input", change_slider_value)
                        with Element() as content:
                            content.cls("imaginer-body-left-bottom-top-div-left")
                            with Element() as content:
                                content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
                                Text(value = "Temperature")
                                Text(value = "50",id="slider-value-5")
                            Slider(id = "5", min = "0", max = "100", value = "50").style("width", "100%").on("input", change_slider_value)    
                #Right Col
            with Element() as content:
                content.cls("imaginer-body-right-bottom")
                Text(value = "Output")
                with Element() as content:
                    content.cls("imaginer-body-right-input-wrapper")

if __name__ == '__main__':
    app.run(ui = main, debug=True)