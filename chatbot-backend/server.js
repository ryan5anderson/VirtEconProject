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
        console.log("Received question:", question);

        const response = await axios.post('https://ps76inspk1.execute-api.us-east-1.amazonaws.com/default/llamaRequest', {
            inputs: question,
            parameters: {
                max_new_tokens: 150,
                top_p: 0.9,
                temperature: 0.6
            }
        }, {
            headers: {
                'Content-Type': 'application/json',
                'customattributes': 'accept_eula=true'
            }
        });

        console.log("API Response:", response.data);
        res.json(response.data);
    } catch (error) {
        console.error("Error from API:", error.response ? error.response.data : error.message);
        res.status(500).json({ error: error.response ? error.response.data : error.message });
    }
});


app.listen(5001, () => console.log('Server running on port 5001'));
