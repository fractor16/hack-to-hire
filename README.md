# Flight Status and Notifications

## Overview
This project provides real-time flight status updates and notifications to passengers. The system displays the current flight status, such as delays, cancellations, and gate changes, and sends push notifications for any changes. The project uses a React frontend and a Flask backend, with the capability to integrate with messaging systems like Kafka or RabbitMQ for notifications.

## Technologies Used
- **Frontend:** React.js
- **Backend:** Python (Flask)
- **Database:** Mock data (JSON file)
- **Notifications:** Kafka or RabbitMQ (optional)

## Project Structure
flight-status
│
├── backend
│ ├── app.py
│ ├── mock_data.json
│ ├── requirements.txt
│
├── frontend
│ ├── public
│ ├── src
│ │ ├── FlightStatus.js
│ │ ├── App.js
│ │ ├── index.js
│ ├── package.json
│
├── .gitignore
└── README.md


## Features
- Real-time flight status updates
- Push notifications for status changes
- Integration with airport systems using mock data

## Setup Instructions

### Prerequisites
- Node.js and npm installed
- Python and pip installed
- Virtual environment tool (optional but recommended)

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
flask run
cd frontend
npm install
npm start

### Adding README.md to GitHub Repository

1. **Navigate to Your Repository Directory**: Ensure you are in the directory where your cloned repository is located.

2. **Copy Project Files**: Copy your project files (including the newly created `README.md`) into the repository directory.

3. **Add, Commit, and Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit with project files"
   git push origin main
