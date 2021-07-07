"use strict";

let express = require("express"),
    router = express.Router(),
    db = require('../db');

// GET all airports
router.get("/", async (req, res, next) => {
    try {
        const results = await db.pool.query("select iata_code, airport from airports group by airport, iata_code order by airport");
        res.send(results);
    } catch (err) {
        throw err;
    }
});

module.exports = router;