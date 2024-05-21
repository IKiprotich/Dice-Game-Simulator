import random

# Parsing and validating user's input
def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Enter a number from 1 - 6.")
        raise SystemExit(1)

# Simulation of dice rolling
def dice_roll(dice_num):
    roll_results = []
    for _ in range(dice_num):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

# Setting up dice faces diagram
Dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

Die_height = len(Dice_art[1])
Die_width = len(Dice_art[1][0])
Die_face_Separator = " "

# Generating dice faces diagram
def generate_dice_face_diagram(dice_values):
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")
    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

# List of dice faces from Dice_art
def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(Dice_art[value])
    return dice_faces

# List containing dice face rows
def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(Die_height):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = Die_face_Separator.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows

# MAIN CODE BLOCK

# Get and validate the user's input
dice_num_input = input("How many dice do you want to roll?: ")
dice_num = parse_input(dice_num_input)
roll_results = dice_roll(dice_num)
dice_face_diagram = generate_dice_face_diagram(roll_results)
print(f"\n{dice_face_diagram}")
