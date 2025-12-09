cd /home/user/serverless-free-tier-api && cat README.md
session: default
# 📝 Serverless Free-Tier Task API

Serverless Free-Tier Task API is a cloud-native, serverless project built with AWS Lambda, API Gateway, and DynamoDB. It provides a fully functional CRUD API for managing tasks while staying completely within AWS Free Tier. This project demonstrates modern serverless architecture, infrastructure-as-code (SAM), and practical DevOps deployment skills, making it a strong portfolio piece for cloud and DevOps roles.

![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Production-green)

A **serverless task management API** built using **AWS Lambda**, **API Gateway**, and **DynamoDB**, fully compatible with **AWS Free Tier**.  
This project demonstrates a **cloud-native, serverless architecture**, ideal for learning and showcasing in your portfolio.

---

## 💻 Technologies Used

- **AWS SAM** – Serverless Infrastructure as Code
- **AWS Lambda** – Serverless compute for Python functions
- **Amazon API Gateway** – HTTP API management
- **Amazon DynamoDB** – NoSQL database (on-demand billing)
- **Python 3.12** – Lambda runtime
- **PowerShell / AWS CLI** – Deployment & testing

---

## 🌟 Features

- Full **CRUD** operations for tasks via HTTP API
- Free-tier compatible serverless setup:
  - Lambda: 128 MB, 5-second timeout
  - DynamoDB: PAY_PER_REQUEST
  - API Gateway: Free Tier
- Easy deployment using **AWS SAM CLI**
- Can be extended with authentication, multiple tables, or front-end integration

---

## 📂 Project Structure

```
serverless-free-tier-api/
├─ src/                # Lambda function source code
│  └─ app.py           # Lambda handler
├─ template.yaml       # AWS SAM template
├─ samconfig.toml      # SAM CLI config
└─ README.md           # Project documentation
```


---

## 🚀 Deployment Instructions

1. **Install prerequisites**:

   - [AWS CLI](https://aws.amazon.com/cli/)
   - [AWS SAM CLI](https://aws.amazon.com/serverless/sam/)
   - [Docker](https://www.docker.com/get-started) (for container builds)
   - Python 3.x

2. **Build the project**:

   ```bash
   sam build --use-container
   sam deploy --guided
   ```

   Follow prompts to set stack name, region, and IAM permissions.

3. **After deployment**, SAM provides your API Gateway URL.

---

## 📡 API Usage

Replace `<API_URL>` with your deployed endpoint.

### Create a task:

```powershell
$body = @{ id="1"; description="Finish project"; completed=$false } | ConvertTo-Json
Invoke-RestMethod -Uri "<API_URL>/tasks" -Method Post -Body $body -ContentType "application/json"
```

### Get all tasks:

```powershell
Invoke-RestMethod -Uri "<API_URL>/tasks" -Method Get
```

### Update a task:

```powershell
$body = @{ completed=$true } | ConvertTo-Json
Invoke-RestMethod -Uri "<API_URL>/tasks/1" -Method Put -Body $body -ContentType "application/json"
```

### Delete a task:

```powershell
Invoke-RestMethod -Uri "<API_URL>/tasks/1" -Method Delete
```

---

## 💡 Notes

- Designed to stay within AWS Free Tier limits
- Great for a portfolio project to demonstrate serverless architecture
- Extendable for more advanced use cases

---

## 📖 References

- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [Amazon API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)

---

## ⚡ Author

**Franklin Chionoso** – DevOps & Cloud Enthusiast

