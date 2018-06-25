import box, sys, time, random

if len(sys.argv) != 3:
	print("Three command line arguments required.")
else:
	start = time.time()
	name = sys.argv[1]
	time_limit = float(sys.argv[2])
	remaining = list(range(1, 10))

def lose():
	print("Game Over!\n")
	print("Score for player ", name, ": ", sum(remaining), " points")
	print("Time played: ", round(time.time() - start, 2), " seconds")
	print("Better luck next time >:)")

while (len(remaining) != 0):
	print("Numbers left: ", remaining)
	if sum(remaining) <= 6:
		roll = random.randint(1, 6)
	else:
		roll = random.randint(2, 12)
	if box.isvalid(roll, remaining):
		print("Roll: ", roll)
		current = True
		while current:
			time_elapsed = time.time() - start
			print("Seconds left ", round(time_limit - time_elapsed, 2))
			eliminate = box.parse_input(input("Numbers to eliminate: "), remaining)
			time_elapsed = time.time() - start
			if time_limit - time_elapsed <= 0:
				lose()
				break
			if (len(eliminate) == 0) | (sum(eliminate) != roll):
				print("Invalid input")
			else:
				current = False
			print("\n")
		for i in eliminate:
			remaining.remove(i)
	else:
		lose()
		break
	
if len(remaining) == 0: 
	print("Score for player ", name, ": 0 points")
	print("Time played: ", round(time.time() - start, 2))
	print("Congratulations!! You shut the box!")
