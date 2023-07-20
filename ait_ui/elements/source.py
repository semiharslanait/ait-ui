from .element import Element
class Source(Element):
    def __init__(self,id = None,value = None , srcset = None , media = None):
        super().__init__(id = id, value = value)
        self.tag = "source"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["srcset"] = srcset
        self.attrs["media"] = media