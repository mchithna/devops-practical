# Docker guide (GitHub Codespaces)

Build and push the image from GitHub Codespaces. Docker Desktop is not required on Windows.

Commit and push `Dockerfile` and `.dockerignore` before opening a codespace, so those files are in the repository.

## 1. Open the repository in Codespaces

1. Open https://github.com/mchithna/devops-practical
2. Click **Code**, then **Codespaces**, then **Create codespace** on the branch that contains `Dockerfile`.

## 2. Verify Docker

```bash
docker --version
docker info
```

Both commands should succeed inside the codespace.

## 3. Build the image

```bash
docker build -t flask-app:v1 .
```

## 4. Run the container

```bash
docker run -d --name flask-app -p 5000:5000 flask-app:v1
```

## 5. Test the application

```bash
curl http://127.0.0.1:5000
```

The response is `Hello, DevOps World! V1`.

## 6. Stop the container

```bash
docker stop flask-app
```

## 7. Log in to Docker Hub

Create an access token at https://hub.docker.com/settings/security, then:

```bash
docker login -u YOUR_DOCKERHUB_USERNAME
```

When prompted for a password, paste the access token.

## 8. Tag the image

```bash
docker tag flask-app:v1 YOUR_DOCKERHUB_USERNAME/flask-app:v1
```

## 9. Push the image

```bash
docker push YOUR_DOCKERHUB_USERNAME/flask-app:v1
```

## 10. Verify the image is public

Open:

```text
https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/flask-app/tags
```

Confirm that tag `v1` is listed and the repository visibility is **Public**.
