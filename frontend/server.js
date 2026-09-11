const express = require("express");
const path = require("path");
const app = express();

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.use(express.static(path.join(__dirname, "public")));

const PORT = 3000;
app.listen(PORT, () => console.log(`Argus frontend stub listening on ${PORT}`));
