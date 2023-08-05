#MIT License
#Copyright (c) 2017 Tim Wentzlau

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
The display module holds classes for handling displays.
"""
import os
from kervi.controllers.controller import Controller
from kervi.values import *
from kervi.values.value_list import ValueList
from kervi.actions import action 
from PIL import Image, ImageDraw

class Display(Controller):
    r"""
    The display class exposes a display device. 

    :param display_id:
            Id of the display. This id is never displayed it is used to reference the display in code.
    :type display_id: ``str``

    :param name:
            Name of the display.
    :type name: ``str``

    :param device:
        The display device that should be used. Could be one of the displays from the kervi device library
        or a display device driver that inherits from kervi.hal.DisplayDeviceDriver
    :type device: ``DisplayDeviceDriver``

    """
    def __init__(self, display_id, name, device_driver):
        Controller.__init__(self, display_id, name)
        self._device = device_driver
        self.text = self.inputs.add("text", "Text", StringValue)
        self._bitmap = None
        self._active = False
        self._font = self._get_font()
        self._line_height = 32
        self._background_color=(0)
        self._text_color = (255)
        self._pages = {}
        self._active_page = None
    
    def add_page(self, page, default = True):
        r"""
        Add a display page to the display.

        :param page:  Page to be added
        :type display_id: ``DisplayPage``

        :param default: True if this page should be shown upon initialization.
            
        :type name: ``bool``
        """
        self._pages[page.page_id] = page
        page._add_display(self)
        if default or not self._active_page:
            self._active_page = page

    @property
    def display_pages(self):
        r"""
        Returns the display pages added to this display 
        """
        return self._pages

    @property
    def active_page(self):
        r"""
        The current active display page or None if no pages are added.
        """
        return self._active_page

    @action
    def activate_page(self, page_id):
        r"""
        Activates a display page. Content of the active page is shown in the display.

        :param page_id:  Id of page to activate
        :type page_id: ``str``

        """
        if page_id in self._pages:
            self._active_page = self._pages[page_id]
        else:
            raise ValueError("Page with {page_id} not found in page list".format(page_id = page_id))

    @property
    def bitmap(self):
        return self._bitmap

    @bitmap.setter
    def bitmap(self, value):
        self._bitmap = value

    @action
    def active(self, state=True):
        self._active = state
        self._device.enable_display(self._active)

    @active.set_interrupt
    def active_interupt(self):
        self._active = False
        self._device.enable_display(self._active)

    @action
    def scroll_v(self):
        pass

    @action
    def scroll_h(self):
        pass

    def _get_font(self, name="Fanwood", size=16):
        """
        Returns a font that can be used by pil image functions.
        This default font is "Fanwood" that is available on all platforms.
        """
        import kervi.vision as vision
        from PIL import ImageFont
        vision_path = os.path.dirname(vision.__file__)
        fontpath = os.path.join(vision_path, "fonts", name + ".otf")
        font = ImageFont.truetype(fontpath, 32)
        return font

    
    def _page_changed(self, changed_page):
        if self._active_page == changed_page:
            self.text.value = changed_page.text
    
    def input_changed(self, changed_input):
        if changed_input == self.text:
            if self._device.display_type == "char":
                self._device.message(self.text.value)
            else:
                image = Image.new('1', size=(self._device.width, self._device.height), color=self._background_color)
                draw = ImageDraw.Draw(image)
                draw.text((0, 0), self.text.value, font=self._font, fill=self._text_color)
                self._device.image(image)
                self._device.display()
                
    def controller_start(self):
        if self._active_page:
            self._active_page._render()

    def controller_exit(self):
        pass


class _DisplayLink:
    def __init__(self, value, value_id, x=0, y=0, size=0):
        self.value = value
        self.value_id = value_id
        self.x= x
        self.y = y
        self.size = size

class DisplayPage(Controller):
    def __init__(self, page_id, name = None):
        Controller.__init__(self, page_id, name)
        self._template = ""
        self._links = {}
        self._displays = []
        self._text = None

    def _add_display(self, display):
        self._displays.append(display)
    
   
    @property
    def text(self):
        return self._text
   
    @property
    def page_id(self):
        return self.component_id 

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        self._template = value
    
    def _render(self):
        kwargs = {}
        for link_id in self._links:
            link = self._links[link_id]
            kwargs[link.value_id] = link.value.value
        self._text = self.template.format(self._template, **kwargs)
        for display in self._displays:
            display._page_changed(self) 
    
    def _transform(self, v, format):
        if format:
            return str.format(v, format)
        else:
            return str(v)
    
    def input_changed(self, value):
        self._render()


    def link_value(self, source, format=None):
        id = None
        if isinstance(source, KerviValue):
            id = source.value_id
        elif isinstance(source, str):
            id = source

        if id:
            value = self.inputs.add(id, id, StringValue)
            value.link_to(source, lambda x: self._transform(x, format))
            self._links[id] = _DisplayLink(value, id)
        else:
            raise ValueError("Source must be a KerviValue or string")