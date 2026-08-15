// After: Parameterized query
const db = require('./db');
app.get('/users', (req, res) => {
  const query = 'SELECT * FROM users WHERE name = ?';
  db.query(query, [req.query.name], (err, results) => {
    if (err) console.error(err);
    res.send(results);
  });
});
