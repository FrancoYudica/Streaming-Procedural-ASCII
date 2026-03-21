from time import sleep

def step(v: float, edge: float):
    return 0.0 if v < edge else 1.0

def saturate(x: float) -> float:
    return max(0.0, min(1.0, x))


class Signal:
    x = 0
    def sample(self, u: float, t: float, prev_row: list) -> float:
        return 0.0


class PaletteMapper:

    def map(self, intensity: float, t: int) -> str:
        return "+"

class Output:

    def __init__(self):
        self.line_buffer = ""

    def write(self, char: str):
        raise NotImplementedError()

    def newline(self):
        raise NotImplementedError()

class PrintOutput(Output):
    def write(self, char: str):
        self.line_buffer += char + " "

    def newline(self):
        print(self.line_buffer)
        self.line_buffer = ""

class Renderer:

    def __init__(
            self, 
            width: int,
            framerate: int = 10,
            output: Output = PrintOutput()):
        self.width = width
        self.framerate = framerate
        self.output = output

    def render(self, signal: Signal, palette: PaletteMapper):
        t = 0.0
        dt = 1.0 / self.framerate
        signal.width = self.width

        prev_row = [0.0] * self.width

        while True:
            
            for x in range(self.width):
                u: float = float(x) / (self.width - 1)
                signal.x = x
                intensity = signal.sample(u, t, prev_row)
                pixel = palette.map(intensity, t)
                self.output.write(pixel)
                prev_row[x] = intensity

            self.output.newline()
            t += dt
            sleep(dt)