#CTI-110
#MT51: Bug Collector
#Johnny Lewis
#10/22/2017

# Initialize the accumulator
total = 0

# get the bugs collected for each day.
for day in range(1, 8):
    # Promt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total = total + bugs

# Display the total bugs.
print('you collected a total of', total, 'bugs.')
    
