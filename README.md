# 🐳 Dockerized Flask Web App with Docker Compose

This project containerizes a simple Flask application using a production-ready WSGI server (**Gunicorn**) and orchestrates the build and run process using **Docker Compose**.

## 💻 Build and Run

1.  **Build and Start Containers (First Time)**
    This command reads `docker-compose.yml`, builds the image using the `Dockerfile`, and starts the container in the background (`-d`).

    ```bash
    docker compose up --build -d
    ```

2.  **Verify Container Status**
    Check that the container is running and its status (it should show `healthy` after a moment).

    ```bash
    docker compose ps
    ```

3.  **Access the Application**
    The app is running on the host port defined in your `.env` file (e.g., **http://localhost:8000**).

    * **Main Route:**
        ```bash
        curl http://localhost:8000/
        ```
        *Expected Output:* `Hello from Flask in Docker!`

---

## ✅ Bonus: Testing the Healthcheck

You added a `/health` route, and Docker Compose is automatically checking it. You can manually verify the endpoint:

```bash
curl http://localhost:8000/health