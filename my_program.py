# task is to create python program which prints even numbers below 50

"""
idea to implement:
# we need 50 numbers to traverse and decide that the current number is even or not
then we should write condition which tells us current number is even or not (condition: current_number%2 == 0)
since the number 50 is constant, hence we use constant variable at top
"""
MAX_NUMBER = 50

#traverse 50 numbers from 0 to 50

#helper function
def even_number():
    for i in range(MAX_NUMBER):
        if i%2 == 0:
            print(i)

#function call
def main():
    #function call
    even_number()

if __name__ == "__main__":
    main()