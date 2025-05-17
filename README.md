# ML Model API

This project implements a machine learning model trained on the Iris dataset, served through a Flask API with a web interface. The model predicts iris flower species based on sepal and petal measurements.

## Project Structure

```
.
├── app.py              # Flask application and API endpoints
├── model.pkl           # Trained machine learning model
├── model2.pkl          # Alternative trained model
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates for web interface
├── Dockerfile         # Docker configuration
└── .dockerignore      # Docker ignore file
```

## Local Development

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```

The application will be available at `http://localhost:1234`

## Web Interface

The project includes a web interface that allows you to:
- Input iris measurements through a form
- View prediction results
- See the model's confidence scores

Access the web interface at `http://localhost:1234` in your browser.

## API Endpoints

### Prediction Endpoint
- `POST /predict`
  - Purpose: Make predictions for iris flower species
  - Request body: 
    ```json
    {
        "features": [5.1, 3.5, 1.4, 0.2]  // [sepal_length, sepal_width, petal_length, petal_width]
    }
    ```
  - Response: 
    ```json
    {
        "prediction": 0,  // 0: Setosa, 1: Versicolor, 2: Virginica
        "confidence": 0.95
    }
    ```

### Health Check
- `GET /health`
  - Purpose: Verify API health status
  - Response: 
    ```json
    {
        "status": "healthy"
    }
    ```

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t ml-api .
```

2. Run the container:
```bash
docker run -p 1234:1234 ml-api
```

## AWS ECS Deployment

1. Create an ECR repository
2. Push the Docker image to ECR
3. Create an ECS cluster and service
4. Configure the service to use the ECR image
5. Set up the necessary security groups and load balancer

## Model Information

The project includes two trained models:
- `model.pkl`: Primary model for iris species prediction
- `model2.pkl`: Alternative model for comparison or fallback

Both models are trained on the Iris dataset and can predict between three iris species:
- Setosa (0)
- Versicolor (1)
- Virginica (2) 