import os
from kervi.controllers.controller import Controller
from kervi.values import *
from kervi.actions import action 
from PIL import Image, ImageDraw

class Display(Controller):
    def __init__(self, display_id, name, device_driver):
        Controller.__init__(self, display_id, name)
        self._device = device_driver
        self.text = self.inputs.add("text", "Text", StringValue)
        self._bitmap = None
        self._active = False
        self._font = self._get_font()
        self._line_height = 32

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

    #@active.set_interupt
    #def active_interupt(self):
    #    self._active = False
    #    self._device.enable_display(self._active)

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

    def input_changed(self, changed_input):
        if changed_input == self.text:
            if self._device.display_type == "char":
                self._device.message(self.text.value)
            else:
                image = Image.new('1', size=(self._device.width, self._device.height))
                draw = ImageDraw.Draw(image)
                draw.text((0, 0), self.text.value, font=self._font)
                self._device.image(image)
                self._device.display()
                