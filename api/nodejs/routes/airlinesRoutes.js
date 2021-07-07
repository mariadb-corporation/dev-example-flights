"use strict";

let express = require("express"),
    router = express.Router(),
    db = require('../db');

// GET all airlines
router.get("/", async (req, res, next) => {
    try {
        const results = await db.pool.query("select * from airlines order by airline");
        res.send(results);
    } catch (err) {
        throw err;
    }
});

module.exports = router;