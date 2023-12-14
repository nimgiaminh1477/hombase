const express = require("express");
const { Sequelize, DataTypes } = require("sequelize");

const app = express();
const port = 3000;

const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: "./database.sqlite3",
});

const User = require("./models/user")(sequelize, DataTypes);

app.use(express.json());

app.post("/users", async (req, res) => {
  try {
    const newUser = await User.create(req.body);
    res.json(newUser);
  } catch (error) {
    res.status(500).json({ error });
  }
});

app.get("/users", async (req, res) => {
  try {
    const users = await User.findAll();
    res.json(users);
  } catch (error) {
    res.status(500).json({ error });
  }
});

app.get("/users/:id", async (req, res) => {
  const userId = req.params.id;
  try {
    const user = await User.findByPk(userId);
    if (user) {
      res.json(user);
    } else {
      res.status(404).json({ error: "User not found" });
    }
  } catch (error) {
    res.status(500).json({ error });
  }
});

app.put("/users/:id", async (req, res) => {
  const userId = req.params.id;
  try {
    const [updatedRowsCount] = await User.update(req.body, {
      where: { id: userId },
      count: true,
    });
    if (updatedRowsCount > 0) {
      const updatedUser = await User.findByPk(userId);
      res.json(updatedUser);
    } else {
      res.status(404).json({ error: "User not found" });
    }
  } catch (error) {
    res.status(500).json({ error });
  }
});

app.delete("/users/:id", async (req, res) => {
  const userId = req.params.id;
  try {
    const deletedRowCount = await User.destroy({
      where: { id: userId },
    });
    if (deletedRowCount > 0) {
      res.json({ message: "User deleted successfully" });
    } else {
      res.status(404).json({ error: "User not found" });
    }
  } catch (error) {
    res.status(500).json({ error });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
