const express = require('express');
const bodyParser = require('body-parser');
const DsaController = require('./controllers/dsaController');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Instantiate controller and register the routes
const dsaController = new DsaController();
dsaController.registerRoutes(app);

// Start server
const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
