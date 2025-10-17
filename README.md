# 🧠 LLM Deployment App for IITM

This project was built as part of the **Modern Application Development - I (LLM Deployment Project)**.

The application receives a JSON POST request from the IITM evaluation system, verifies a secret, builds a simple LLM-assisted app, pushes it to GitHub Pages, and reports deployment status back to the evaluation API.

---

## ⚙️ Features

- Flask API endpoint `/api-endpoint` that handles JSON POST requests  
- Secret verification for secure evaluation  
- Automatic repo update and evaluation ping  
- Docker + Hugging Face deployment for always-on hosting  
- Compatible with IITM Evaluation API format

---

## 🧩 API Usage

### Endpoint
POST https://atul0987-llm-deployment.hf.space/api-endpoint

bash
Copy code

### Example Request
```json
{
  "email": "22f3002956@ds.study.iitm.ac.in",
  "secret": "mysecret123",
  "task": "test-task",
  "round": 1,
  "nonce": "abcd1234",
  "brief": "Create a simple test app that says hello world.",
  "evaluation_url": "https://httpbin.org/post"
}
Example Response
json
Copy code
{
  "message": "Project 'test-task' deployed successfully",
  "status": "success",
  "project_url": "https://22f3002956.github.io/test-task/"
}
🧱 Deployment Setup
Local Run

bash
Copy code
pip install -r requirements.txt
python app.py
Environment Variables

GITHUB_TOKEN → Your GitHub Personal Access Token

SECRET → mysecret123

Hugging Face Deployment

Add variables under “Settings → Variables and Secrets”

Public Space: https://huggingface.co/spaces/atul0987/llm-deployment

Hardware: CPU Basic

🧠 Tech Stack
Python (Flask)

Hugging Face Spaces (Docker)

GitHub Pages

JSON APIs

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

👤 Author
Atul Raghav
22f3002956@ds.study.iitm.ac.in
IIT Madras — BS in Data Science and Applications