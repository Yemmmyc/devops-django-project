# DevOps Pipeline for a Django App with CI/CD to Kubernetes on AWS

## 📌 Project Overview

This project demonstrates a full DevOps pipeline for deploying a Django web app using:

* **Vagrant** (local provisioning)
* **Docker** (containerization)
* **GitHub** (source control)
* **DockerHub** (image registry)
* **Jenkins** (CI/CD automation)
* **Kubernetes** (orchestration on AWS EC2)

---

## 🛠️ Tech Stack

* Python 3.9
* Django 3.2
* Docker
* Jenkins
* Kubernetes (Minikube/Kind/K3s)
* AWS EC2 (Ubuntu 18.04)
* Bash, YAML, JSON

---

## 🗓️ Project Timeline & Tasks

### ✅ Day 1: Setup & Local Deployment

#### Task 1: Vagrant Setup

* **Vagrantfile** to spin up an Ubuntu 18.04 VM
* `provision.sh` installs Python, pip, Git, Docker, Docker Compose

#### Task 2: Create Django App

* Created a new Django project `app`
* Created `hello` app with a single endpoint: `/hello` → `Hello DevOps!`
* Added `requirements.txt`
* Allowed all hosts in Django settings

#### Task 3: Dockerize the App

* Created `Dockerfile` to install dependencies and run the app
* Created `docker-compose.yml` to map port 8000 (Django) to 8010 (host)

#### Task 4: GitHub Integration

* Initialized Git repo
* Added `.gitignore`
* Committed all files
* Pushed to GitHub: [https://github.com/Yemmmyc/devops-django-project](https://github.com/Yemmmyc/devops-django-project)

#### Task 5: DockerHub Integration

* Docker image built and tagged
* Pushed to DockerHub: `docker.io/yemisi76/devops-django`

---

### ✅ Day 2: CI/CD with Jenkins + AWS EC2

#### Task 6: Provision EC2

* Launched Ubuntu 18.04 EC2 instance
* Installed Docker, Jenkins, and `kubectl`
* Allowed ports 22, 80, 8080 in EC2 security group

#### Task 7: Jenkins Setup

* Installed Jenkins plugins (Docker, GitHub, Kubernetes CLI)
* Created a multibranch pipeline
* Added `Jenkinsfile` to GitHub
* Configured Jenkins to pull repo, build Docker image, push to DockerHub

#### Task 8: App Configs

* `config.json` for app settings (mock/demo config)
* `k8s/deployment.yaml` and `k8s/service.yaml` created for Kubernetes deployment

---

### ✅ Day 3: Kubernetes Deployment & Monitoring

#### Task 9: Set Up Kubernetes

* Installed and started K8s cluster with Kind
* Verified with `kubectl get nodes`

#### Task 10: Deploy Django to Kubernetes

* Applied `deployment.yaml` and `service.yaml`
* Exposed service on NodePort
* Accessed app at `http://<ec2-ip>:<nodeport>/hello`

#### Task 11: CI/CD Verification

* Made a change to `/hello` endpoint
* Pushed to GitHub
* Jenkins auto-built, pushed new Docker image, and triggered K8s redeploy

#### Task 12: Monitoring & Cleanup

* Verified logs with `kubectl logs <pod>`
* Cleaned up with:

```bash
kubectl delete deployment <name>
kubectl delete service <name>
docker rmi <image-id>
```

---

## 📁 Project Structure

```
devops-django-project/
├── myproject/
│   ├── app/               # Django project files
│   ├── hello/             # App with /hello view
│   ├── manage.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── config.json
├── provision.sh
├── Vagrantfile
├── .vagrant/
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

---

## ✅ Deliverables

* GitHub: [https://github.com/Yemmmyc/devops-django-project](https://github.com/Yemmmyc/devops-django-project)
* DockerHub: [https://hub.docker.com/r/yemisi76/devops-django](https://hub.docker.com/r/yemisi76/devops-django)
* EC2 Public IP: `http://<your-ec2-ip>:<nodeport>/hello`

---

## 🧠 Lessons Learned

* Bridging local and cloud development using Vagrant and AWS
* Automating container builds and deployments with Jenkins
* Kubernetes orchestration and troubleshooting with YAML
* Importance of config management and log tracing

---

## 🙌 Author

**Yemisi** — DevOps Enthusiast & Cloud Infrastructure Learner

