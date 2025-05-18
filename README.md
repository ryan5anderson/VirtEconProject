VirtEcon Project - Local Dev Setup (Mac)
Prerequisites
Homebrew (https://brew.sh/)

Python 3.x (Install via Homebrew if missing)

Node.js and npm (Install via Homebrew if missing)

What This Project Includes
chatbot-backend:
Node.js server that connects to AWS OpenSearch and Together AI.

chatbot-frontend:
React frontend that sends questions to the backend.

Setup Instructions
1. Clone & Navigate
bash
Copy
Edit
cd /path/to/VirtEconProject
Starting the Backend (Python + Node)
1. Go to Backend Directory
bash
Copy
Edit
cd chatbot-backend
2. Create and Activate Python Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set AWS Environment Variables
bash
Copy
Edit
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"
export AWS_DEFAULT_REGION="us-east-1"
Replace YOUR_ACCESS_KEY_ID and YOUR_SECRET_ACCESS_KEY with valid AWS credentials.

5. Install Node Dependencies
bash
Copy
Edit
npm install
6. Start Node Server
bash
Copy
Edit
node server.js
The backend will be available at http://localhost:8080.

Starting the Frontend (React App)
1. Open New Terminal Tab or Window
bash
Copy
Edit
cd /path/to/VirtEconProject/chatbot-frontend
2. Install Frontend Dependencies
bash
Copy
Edit
npm install
3. Start Frontend
bash
Copy
Edit
npm start
The frontend will be available at http://localhost:3000.

Testing Your Setup
Open http://localhost:3000 in your browser.

Submit a question to the chatbot.

You should see a response coming from the backend.