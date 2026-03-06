# Suivi de Brossage des Dents

A simple Python application to track daily tooth brushing habits using SQLite.

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd "projet 1"
   ```

## Usage

Run the application:

```bash
python brossage_dents.py
```

The application will:
1. Initialize the SQLite database (`brossage_dents.db`) if it doesn't exist
2. Prompt you to enter how many times you brushed your teeth today (0, 1, or 2)
3. Record your response with a timestamp in the database

## Database

The application stores data in `brossage_dents.db` with the following structure:

- `id`: Unique identifier (auto-increment)
- `date_reponse`: ISO 8601 timestamp of the entry
- `brossages`: Number of times brushed (0, 1, or 2)

## Development

To inspect the database manually:

```bash
sqlite3 brossage_dents.db
```

Then use SQL commands like:
```sql
SELECT * FROM suivi_brossage;
```
