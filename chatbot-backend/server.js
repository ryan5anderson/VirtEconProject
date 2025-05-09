const express = require('express');
const cors = require('cors');
const { exec } = require('child_process');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/ask', (req, res) => {
    const { question } = req.body;
    if (!question) {
        return res.status(400).json({ error: "No question provided." });
    }

    const cmd = `python3 chatbot.py "${question}"`;

    exec(cmd, (error, stdout, stderr) => {
        if (error) {
            console.error(`Exec error: ${error}`);
            return res.status(500).json({ error: "Python script failed." });
        }

        try {
            const result = JSON.parse(stdout);
            res.json(result);
        } catch (err) {
            res.status(500).json({ error: "Invalid response from Python." });
        }
    });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
