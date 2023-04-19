// Refer: https://www.bezkoder.com/node-js-rest-api-express-mysql/

// Test API
// curl -i -X POST "http://127.0.0.1:8080/api/dht11" -H "accept: */*" -H "Content-Type: application/json" -d "{\"humidity\": 52, \"temperature\": 29}"

const express = require("express");
const cors = require("cors");

const app = express();

var corsOptions = {
    origin: "http:localhost:8081"
};

app.use(cors(corsOptions));

// Parse requests of content-type - application/json
app.use(express.json());

// Parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({extended: true}));

app.get("/", (req, res) => {
    res.json({message: "Welcome!"})
});

require("./app/routes/dht11.routes.js")(app)

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});