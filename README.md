# Project Repository

## Production Deployment and Containerization

This project is set up to support production packaging and Docker containerization.

### Installation

1. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and configure custom environment parameters.

### Docker Run

Build the Docker image:
```bash
docker build -t ml-app .
```

Run the container:
```bash
docker run -it ml-app
```
