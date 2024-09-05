# Quiz_Project

A simple quiz application written in Python. This project demonstrates how to build a quiz game using object-oriented programming principles.

## Project Structure

- `question_model.py`: Contains the `Question` class that models a quiz question with its text and answer.
- `data.py`: Stores the quiz data in a list of dictionaries, each containing a question and its correct answer.
- `quiz_brain.py`: Contains the `Quiz_brain` class that manages the quiz logic, including asking questions, checking answers, and keeping score.
- `main.py`: The main script that initializes the quiz and starts the game.

## Getting Started

To run the quiz application, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/quiz-app.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
    cd quiz-app
   ```
   
3. **Install Dependencies:**

   Ensure you have Python installed. This project does not have external dependencies, but you should have Python 3.x.

4. **Run the Application:**

   Execute the main script to start the quiz:
     ```bash
      python main.py
     ```
     
## How It Works

1. **Question Model:**
   - The `Question` class represents a quiz question with its text and the correct answer.

2. **Quiz Brain:**
   - The `Quiz_brain` class manages the quiz, including presenting questions, checking answers, and keeping track of the score.

3. **Main Script:**
   - The `main.py` script initializes the `Question` objects from the data, sets up the `Quiz_brain`, and starts the quiz loop.

