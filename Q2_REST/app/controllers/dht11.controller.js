const DHT11 = require("../models/dht11.model.js");

exports.create = (req, res) => {
    console.log("New Incoming!");

    if (!req.body) {
        res.status(400).send({
            message: "ERR! Content can not be empty."
        });
    }

    const newEntry = new DHT11({
        humidity: req.body.humidity,
        temperature: req.body.temperature,
    })

    DHT11.create(newEntry, (err, data) => {
        if (err) {
            res.status(500).send({
                message: err.message || "ERR! Error occured while making new entry."
            });
        }
        else
            res.send(data);
    });
};

exports.getAll = (req, res) => {
    const _id = req.query._id;

    DHT11.getAll(_id, (err, data) => {
        if (err) {
            res.status(500).send({
                message: err.message || "ERR! Error occured while retriving the entry."
            });
        }
        else
            res.send(data);
    })
};