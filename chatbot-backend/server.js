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

    const cmd = `venv/bin/python chatbot.py "${question}"`;

    exec(cmd, (error, stdout, stderr) => {
        if (error) {
            console.error(`Exec error: ${error}`);
            console.error(`stderr: ${stderr}`);
            console.error(`stdout: ${stdout}`);
            return res.status(500).json({ 
                error: "Python script failed.",
                details: stderr || stdout 
            });
        }

        try {
            const result = JSON.parse(stdout);
            res.json(result);
        } catch (err) {
            res.status(500).json({ error: "Invalid response from Python.", details: stdout });
        }
    });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

