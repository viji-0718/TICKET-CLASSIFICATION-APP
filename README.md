# Ticket Classification App

## Overview
The Ticket Classification App is designed to automate the process of categorizing customer tickets using machine learning techniques. The application leverages natural language processing to analyze ticket content and suggest appropriate categories.

## Features
- Automatic ticket categorization
- User-friendly interface
- Support for various ticket formats
- Integration with existing ticketing systems

## Tech Stack
- **Frontend:** React
- **Backend:** Flask
- **Database:** PostgreSQL
- **Machine Learning:** scikit-learn, pandas
- **Hosting:** AWS

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/viji-0718/TICKET-CLASSIFICATION-APP.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TICKET-CLASSIFICATION-APP
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Usage
- Access the application at `http://localhost:5000`
- Upload your ticket data in .csv format.
- View categorized tickets and analytics through the dashboard.

## Dataset Format
The application expects the input dataset to be in .csv format with the following columns:
- `ticket_id`: Unique identifier for the ticket
- `ticket_content`: Content of the ticket 
- `category`: (optional) Assigned category for supervised learning

## API Endpoints
- **GET /api/tickets**: Retrieve all tickets
- **POST /api/tickets**: Submit a new ticket for categorization
- **GET /api/categories**: List all available categories

## Troubleshooting
- Ensure all dependencies are installed.
- Check if the database is running if encountering connection errors.
- Verify the format of the input dataset.

## Contributing Guidelines
We welcome contributions! To contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

Thank you for your interest in contributing to the Ticket Classification App!