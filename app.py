def add(a, b):
return a + b

def greet(name):
return f"Hello, {name}!"
test_app.py:

from app import add, greet

def test_add():
assert add(2, 3) == 5

def test_greet():
assert greet("World") == "Hello, World!"
Dockerfile:

FROM python:3.11-alpine
WORKDIR /app
COPY app.py .
CMD ["python", "-c", "from app import greet; print(greet('DevOps'))"]
buildspec.yml:

version: 0.2
phases:
install:
commands:
- pip install flake8 pytest
pre_build:
commands:
- echo "Running lint..."
- flake8 app.py
- echo "Running unit tests..."
- pytest test_app.py -v
- aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin $ECR_URI
build:
commands:
- IMAGE_TAG=$CODEBUILD_RESOLVED_SOURCE_VERSION
- docker build -t $ECR_URI:$IMAGE_TAG .
- docker push $ECR_URI:$IMAGE_TAG
- docker tag $ECR_URI:$IMAGE_TAG $ECR_URI:latest
- docker push $ECR_URI:latest
post_build:
commands:
- echo "Build complete. Image tag $IMAGE_TAG pushed to ECR.