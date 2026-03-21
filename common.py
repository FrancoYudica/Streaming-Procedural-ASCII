from framework import PaletteMapper

class GradientPalette(PaletteMapper):
    def __init__(self, gradient: str):
        self.gradient = gradient

    def map(self, intensity, t):
        i = int(intensity * (len(self.gradient) - 1))
        return self.gradient[i % len(self.gradient)]