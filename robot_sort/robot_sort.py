class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def __repr__(self):
        return f"{self._list}, {self._position}, {self._item}"

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # I need to turn the light on because I'm using that as a boolean to break out of my main loop
        self.set_light_on()

        # I need to swap the initial item so that I can compare against it while I loop
        self.swap_item()

        # This is the Main Loop that should run only once.
        while self.light_is_on() is True:
            # this first loop will make the robot go back to starting position each time
            while self.can_move_left() is True:
                self.move_left()

            # second loop will keep comparing and swapping until it moves to None placeholder
            while self.compare_item() is not None:
                if self.compare_item() is -1:
                    self.swap_item()
                self.move_right()

            # this will swap to get the None back into the robot's hands
            # We need to do this once we are at the end of the sorting algo, because we need to get rid of that None at the end
            self.swap_item()

            # if we can't move right then the sorting has finished and we break out
            if self.can_move_right() is False:
                self.set_light_off()
            else:   # if we can move right, then we still need to go again through the loop
                self.move_right()
                self.swap_item()
        pass

# TEST DATA
# l = [15, 200, 58, 49]

# robot = SortingRobot(l)


# robot.sort()
# print(robot)
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)

"""
1. Understand the question you're being asked.
This is an in place sorting problem

I think I can use a bubble sort in this problem

I must sort only using defined methods. I cannot access any list or variable directly, my only interaction with any variable is to get it via a method.

The difficulty of this problem comes from the constraints. I can't effectively use for loops or index variables since I can't even get the length of the list or keep track of anything.

I will have to use boolean values with While loops that break by checking a boolean.

The next challenge is the None value that the robot is holding via the item property. How do I ensure that at the end of the swapping that the None ends up in the robot's item property. I can use it as a placeholder, and essentially like a variable. When I reach

I need a way to move all the way back to the beginning. At the beginning of the main loop, I'll just add a loop that makes me go left until I can't anymore. Essentially starting at the first position each time.
"""

"""
2. Make a plan.

Try: Bubble Sort

I will initially set the robot light to on, imitating that a robot is active and running through the list.

Then I will swap the first item so that I am no longer holding None. I will be using None as a placeholder throughout my code.

BASE CASE = when the boolean value (the light) is swapped off, it means the last swap is completed and that will break the loop and return the (hopefully) sorted list. This will be triggered by checking if I can or can't move right after my loops

Inside the initial loop, I will have another loop that checks if I can go left, is yes then it will the robot back one and keep looping until I move back to the first position.

The second loop inside the main loop will see if the item held is less than the item at the position. if it is then swap. Then move right, this continues until you reach None.

Once you reach None break out of the second loop and go swap the items to take None into the robot's hands.

Do a final if check. If you reached the end of the list then that means you are done sorting, you can break out of main loop and return list.
If you are not at the end of the list move right, then take the item that you will be comparing in the next iteration of the main loop.

"""

"""
3. Pseudo code

Defining the function with no params except self
    Turn the light on
    Swap to take the first item, leaving none in the first position

    Main loop that runs while the light is on
        First loop that keeps moving you back to the start every time until you can't go any further back left

        After you are certain that you are at the starting position, run another loop is you are not at None
            If robot's item is smaller than position value then swap
            Move right after if statement either way
        
        Do another swap after the second loop to get back the None value

        If the robot can't move right, then you are finished sorting, turn off light and break out of the loop
        Else
            Move Right
            Swap items again so robot should have the item and the position should have the None
            This else block will make you repeat the main loop
"""
