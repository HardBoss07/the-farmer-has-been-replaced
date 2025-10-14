import field
import crops
import watering

def reset_pos():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def new_line():
	if get_pos_y() < get_world_size() - 1:
		move(North)

def prepare_ground():
	size = get_world_size()

	for y in range(size):
		for x in range(size):
			if get_ground_type() == Grounds.Grassland:
				till()
			if x < size - 1:
				move(East)
		if y < size - 1:
			new_line()
	reset_pos()

def is_dead():
	entity = get_entity_type()
	if entity == Entities.Dead_Pumpkin:
		return True
	return False

def harvest_all():
	size = get_world_size()
	right = True

	for y in range(size):
		for x in range(size):
			if can_harvest():
				harvest()

			if x < size - 1:
				if right:
					move(East)
				else:
					move(West)

		if y < size - 1:
			new_line()
			right = not right

	reset_pos()

def pumpkin_mode():
	size = get_world_size()
	right = True
	all_alive = True

	for row in range(size):
		for x in range(size):
			entity = get_entity_type()

			if entity != Entities.Pumpkin or is_dead():
				plant(Entities.Pumpkin)
				all_alive = False

			if x < size - 1:
				if right:
					move(East)
				else:
					move(West)

		if row < size - 1:
			new_line()
			right = not right

	reset_pos()

	if all_alive:
		harvest()

def normal_mode(mode):
	pattern = crops.get_pattern(mode)
	size = get_world_size()
	right = True

	for row in range(size):
		entity = pattern[row]

		for x in range(size):
			field.cycle(entity)
			if x < size - 1:
				if right:
					move(East)
				else:
					move(West)

		if row < size - 1:
			new_line()
			right = not right

	reset_pos()

def plant_all(mode):
	if mode == "pumpkin":
		pumpkin_mode()
	else:
		normal_mode(mode)

def init():
	reset_pos()
	harvest_all()
	prepare_ground()
