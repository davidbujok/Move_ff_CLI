# Learning CLI Tools Repository

## Main Goals

The primary objectives of this repository are:

1. **Learning how to create CLI (Command Line Interface) applications.**
    - understand the basics of building applications that run in the terminal.
2. **Exploring Python virtual environments workflow.**
    - Understanding how to manage project dependencies via virtual environments.
3. **Learning the Click library.**
    - Click is a Python package for creating beautiful command-line interfaces in a composable way with as little code as necessary.
4. **Creating a CLI application that takes multiple arguments.**
    - Focus on expanding applications to handle various user inputs dynamically.

## Repository Content

This repository contains several command-line applications replicating standard Unix utilities for learning purposes, as well as main project, the `mvf` application.

### Simple CLI Apps

- Replications of simple tools such as `ls` and `cat`.
- These apps are designed to mimic the basic functionalities of their original counterparts, providing a foundation for understanding CLI app development.

### MVF - Move Files Interactively

The main highlight of this repository is the `mvf` application, a simple tool designed for moving files and directories interactively in the command line. Features of `mvf` include:

- **File name prompting**: When executed, `mvf` asks the user for the file name to move. If multiple files are found, it will list them with indices for the user to select by entering the corresponding number.
- **Directory move support**: By providing the `--type dir` argument, user can indicate a wish to move directories instead of files.
- **Interactive destination selection**: After a file or a directory selection, the program prompts for the destination folder, listing available folders with numbers if there's more than one.
- **Current directory support**: Using a `.` will specify the current directory as the destination for the move operation.

## Getting Started

The compiled binary can be found in the `dist` folder, and running it requires Python 3.6.

For development and experimentation:

1. Clone the repository.
2. Create a virtual environment:

   ```bash
   python -m venv venv-name
   ```

3. Activate the virtual environment:

   - On Windows:

     ```cmd
     venv-name\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv-name/bin/activate
     ```

4. Install necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Contributing

Contributions are welcome! Please feel free to submit pull requests, suggest new features, or report bugs.
