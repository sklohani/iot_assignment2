module.exports = app => {
    const dht11 = require("../controllers/dht11.controller.js");

    var router = require("express").Router();

    // Create new entry
    router.post("/", dht11.create);

    // Retrieve all entry
    router.get("/", dht11.getAll);

    app.use('/api/dht11', router);
}