const express = require('express');
const routes = require('./routes/rout');
const mongoose = require('mongoose')

const app = express();
const PORT = 5000;

app.use('/api/', routes);

async function start() {
    try {
            await mongoose.connect(config.get('mongoUri'), {
                useNewUrlParser: true,
                useUnifiedTopology: true,
                useCreateIndex: true
            }) 
        app.listen(PORT, (req, res) => console.log(`Server has been run on port ${PORT}`));
    }   catch (e) {
        console.log("SERVER ERROR!!!",e.message);
    }
}

start();