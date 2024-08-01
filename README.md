# Food-Tracker-Flask
Food Tracker is a web application developed to help users track their daily food intake and monitor nutritional information such as protein, carbohydrates, and fat. This application was built using Flask, a lightweight and versatile Python web framework, which facilitates rapid development and easy integration with SQLite, a self-contained, serverless, zero-configuration SQL database engine.

## Features
- **User-friendly Interface**: Designed with HTML and CSS for a clean and intuitive interface, making it easy to input and review food data.
- **Daily Food Entries:** Users can log food items along with the date, food name, and nutritional details including protein, carbohydrates, and fat.
- **Calorie Calculation:** Automatically calculates the total calorie count for each day based on the nutritional information provided.
- **Review and Analysis:** Users can review their food entries by date, allowing them to track their dietary habits over time.

## Technologies Used
-**Flask:** Provides the web framework for developing the application.
-**SQLite3:** Manages data storage and retrieval in a lightweight, serverless SQL database.
-**HTML:** Structures the content of the web pages.
-**CSS:** Styles the web pages to ensure a visually appealing and user-friendly experience.
-**Python:** The core programming language used for backend development and data processing.

## Installation
1. **Clone the Repository:**
  '''bash
  git clone https://github.com/yourusername/food-tracker.git
  cd food-tracker
  '''

**Set Up Virtual Environment:**

  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install Dependencies:**

  pip install -r requirements.txt

**Initialize the Database:**

  flask init-db

**Run the Application:**

  flask run

## Usage
**Log Food Entries:** Navigate to the food entry page and input details such as the date, food name, protein, carbohydrates, and fat.
**View Daily Totals:** Go to the daily summary page to see the total calories and nutritional breakdown for each day.
**Review Historical Data:** Use the review feature to look back at past entries and analyze dietary patterns.

## Contributing
We welcome contributions from the community. To contribute:

Fork the repository.
Create a new branch.

  git checkout -b feature-branch

Make your changes and commit them with a clear message.

  git commit -m "Description of your changes"

Push to the branch.

  git push origin feature-branch

Create a pull request on GitHub.
