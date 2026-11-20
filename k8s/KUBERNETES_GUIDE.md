# Kubernetes guide (Killercoda)

Deploy `minalchithna/flask-app:v1` from the Killercoda Kubernetes Playground. No local Kubernetes install is required.

Commit and push the `k8s` folder before cloning, so the playground receives the manifests.

## 1. Open the playground

Open https://killercoda.com/playgrounds/scenario/kubernetes and start the scenario. Wait until the terminal is ready.

## 2. Clone the repository

```bash
git clone https://github.com/mchithna/devops-practical.git
cd devops-practical
```

## 3. Deploy the manifests

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

## 4. Verify the Deployment and Pods

```bash
kubectl get deployment flask-deployment
kubectl get pods -l app=flask-web
```

`flask-deployment` should show `2/2` ready. Two Pods should show `Running`.

## 5. Check the Service

```bash
kubectl get service flask-service
```

The Service type is `NodePort`. Port `80` targets container port `5000`.

## 6. Test the application

```bash
kubectl port-forward service/flask-service 8080:80
```

Open a second terminal in the playground and run:

```bash
curl http://127.0.0.1:8080
```

The response is `Hello, DevOps World! V1`.

## 7. Capture screenshots

Save these as evidence:

- `kubectl get deployment flask-deployment` and `kubectl get pods -l app=flask-web` showing two running Pods.
- `kubectl get service flask-service`.
- The `curl` response `Hello, DevOps World! V1`.
