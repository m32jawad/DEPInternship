## Application Management API

This project provides an API for managing applications, including adding, retrieving, and listing application records. It is built using Django and provides JSON responses for API interactions.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git https://github.com/m32jawad/DEPInternship.git
   cd 'DEPInternship/Task1 Registration API'
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Add Record

- **URL:** `/add_record/`
- **Method:** `POST`
- **Data:**
  ```json
  {
    "apply_for": "role",
    "fullname": "John Doe",
    "email": "john.doe@example.com",
    "whatsapp": "1234567890",
    "gender": "male",
    "institute": "ABC University",
    "field_of_study": "Computer Science",
    "years_education": "4",
    "region": "North America",
    "facebook": "facebook.com/johndoe",
    "instagram": "instagram.com/johndoe",
    "linkedin": "linkedin.com/in/johndoe",
    "experience": "2 years in software development",
    "skills": ["Python", "Django", "JavaScript"]
  }
  ```
- **Response:**
  - Success: `200 Created`
    ```json
    {
      "Message": "Data Added Successfully",
      "RecordID": 1
    }
    ```
  - Error: `500 Internal Server Error`
    ```json
    {
      "Message": "error while adding record"
    }
    ```

### Get Record

- **URL:** `/get_record/<str:id>`
- **Method:** `GET`
- **Response:**
  - Success: `200 OK`
    ```json
    {
      "role": "role",
      "fullname": "John Doe",
      "email": "john.doe@example.com",
      "whatsapp": "1234567890",
      "gender": "male",
      "institute": "ABC University",
      "field_of_study": "Computer Science",
      "years_education": 4,
      "region": "North America",
      "facebook": "facebook.com/johndoe",
      "instagram": "instagram.com/johndoe",
      "linkedin": "linkedin.com/in/johndoe",
      "experience": "2 years in software development",
      "skills": ["Python", "Django", "JavaScript"]
    }
    ```
  - Error: `404 Not Found`
    ```json
    {
      "Message": "No record exists with id=<id>"
    }
    ```

### Get All Records

- **URL:** `/get_all_records/`
- **Method:** `GET`
- **Response:**
  - Success: `200 OK`
    ```json
    {
      "Records": [
        {
          "role": "role",
          "fullname": "John Doe",
          "email": "john.doe@example.com",
          "whatsapp": "1234567890",
          "gender": "male",
          "institute": "ABC University",
          "field_of_study": "Computer Science",
          "years_education": 4,
          "region": "North America",
          "facebook": "facebook.com/johndoe",
          "instagram": "instagram.com/johndoe",
          "linkedin": "linkedin.com/in/johndoe",
          "experience": "2 years in software development",
          "skills": ["Python", "Django", "JavaScript"]
        }
        // more records
      ]
    }
    ```
  - Error: `404 Not Found`
    ```json
    {
      "Message": "No record exists"
    }
    ```
