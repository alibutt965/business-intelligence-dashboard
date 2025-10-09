const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// --- MongoDB Connection ---
const uri = "mongodb://root:toor@localhost:27017/?authSource=admin";


mongoose
  .connect(uri)
  .then(() => console.log("✅ Connected to MongoDB (Docker)"))
  .catch((err) => console.error("❌ MongoDB connection error:", err));

// --- Sample schema & route ---
const userSchema = new mongoose.Schema({ name: String, age: Number });
const User = mongoose.model("User", userSchema);

app.get("/api/users", async (req, res) => {
  const users = await User.find();
  res.json(users);
});

app.post("/api/users", async (req, res) => {
  const newUser = await User.create(req.body);
  res.json(newUser);
});

const PORT = 3000;
app.listen(PORT, () => console.log(`🚀 Server running at http://localhost:${PORT}`));
