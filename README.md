# Python Word Counter 

A simple yet robust command-line Python script that counts the number of words in a text file. This project demonstrates basic file I/O, string manipulation, and exception handling in Python.

## About The Project

This script provides a straightforward way to analyze text files from your terminal. It's designed to be user-friendly, prompting for a filename and providing clear feedback, including gracefully handling cases where a file cannot be found.

### Features
* Counts the total number of words in any given text file.
* Simple and interactive command-line interface.
* Graceful error handling for non-existent files.
* Written in clean, easy-to-understand Python.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3 installed on your system. You can check your Python version by running:
```sh
python --version
```

### Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone [https://github.com/your-username/python-word-counter.git](https://github.com/your-username/python-word-counter.git)
    ```
2.  Navigate to the project directory:
    ```sh
    cd python-word-counter
    ```

## Usage

1.  Run the script from your terminal:
    ```sh
    python word_counter.py
    ```
2.  The script will prompt you to enter the name of the file you wish to analyze.
    ```
    Enter the name of the text file (e.g., sample.txt):
    ```
3.  Provide the name of a local text file (e.g., `sample.txt`) and press Enter.

### Example

#### Successful Run 
If the file exists, the script will output the word count.
```
Enter the name of the text file (e.g., sample.txt): sample.txt
✅ Success! The file 'sample.txt' contains 16 words.
```

#### File Not Found ❌
If the file does not exist, it will display a user-friendly error message.
```
Enter the name of the text file (e.g., sample.txt): nonexistent.txt
❌ Error: The file 'nonexistent.txt' was not found. Please check the file name and path.
```


Distributed under the MIT License. See `LICENSE` file for more information.

---
