# organization
API Development Project using Flask with MongoDB
## Overview
This project provides a **RESTful API** built with **Flask** and **MongoDB** that provides API endpoints for user authentication and organization management. It supports user signup, signin,token refresh, and organization CRUD operations .


### Features

- **Signup**
- **Signin**
- **Organization Management**

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **MongoDB**: A NoSQL database for storing user and organization data.
- **JWT (JSON Web Tokens)**: For secure token-based authentication.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB
- Flask

### Installation
### Step1 : Clone the repository:
1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```
### Step 2: Install Required Packages

To install the necessary packages, run the following command:
```bash
pip install -r requirements.txt
```
### Step 3: Set Up MongoDB
 **Create a MongoDB Database**:
   - If you haven't already, create a new MongoDB database using your preferred method (e.g., MongoDB Atlas, local installation).
   - Locate the configuration file (e.g., `config.py`).

### Step 4: Run the Application
    - Use the following command to start the Flask development server:
```bash
flask run
```
    - For docker use the following command:
```bash
docker compose up --build
```
## API Endpoints

### 1. Signup Endpoint

- **Method**: `POST`
- **URL**: `/signup`
- **Description**: Creates a new user .
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string",
    "password": "string"
  }
    ```
### 2. Signin Endpoint

- **Method**: `POST`
- **URL**: `/signin`
- **Description**: Authenticates a user and provides access and refresh tokens.
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
    ```
### 3. Refresh Token Endpoint

- **Method**: `POST`
- **URL**: `/refresh-token`
- **Description**: Refreshes the access token using a valid refresh token.
- **Request Body**:
  ```json
  {
    "refresh_token": "string"
  }

### 4. Create Organization Endpoint

- **Method**: `POST`
- **URL**: `/organization`
- **Authorization**: Bearer [Token]
- **Description**: Creates a new organization.
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }
    ```
### 5. Read Organization Endpoint

- **Method**: `GET`
- **URL**: `/organization/{organization_id}`
- **Authorization**: Bearer [Token]
- **Description**: Retrieves details of a specific organization by its ID.

### 6. Read All Organizations Endpoint

- **Method**: `GET`
- **URL**: `/organization`
- **Authorization**: Bearer [Token]
- **Description**: Retrieves a list of all organizations associated with the members.

### 7. Update Organization Endpoint

- **Method**: `PUT`
- **URL**: `/organization/{organization_id}`
- **Authorization**: Bearer [Token]
- **Description**: Updates the details of a specific organization.
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }

### 8. Delete Organization Endpoint

- **Method**: `DELETE`
- **URL**: `/organization/{organization_id}`
- **Authorization**: Bearer [Token]
- **Description**: Deletes a specific organization.

### 9. Invite User to Organization Endpoint

- **Method**: `POST`
- **URL**: `/organization/{organization_id}/invite`
- **Authorization**: Bearer [Token]
- **Description**: Invites a user to join a specific organization.
- **Request Body**:
  ```json
  {
    "user_email": "string"
  }

## Test API Endpoints

- Deployed version: https://flask-api-app.vercel.app/[endpoint]
- For docker: Once the containers are up, the API should be accessed on http://localhost:8080/[endpoint]
- Local flask run: http://127.0.0.1:5000/[endpoint]
