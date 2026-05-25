const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

// MongoDB connection
mongoose.connect("mongodb://127.0.0.1:27017/customersDB")
.then(() => console.log("MongoDB connected"))
.catch(err => console.log(err));

// Customer schema
const Customer = mongoose.model("Customer", {
  name: String
});

// Add customer
app.post("/add", async (req, res) => {
  const customer = new Customer({ name: req.body.name });
  await customer.save();
  res.send("Customer Added");
});

// Get customers
app.get("/customers", async (req, res) => {
  const customers = await Customer.find();
  res.json(customers);
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});
