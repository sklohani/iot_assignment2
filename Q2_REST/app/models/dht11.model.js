const sql = require("./db.js");

// Constructor
const DHT11 = function(dht11) {
    this.humidity = dht11.humidity;
    this.temperature = dht11.temperature;
};

DHT11.create = (newEntry, result) => {
    sql.query("INSERT INTO dht11 SET ?", newEntry, (err, res) => {
        if (err) {
            console.log("ERR: ", err);
            result(err, null);
            return;
        }

        console.log("Created Entry: ", {id: res.insertID, ...newEntry});
        result(null, {id: res.insertID, ...newEntry});
    });
};

DHT11.getAll = (_id, result) => {
    let query = "SELECT * FROM dht11";

    if (_id) {
        query += `WHERE id LIKE '%${_id}'`;
    }

    sql.query(query, (err, res) => {
        if (err) {
            console.log("ERR: ", err);
            result(err, null);
            return;
        }

        console.log("Entry: ", res);
        result(null, res);
    });
};

module.exports = DHT11;