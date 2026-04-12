# AI Business Platform

## Day 2 Progress
- Setup PostgreSQL database
- Created database models (User, Product, Order)
- Connected FastAPI with database
- Built API to create and fetch users

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

## How to Run
1. Activate virtual environment
2. Install requirements:
   pip install -r requirements.txt
3. Run server:
   uvicorn backend.main:app --reload

## Day 3 Progress
- Refactored backend into modular structure (routers + services)
- Implemented pagination (skip, limit)
- Implemented filtering (search users by name)
- Improved API structure for scalability

## API Features
- Create User
- Get Users (with pagination)
- Search Users by name