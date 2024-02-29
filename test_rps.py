import pytest
from rps1 import rps  

# These are all test cases relating to a tie situation
def testrpstie():
    # This code will result in a tie
    result = rps("rock", "rock")
   
    assert result == 0, f"Expected 0 (tie), but got {result}"

    # This code will result for paper vs paper would result in a tie
    result = rps("paper", "paper")
    
    assert result == 0, f"Expected 0 (tie), but got {result}"

    # This code will result for Scissors vs Scissors would result in a tie
    result = rps("scissors", "scissors")
   
    assert result == 0, f"Expected 0 (tie), but got {result}"

# These are all test cases for p1 relating to winning scenarios
def testrpsp1wins():
    # This code would result in p1 winning from Rock vs Scissors 
    result = rps("rock", "scissors")
   
    assert result == 1, f"Expected 1 (player1 wins), but got {result}"

    # This code would result in p1 winning from Paper vs Rock 
    result = rps("paper", "rock")
    
    assert result == 1, f"Expected 1 (player1 wins), but got {result}"

    # This code will result in p1 winning from Scissors vs Paper 
    result = rps("scissors", "paper")
    
    assert result == 1, f"Expected 1 (player1 wins), but got {result}"

# These are all test cases for p2 winning scenarios
def testrpsp2wins():
    # This code will result in p2 winning from Scissors vs Rock 
    result = rps("scissors", "rock")
   
    assert result == 2, f"Expected 2 (player2 wins), but got {result}"

    # This code will result in p2 winning from Rock vs Paper 
    result = rps("rock", "paper")
   
    assert result == 2, f"Expected 2 (player2 wins), but got {result}"

    # This code will result in p2 winning Paper vs Scissors 
    result = rps("paper", "scissors")
    
    assert result == 2, f"Expected 2 (player2 wins), but got {result}"



