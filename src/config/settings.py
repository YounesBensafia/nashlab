from utils.exo1.randomMatrix import random_matrix as matrix
from prompt_toolkit.styles import Style
N = 3
GAME = matrix(N, N)

choice_style = Style([
        ("qmark", "fg:ansiyellow bold"),   
        ("question", "bold"),                  
        ("answer", "fg:ansiyellow bold"),    
        ("pointer", "fg:ansiyellow bold"),     
        ("selected", "fg:ansiyellow"),        
        ("highlighted", "fg:ansiyellow bold")
    ])

choice_question =   [
            "Exercise 1: Remove strictly dominated strategies",
            "Exercise 2: Find dominant strategies",
            "Exercise 3: Find pure Nash equilibria",
            "Exercise 4: Find Pareto optimal profiles",
        ]

