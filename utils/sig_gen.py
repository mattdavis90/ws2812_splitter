RST = 50.0
HI1 = 0.8
LO1 = 0.45
HI0 = 0.4
LO0 = 0.85
RISE = 0.05

time = 0.0

leds = [
    [
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (255, 255, 255),
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (255, 255, 255),
    ],
    [
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (255, 255, 255),
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (255, 255, 255),
    ],
    # [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
    # [(0, 255, 0), (0, 0, 255), (255, 0, 0)],
    # [(0, 0, 255), (255, 0, 0), (0, 255, 0)],
]

signal = []
for step in leds:
    signal.append("R")
    for led in step:
        for colour in led:
            for i in range(8):
                signal.append(1 if ((colour >> i) & 1) else 0)

out = []
for s in signal:
    match s:
        case "R":
            out.append(f"{time+RISE} 0")
            time += RST
            out.append(f"{time} 0")
        case 0:
            out.append(f"{time+RISE} 5000")
            time += HI0
            out.append(f"{time} 5000")
            out.append(f"{time+RISE} 0")
            time += LO0
            out.append(f"{time} 0")
        case 1:
            out.append(f"{time+RISE} 5000")
            time += HI1
            out.append(f"{time} 5000")
            out.append(f"{time+RISE} 0")
            time += LO1
            out.append(f"{time} 0")

print("\n".join(out))
