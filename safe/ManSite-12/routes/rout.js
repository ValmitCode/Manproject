const express = require('express');
const

const router = express.Router();

// localhost:5000/api/test/
router.get('/test', (req, res) => {
    res.send('Hello, World!');
});




module.exports = router;