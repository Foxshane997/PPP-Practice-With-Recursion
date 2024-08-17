# Recursion Number Countdown

def count_down(n):

  #  Base case To stop the function when reaches 0
  if n==0:
      return

  #  Recursive case To run the countdown until desired number is reached
  else:
      print(n)
      count_down(n-1)

# test case Counting down from 8 & calling the function with n passed in.
n=8
count_down(n)
