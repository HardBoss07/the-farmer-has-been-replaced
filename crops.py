import costs

def generate_pattern(mode):
	size = 32
	pattern = []
	row = 0

	if mode != "balanced":
		# fallback to old logic for yield/speed
		while row < size:
			if mode == "yield":
				if row < 6:
					if row % 2 == 0:
						pattern.append(Entities.Grass)
					else:
						pattern.append(Entities.Bush)
				elif row < 14:
					pattern.append(Entities.Carrot)
				else:
					if row % 2 == 0:
						pattern.append(Entities.Pumpkin)
					else:
						pattern.append(Entities.Tree)
			elif mode == "speed":
				# Cycle through Grass, Bush, Carrot, Sunflower
				cycle = [Entities.Grass, Entities.Bush, Entities.Carrot, Entities.Sunflower]
				index = row % 4
				pattern.append(cycle[index])
			row += 1
		return pattern

	# Balanced mode: ensure all resources have net positive
	# Use a list of tuples instead of dictionary
	resource_crops = [
		(Items.Hay, Entities.Grass),
		(Items.Wood, Entities.Bush),
		(Items.Carrot, Entities.Carrot),
		(Items.Power, Entities.Sunflower),
		(Items.Pumpkin, Entities.Pumpkin)
	]

	resource_count = len(resource_crops)
	while row < size:
		index = row % resource_count
		crop = resource_crops[index][1]  # pick the crop
		pattern.append(crop)
		row += 1

	return pattern

def get_pattern(mode):
	return generate_pattern(mode)
