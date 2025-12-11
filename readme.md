# Project Setup Guide

A Django-based application for loading and managing CSV data.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

### 1. Install Dependencies

Install all required packages using the requirements file:

```bash
pip install -r requirements.txt
```

### 2. Database Setup

Run migrations to set up your database schema:

```bash
python manage.py migrate
```

### 3. Load Initial Data

Use the custom management command to load CSV data into the database:

```bash
python manage.py csvloader --file_path <file-path>
```

### 4. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Possible Enhancements

This is a basic setup to get the project running. Potential improvements include:

- **Flexible CSV Loading**: Add command-line arguments to `csvloader` for specifying custom file paths
- **API Endpoints**: Implement Django REST Framework (DRF) for RESTful API functionality


