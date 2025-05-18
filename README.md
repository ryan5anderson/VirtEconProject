# VirtEcon Project - Local Development Setup (Mac)

## 🚀 Prerequisites

Make sure you have the following installed:

* **Homebrew**: [https://brew.sh/](https://brew.sh/)
* **Python 3.x**:
  *Install with:*

  ```bash
  brew install python
  ```
* **Node.js & npm**:
  *Install with:*

  ```bash
  brew install node
  ```

---

## 📦 Project Structure

* **`chatbot-backend`**: Node.js server that connects to AWS OpenSearch and Together AI.
* **`chatbot-frontend`**: React app for interacting with the chatbot.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
cd /path/to/VirtEconProject
```

---

## 🖥️ Starting the Backend (Python + Node)

### Step 1: Navigate to Backend Directory

```bash
cd chatbot-backend
```

### Step 2: Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set AWS Environment Variables

```bash
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"
export AWS_DEFAULT_REGION="us-east-1"
```

*Replace with valid AWS credentials.*

### Step 5: Install Node.js Dependencies

```bash
npm install
```

### Step 6: Start the Node Server

```bash
node server.js
```

*Backend is now running at:*
[http://localhost:8080](http://localhost:8080)

---

## 🖼️ Starting the Frontend (React)

### Step 1: Open New Terminal Tab or Window

```bash
cd /path/to/VirtEconProject/chatbot-frontend
```

### Step 2: Install Frontend Dependencies

```bash
npm install
```

### Step 3: Start the React App

```bash
npm start
```

*Frontend is now running at:*
[http://localhost:3000](http://localhost:3000)

---

## ✅ Testing Your Setup

1. Open [http://localhost:3000](http://localhost:3000) in your browser.
2. Submit a question to the chatbot.
3. You should see a response coming from the backend.


