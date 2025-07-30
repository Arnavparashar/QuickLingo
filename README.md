# 🌐 QuickLingo - Cloud-Based Language Translator

QuickLingo is a lightweight, serverless language translation web app hosted on AWS. It enables users to quickly translate text between languages using a simple web interface powered by AWS services.

🔗 **Live App**: [http://langtranslate1.s3-website-us-east-1.amazonaws.com/](http://langtranslate1.s3-website-us-east-1.amazonaws.com/)

---

## 🧰 Tech Stack

- **Amazon S3** – Hosts the static frontend (HTML/CSS/JavaScript)
- **AWS Lambda** – Backend logic for processing translation requests
- **Amazon API Gateway** – Exposes the Lambda function as a REST API
- **Amazon Translate** – (Optional) Provides translation service via AWS SDK
- **Postman** – Used for testing and debugging the API endpoints

---

## 🧠 How It Works

1. User enters text and selects source and target languages on the website.
2. The frontend sends a POST request to the API Gateway.
3. API Gateway triggers the Lambda function with the input.
4. Lambda processes the input and returns the translated output.
5. The response is displayed back to the user on the frontend.

---

## 🚀 Project Structure
QuickLingo/
│
├── frontend/ # Static frontend files (hosted on S3)
│ ├── index.html
│ └── script.js
│
├── lambda_function/ # AWS Lambda code
│ └── index.js (or .py)
│
├── postman/ # Postman collection for API testing
│ └── quicklingo.postman_collection.json
│
└── README.md

---

## 📦 Deployment Steps (Using AWS Console)

### 1. Upload Frontend to S3
- Go to **Amazon S3**
- Create a bucket (e.g., `langtranslate1`)
- Upload `index.html` and other static files
- Enable **static website hosting** in bucket properties

### 2. Create the Lambda Function
- Go to **AWS Lambda**
- Create a function (Node.js or Python)
- Add the logic to translate using AWS Translate or any translation logic
- Set permissions to allow Lambda to access Translate service (if used)

### 3. Setup API Gateway
- Go to **Amazon API Gateway**
- Create a new REST API
- Link it to your Lambda function
- Enable CORS for cross-origin requests

### 4. Connect Frontend to API
- In `script.js`, update the API endpoint URL to your deployed API Gateway URL.

---

## 🧪 API Testing with Postman

1. Import the provided `quicklingo.postman_collection.json` file into Postman.
2. Update the endpoint URL to match your deployed API Gateway URL.
3. Send a POST request with the following format:

```json
{
  "text": "Hello world",
  "source_lang": "en",
  "target_lang": "es"
}

