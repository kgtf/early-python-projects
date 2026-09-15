# Image-to-Text Converter

A Python program that converts an image into a text-based representation.

The program reads the image at the pixel level and converts black-and-white pixel values into characters written to a text file.

## Features

- Select an image using a file picker
- Convert the image to black and white
- Optionally downscale the image
- Read pixel-level image data
- Convert pixels into text characters
- Save the result as a `.txt` file

## How It Works

The application uses Tkinter to let the user select an image.

The image is opened with Pillow and converted into a black-and-white image.

The user can optionally reduce the image size before processing.

The program then reads the image pixel by pixel and writes a corresponding text character for each pixel into `imagetext.txt`.

Each row of image pixels becomes a line of text.

Example:
Input image - <img width="800" height="525" alt="gratisography-moon-robot-800x525" src="https://github.com/user-attachments/assets/3e6dbf9d-8e0d-4e8e-8c25-f8fb53341705" />
Output - 

https://github.com/user-attachments/assets/9f7788be-0a67-4209-b6a6-35f57ba3163e




## Technologies

- Python
- Pillow
- Tkinter
- File I/O

## What I Learned

This project introduced me to:

- Basic image processing
- Pixel data
- File handling
- GUI file selection
- Converting visual data into a text representation
