# Python Automation Project

This project allows you to automate screen interactions by tracking mouse positions and executing predefined actions at those positions.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Stopping the Automation](#stopping-the-automation)
- [License](#license)
- [Contact](#contact)

## Installation

1. **Install Python**:
   - Download and install Python from the [official website](https://www.python.org/downloads/).
   - Ensure that Python is added to your system PATH.

2. **Create and Activate a Virtual Environment**:
   - Navigate to your project directory:
     ```bash
     cd path/to/your/project
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

3. **Install Required Packages**:
   - Ensure you have a `requirements.txt` file listing all necessary packages.
   - Install the packages:
     ```bash
     pip install -r requirements.txt
     ```

## Setup

1. **Run `track.py` to Get Positions**:
   - This script is used to capture the screen positions you want to interact with.
   - Run the script and move your mouse to the desired locations. Follow the on-screen instructions to capture and print the coordinates.

2. **Update `main.py`**:
   - Replace placeholder coordinates in `main.py` with the positions obtained from `track.py`.

## Usage

1. **Run `main.py`**:
   - Execute the script to start the automation process:
     ```bash
     python main.py
     ```
   - The script will perform actions such as clicking and typing based on the coordinates specified.

## Stopping the Automation

- To stop the running script, interrupt it by pressing `Ctrl + C` in the terminal.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any questions or issues, please contact:

- **Name**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [yourusername](https://github.com/yourusername)
