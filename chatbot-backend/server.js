const express = require('express');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

app.post('/ask', async (req, res) => {
    try {
        const { question } = req.body;
        if (!question) {
            return res.status(400).json({ error: "No question provided." });
        }

        console.log("Received question:", question);

        const response = await axios.post('https://api.together.xyz/v1/chat/completions', 
        {
            model: "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages: [{ role: "user", content: question }],
            max_tokens: 150,
            top_p: 0.9,
            temperature: 0.6
        }, 
        {
            headers: {
                'Authorization': `Bearer 7c250b03ffca377edb3b61d3d11bea4c1f2ab4c7f156851e8b6ff5844916f719`,
                'Content-Type': 'application/json'
            }
        });

        res.json({ generated_text: response.data.choices[0].message.content });

    } catch (error) {
        console.error("API Error:", error.response ? error.response.data : error.message);
        res.status(500).json({ error: "Failed to get response from Together API." });
    }
});

app.listen(5001, () => console.log('Server running on port 5001'));
