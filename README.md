# Jesse Piccione Backend - Resume API

This project contains a Django REST API that exposes resume information such as awards, education, skills and more.  It also provides an endpoint to submit contact messages.  The API is intended to power personal portfolio websites or any front‑end that needs access to this resume data.

## Prerequisites

- Python 3.12
- MySQL server (or compatible database)
- The dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository** and install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables.**  Create a `.env` file or set the following variables in your environment:

   - `SECRET_KEY_VAR` – Django secret key
   - `DATABASE_ENGINE` – Database backend (e.g. `django.db.backends.mysql`)
   - `DATABASE_NAME` – Database name
   - `DATABASE_HOST` – Database host
   - `DATABASE_PORT` – Database port
   - `DATABASE_USERNAME` – Database user
   - `DATABASE_PASSWORD` – Database password
   - `OPENAI_API_KEY` – API key used by the assistant feature (optional)

3. **Apply migrations and create a superuser:**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/` by default.

## Authentication

Most read‑only endpoints are public.  Endpoints that list or delete messages require token authentication and the user to be in the `Admin` group.  Authentication tokens are handled by [Djoser](https://djoser.readthedocs.io/):

- Obtain a token by sending a POST request to `/api/auth/token/login/` with `username` and `password`.
- Include the token in subsequent requests using the `Authorization: Token <token>` header.

## Endpoints

All endpoints are prefixed with `/api/` as shown in `ResumeAPI/urls.py`.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/award/` | List awards |
| GET | `/award/<id>/` | Award details |
| GET | `/award/category/` | List award categories |
| GET | `/award/category/<id>/` | Award category details |
| GET | `/education/` | List education entries |
| GET | `/education/<id>/` | Education entry details |
| GET | `/work/experience/` | List work experiences |
| GET | `/work/experience/<id>/` | Work experience details |
| GET | `/skill/` | List skills |
| GET | `/skill/<id>/` | Skill details |
| GET | `/skill/category/` | List skill categories |
| GET | `/skill/category/<id>/` | Skill category details |
| GET | `/project/` | List projects |
| GET | `/project/<id>/` | Project details |
| GET | `/home/` | List home page entries |
| GET | `/home/<id>/` | Home page entry details |
| GET | `/technology/` | List technologies |
| GET | `/technology/<id>/` | Technology details |
| POST | `/message/` | Submit a contact message |
| GET | `/message/` | List messages (requires admin token) |
| GET/DELETE | `/message/<id>/` | Retrieve or delete a message (admin only) |

## Usage example

```bash
# Get all projects
curl http://localhost:8000/api/project/

# Submit a contact message
curl -X POST http://localhost:8000/api/message/ \
     -H "Content-Type: application/json" \
     -d '{"email":"you@example.com","name":"You","subject":"Hello","message":"Hi Jesse"}'
```

For admin endpoints, first obtain an authentication token and include it in the `Authorization` header as described above.

## Deployment

The repository includes a `Dockerfile` and `cloudbuild.yaml` for containerized deployments.  To deploy with Docker:

```bash
docker build -t jesse-backend .
docker run -p 8000:8000 --env-file .env jesse-backend
```

Use the provided `PreDeployment.py` script to generate an `app.yaml` file when deploying to Google App Engine.

## License

This project is released under the MIT License.
