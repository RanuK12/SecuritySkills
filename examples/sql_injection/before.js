// Before: Vulnerable SQL query
const db = require('./db');
app.get('/users', (req, res) => {
  const query = ;
  db.query(query, (err, results) => {
    if (err) console.error(err);
    res.send(results);
  });
});
