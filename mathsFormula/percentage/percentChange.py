"""
This class takes two @paras to calculate the percentage change of a given 2
numbers.
@args 1 = orig_num_input_1
@args 2 = orig_num_input_2

orig_num_input_1 is the first given number
orig_num_input_2 is the second given number

Formula
Step 1: difference between the numbers = orig_num_input_1 - orig_num_input_2
Step 2: divide the difference = difference between the numbers / orig_num_input_1
Step 3: the percentage change = divided difference * 100

"""

class PercentChange:
    def __init__(self, orig_num_input_1, orig_num_input_2):
        self.orig_num_input_1 = orig_num_input_1
        self.orig_num_input_2 = orig_num_input_2
    
    # =================
    # Step 1: Find the difference between input
    # =================
    def input_difference(self):
        orig_num_input_1 = self.orig_num_input_1
        orig_num_input_2 = self.orig_num_input_2
        input_difference = orig_num_input_1 - orig_num_input_2
        print(f"Input difference: {input_difference}")
        return input_difference
    
    # =================
    # Step 2: Multiply the 'difference between input' by Original input 1
    # =================
    def div_the_difference(self):
        orig_num_input_1 = self.orig_num_input_1
        input_difference = self.input_difference()
        div_diff = input_difference / orig_num_input_1
        return div_diff

    # =================
    # Step 2: Multiply the function div_the_difference() decimal function 
    # by 100 for percentage form.
    # =================
    def workout_percentage_change(self):
        multi_diff = self.div_the_difference()
        percentageDifference = multi_diff * 100
        return print(percentageDifference)