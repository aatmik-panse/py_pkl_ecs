# ML Model API

This project contains a machine learning model trained on the Iris dataset, served through a Flask API.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Train the model:
```bash
python train_model.py
```

3. Run the Flask application:
```bash
python app.py
```

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t ml-api .
```

2. Run the container:
```bash
docker run -p 5000:5000 ml-api
```

## API Endpoints

- `POST /predict`: Make predictions
  - Request body: `{"features": [5.1, 3.5, 1.4, 0.2]}`
  - Response: `{"prediction": 0}`

- `GET /health`: Health check endpoint
  - Response: `{"status": "healthy"}`

## AWS ECS Deployment

1. Create an ECR repository
2. Push the Docker image to ECR
3. Create an ECS cluster and service
4. Configure the service to use the ECR image
5. Set up the necessary security groups and load balancer 