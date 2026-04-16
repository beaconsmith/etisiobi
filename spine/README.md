# Research Spine

Connects Oroma (product) to etisiobi (research archive).

## What it does

Queries Oroma's database, computes OGI indicator values, writes structured facts files to `research/icegov/facts/`, and logs contradictions where indicators are uncomputable.

## Setup

```bash
pip install psycopg2-binary python-dotenv
cp spine/.env.example spine/.env
# Edit .env with your Oroma DB connection string
```

Create a read-only DB user in Oroma's Postgres:
```sql
CREATE USER research_reader WITH PASSWORD 'your_password';
GRANT CONNECT ON DATABASE oroma TO research_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO research_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO research_reader;
```

## Run

```bash
# From etisiobi root
python spine/extractor.py

# For a specific workspace
python spine/extractor.py --workspace ws_abc123

# With custom measurement window
python spine/extractor.py --days 30
```

## Outputs

- `research/icegov/facts/YYYY-MM-DD.json` — machine-readable indicator values
- `research/icegov/facts/YYYY-MM-DD.md` — human-readable summary
- Appended entry in `log.md`

## Offline mode

If no DB connection is configured, the extractor writes a "no_db_connection" facts file. This documents the absence of evidence — which is itself research-relevant.

## Automating with GitHub Actions

See `.github/workflows/daily_extraction.yml` (to be created).
Requires `OROMA_DB_URL` set as a GitHub Actions secret.
