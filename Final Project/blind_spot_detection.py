# File: blind_spot_detection.py

"""
Experiment to detect potential blind spots by presenting a circle stimulus at
random locations and measuring the user's reaction time.

Author: Abdiwahab Ali
"""



# Import necessary libraries
from psychopy import visual, core, event
import random
import csv

# Create a window to display the experiment
win = visual.Window(size=(800, 600),fullscr='yes')
Trials = 40
Blocks = 1

# Create a fixation point to be displayed in the middle of the window


# Create a fixation point using the ShapeStim class and the plus sign coordinates
fix_text = visual.TextStim(win, text='+',color = 'black')
# Create a circle stimulus
circle = visual.Circle(win, radius=0.008, edges=30, lineColor="white")

# Set up a list to store the reaction times and stimulus locations
reaction_times = []
stimulus_locations = []

with open("experiment_data.csv", "w", newline="") as csvfile:
    # Set up the CSV writer
    writer = csv.writer(csvfile)

    # Write the column headers to the file
    writer.writerow(["Block","Trial","reaction_time", "x", "y"])
    # Present the circle stimulus 25 times at random locations
    for block in range(Blocks):
        for trial in range(Trials):
              # Generate a random location for the circle stimulu
              x = random.uniform(-1, 1)
              y = random.uniform(-1, 1)
              circle.setPos([x, y])
              stimulus_locations.append((x, y))
              # Draw the circle stimulus and update the window
              circle.draw()
              fix_text.draw()
              win.flip()
              # Wait for the user to respond (either by pressing a button or after 1 second)
              response = None
              timer = core.CountdownTimer(1.0)
              while response is None:
                if event.getKeys(keyList=["space"]):
                    response = "yes"
                elif timer.getTime() < 0:
                    response = "no"
              # If the user responded "yes", record their reaction time
              if response == "yes":
                reaction_time = timer.getTime() * -1
                reaction_times.append(reaction_time)
                writer.writerow([(block+1),(trial+1),reaction_time, x, y])
            # Clear the screen and wait 100 ms before presenting the next stimulus
              win.flip()
              core.wait(0.1)
      

# After all stimuli have been presented, calculate the average reaction time
average_reaction_time = sum(reaction_times) / len(reaction_times)

# Print the average reaction time to the console
print(f"Average reaction time: {average_reaction_time:.3f} seconds")

# Check for potential blind spots by comparing stimulus locations to response locations
for i, (x, y) in enumerate(stimulus_locations):
    response = "yes" if i < len(reaction_times) else "no"
    print(f"Stimulus at ({x:.2f}, {y:.2f}): {response}")

# Close the window
win.close()
