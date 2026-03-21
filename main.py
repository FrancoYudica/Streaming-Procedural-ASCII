from framework import *
from common import GradientPalette
import math

class WaveSignal(Signal):

    def __init__(self, frequency: float, amplitude: float):
        self.frequency = frequency
        self.amplitude = amplitude

    def sample(self, u: float, t: float, prev_row: list) -> float:
        s = math.sin(t * self.frequency) * self.amplitude
        return 1.0  - abs(s - u)
    

class TestSignal(Signal):

    def sample(self, u: float, t: float, prev_row: list) -> float:
        p = prev_row[self.x]
        return (math.sin(p * u + t) * 0.5 + 0.5) * u

class CompositeSignal(Signal):

    def __init__(self, signals: list):
        self.signals = signals

    def sample(self, u: float, t: float, prev_row: list) -> float:
        return sum(signal.sample(u, t, prev_row) for signal in self.signals) / len(self.signals)


if __name__ == "__main__":
    renderer = Renderer(50, 10) 
    renderer.render(TestSignal(), GradientPalette(" .:-=+*%#@"))