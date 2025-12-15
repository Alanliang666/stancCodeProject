"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1


def main():
	"""
	Input
		Accepts an indefinite number of temperature inputs; enter -1 to exit
	Output
		four numbers: highest temperature, lowest temperature, average temperature, cold day
	"""
	print('stanCode "Weather Master 4.0"!')
	temperature = int(input('Next temperature: (or -1 to quit)? '))
	if temperature == EXIT:
		print('No temperature were entered')
	else:
		highest = temperature
		lowest = temperature
		sum_data = temperature
		num_of_data = 1
		if temperature < 16:  # Check if it is a cold day
			cold_day = 1
		else:
			cold_day = 0
		while True:
			temperature = int(input('Next temperature: (or -1 to quit)? '))
			if temperature == EXIT:
				break
			if temperature < 16:  # Increment cold day count if temperature is below 16
				cold_day += 1
			if highest < temperature:
				highest = temperature
			elif lowest > temperature:
				lowest = temperature
			sum_data += temperature  # Sum total temperature
			num_of_data += 1  # Increment data count
		average = sum_data / num_of_data
		print("Highest temperature = " + str(highest))
		print("Lowest temperature = " + str(lowest))
		print("Average = " + str(average))
		print(str(cold_day) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
	main()
