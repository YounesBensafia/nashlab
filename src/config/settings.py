from utils.exo1.randomMatrix import random_matrix as matrix
from prompt_toolkit.styles import Style
N = 3
GAME = matrix(N, N)

choice_style = Style([
        ("qmark", "fg:ansiyellow bold"),       # token in front of the question
        ("question", "bold"),                  # question text
        ("answer", "fg:ansiyellow bold"),      # submitted answer text behind the question
        ("pointer", "fg:ansiyellow bold"),     # pointer used for the current selection
        ("selected", "fg:ansiyellow"),         # style for a selected item of a checkbox
        ("highlighted", "fg:ansiyellow bold")  # style for highlighted text
    ])

choice_question =   [
            "Exercise 1: Remove strictly dominated strategies",
            "Exercise 2: Find dominant strategies",
        ]

