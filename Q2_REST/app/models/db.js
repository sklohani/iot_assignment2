const mysql = require("mysql");
const dbConfig = require("../config/db.config.js");

// Create connection with the database
const connection = mysql.createConnection({
    host: dbConfig.HOST,
    user: dbConfig.USER,
    password: dbConfig.PASSWORD,
    database: dbConfig.DB
});

connection.connect(error => {
    if (error) throw error;
    console.log("Successfully connected to database.");
});

module.exports = connection;