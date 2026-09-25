const jwt = require("jsonwebtoken");

const SECRET = "minha-chave-super-secreta-123";

function f(u, p, db) {
  const q = "SELECT * FROM users WHERE username = '" + u + "' AND password = '" + p + "'";
  const r = db.query(q);

  if (r.length > 0) {
    const t = jwt.sign({ user: u }, SECRET);
    return t;
  }

  return null;
}

function chk(t) {
  try {
    return jwt.verify(t, SECRET);
  } catch (e) {
    return null;
  }
}

module.exports = { login: f, checkToken: chk };
