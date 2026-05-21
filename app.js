const express = require('express');
const app = express();
const PORT = 4000; //We will use Port 4000 to keep it separate from Project 1

// Serve a simple shopping page with an interactive button
app.get('/', (req,res) => {
    res.send(`
        <html>
        <head><title>DevOps Shop</title></head>
        <body>
            <h1>Welcome to the DevOps Store</h1>
            <p>Items in Cart: <span id="cart-count">0</span><p>
            <button id="add-btn" onclick="document.getElementById('cart-count').innerText = '1'">Add to Cart</button>
            </body>
            </html>
        `);
});

//A dedicated health endpoint (how modern production systems tell Nagios they are working)
app.get('/health', (req, res) => {
    res.json({ status: "UP", database: "CONNECTED" });
});

app.listen(PORT, () => {
    console.log(`E-Commerce Store running on http://localhost:${PORT}`);
});