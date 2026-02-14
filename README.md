# Portfolio Management API

A simple REST API for managing investment portfolios and their assets. Built with FastAPI and SQLite.

## Features

- **Portfolios** — Create and manage investment portfolios (name, description)
- **Assets** — Track assets within portfolios (ticker, amount, average price)

## Prerequisites

- Python 3.12 or higher

## Setup

1. **Install dependencies**

   ```bash
   pip install -e .
   ```

   Or with uv:

   ```bash
   uv sync
   ```

2. **Run database migrations**

   ```bash
   alembic upgrade head
   ```

3. **Start the server**

   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, open **http://localhost:8000/scalar** to view the interactive API documentation.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/api/portfolios` | List all portfolios |
| POST | `/api/portfolios` | Create a portfolio |
| GET | `/api/portfolios/{id}` | Get a portfolio by ID |
| DELETE | `/api/portfolios/{id}` | Delete a portfolio |
| GET | `/api/assets` | List all assets |
| POST | `/api/assets` | Create an asset |
| GET | `/api/assets/{id}` | Get an asset by ID |

## Data Models

**Portfolio**
- `name` — Portfolio name
- `description` — Portfolio description

**Asset**
- `ticker` — Stock/investment ticker symbol
- `amount` — Number of shares/units
- `avg_price` — Average purchase price
- `portfolio_id` — ID of the portfolio this asset belongs to

## Project Structure

```
app/
├── main.py          # FastAPI app entry point
├── core/
│   └── settings.py  # App configuration
├── models/          # Database models (SQLModel)
├── routers/         # API route handlers
├── schema/          # Pydantic request/response schemas
└── utils/           # Shared utilities
migrations/          # Alembic database migrations
```
