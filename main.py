import farm

farm.init()

# choose mode: "yield", "speed", "balanced", "pumpkin"
current_mode = "balanced"

while True:
    farm.plant_all(current_mode)

