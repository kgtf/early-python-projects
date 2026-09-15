# Family Tree Generator

A Python application that lets users enter family members and generates a visual family tree in real time.

The program combines **Tkinter** for the user interface and **Turtle Graphics** for visualization.

## Features

- User-selectable family-tree depth
- Support for:
  - Self
  - Parents
  - Grandparents
  - Great-grandparents
- Dynamic input fields based on the selected generation
- Dictionary-based storage of family relationships
- Procedural drawing of maternal and paternal branches
- Real-time family-tree visualization
- Object-oriented structure using multiple classes

## How It Works
<img width="589" height="316" alt="Screenshot 2026-09-15 at 1 41 30 PM" src="https://github.com/user-attachments/assets/149b852c-54f8-4783-b02d-a933f327b390" />

The program first asks the user how many generations of family information they want to enter.

<img width="591" height="224" alt="Screenshot 2026-09-15 at 1 41 51 PM" src="https://github.com/user-attachments/assets/04919a23-cebf-4336-9717-e9f3c1bd7cd6" />

Based on that selection, the interface dynamically creates the required input fields.
<img width="605" height="698" alt="Screenshot 2026-09-15 at 1 42 10 PM" src="https://github.com/user-attachments/assets/fa7fd352-5f55-4585-bb0f-73654ca402c2" />

The entered names are stored in a dictionary using numeric keys that represent positions in the family tree.

The `FamilyTree` class then uses Turtle Graphics to draw the tree and place each family member in the appropriate position.


https://github.com/user-attachments/assets/8a5004d8-8f9e-44e9-b79b-c2da8f02b111


## Technologies

- Python
- Tkinter
- Turtle Graphics

## What I Learned

This project helped me practice:

- Object-oriented programming
- GUI development
- Dictionaries and data structures
- Procedural graphics
- Event handling
- Dynamic user input

This was one of my more complex early Python projects.
