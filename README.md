## Setup

1. Clone repo
2. Install requirements: `pip install -r requirements.txt`
3. Run seed: `python seed_data.py`
4. Start API: `uvicorn main:app --reload`

## Endpoints
- `GET /classes`
- `POST /book`
- `GET /bookings?email=...`
