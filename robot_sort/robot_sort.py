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
        self.set_light_on()

        while self.light_is_on(): # set lights
            
            self.set_light_off() # stop
            self.swap_item() # get initial item

            while self.can_move_right():
                self.move_right() # move right

                if self.compare_item() == 1: # compare
                    self.swap_item()
                    self.set_light_on()
            while self.can_move_left() and self.compare_item() != None: # checking for more moves
                self.move_left()

            self.swap_item() # restart iteration

            self.move_right() # start sort again
        return

        # self.set_light_on()

        # while self.light_is_on(): # set lights
        #     self.set_light_off()
        #     self.swap_item() # grab initial card
        #     # print("cardA", self._item)
        #     # if self.compare_item() == None:
        #     #     return None
            
        #     while self.can_move_right():
        #         self.move_right() # move right
        #         if self.compare_item() == 1: # compare
        #             self.swap_item() # swap made
        #             # print("cardB", self._item)
        #             self.set_light_on() # turn on light
        #         if self.compare_item() == 0:
        #             self.move_left()
        #             self.swap_item()
        #             self.move_right()
        #         if self.compare_item() == -1:
        #             continue
        #         # if self.compare_item() == None:
        #         #     continue
        #             # self.swap_item()
        #             # self.move_left()
        #             # self.swap_item()
        #         # if self.compare_item() == -1:
        #         # if self.compare_item() == None:
        #         #     self.move_left()
        #         #     self.swap_item()
        #         #     self.move_right()
        #     while self.can_move_left():
        #         self.move_left() # move left
        #         if self.compare_item() == None:
        #             # self.move_right
        #             self.swap_item() # place other card
        #             break 
        #     self.move_right() # move restart iteration
        # while self.can_move_right():
        #     self.move_right()
        # self.swap_item() # place remaining card


        # self.set_light_off()

        # while self.light_is_off():
        #     self.set_light_on()
        #     self.swap_item()
        #     self.set_light_on()

        # while self.can_move_right(): # move right
        #     self.move_right()
        #     if self.compare_item() == 1: # compare items
        #         self.swap_item()
        #         self.set_light_on()

        # while self.can_move_left():
        #         # move left
        #         self.move_left()
        #         # if compare item is true, swap item with current item
        #         if self.compare_item() == None:
        #             self.swap_item()
        #             

        # self.move_right()

        # while self.can_move_right():
        #     self.swap_item()
        #     self.set_light_on()
        # else:
        #     # swapped
        #     self.set_light_on()
        

        # while self.can_move_left(): # move left
        #     self.move_left()
        #     if self.compare_item() == None: # compare items
        #         self.swap_item()

        # while self.can_move_left() 
        #         self.move_left()
        #         self.swap_item()
           
        # self.move_right()
            
        #     if not self.can_move_right():
                
        #         self.set_light_off()
            
        # self.move_right() # move over

        # while(self.can_move_right()):
        #     self.move_right()
        # self.swap_item()
    
        # if self.light_is_on():
            # self.sort


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


'''
 what's the point of the light? can robot not move/sort without it? - light needed for swapping - on/off
 can move to either side 


 compare and swap while moving through items - two at a time -> bubble sort

need to pick up first item first to compare to next item

 while not end of list:
    move right
    if item held is larger than item in front of robot:
        swap item
        put other in previous spot - left spot
        move right
        repeat until sorted
    if item held is less than item in front of robot:
        replace item in left spot
        move right
        repeat until sorted
    if item held is equal to item in front of robot:
        replace item to left
        move right
        repeat until sorted
    at end of loop start at beginning
    if swap light stays on 
    when robot completes loop with no swaps light off - robot off.
'''
'''
[0, 41, 58, 49, 26, 15, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 4, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 
76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 
79, 83, 13, 57, 86, 12, 56, 50, 55, None] almost there - meh
'''

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
90, 91, 92, 93, 94, 95, 96, 97, 98, 99] only failing test 5 raceback (most recent call last):
  File "f:/Sprint-Challenge--Algorithms/robot_sort/test_robot.py", line 37, in test_sorting_random_list
    self.assertEqual(robot._list, sorted(self.random_list))
TypeError: '<' not supported between instances of 'NoneType' and 'int'
'''