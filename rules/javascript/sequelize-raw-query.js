// ruleid: sequelize-raw-query
db.sequelize.query(
  `INSERT INTO user (username, password) VALUES('${username}','${password}')`
)

var query = `INSERT INTO user (username, password) VALUES('${username}','${password}')`
// ruleid: sequelize-raw-query
db.sequelize.query(query)

// ruleid: sequelize-raw-query
db.sequelize.query(
  "INSERT INTO user (username, password) VALUES('" + username + "','" + password + "')"
)

var query = "INSERT INTO user (username, password) VALUES('" + username + "','" + password + "')"
// ruleid: sequelize-raw-query
db.sequelize.query(query)
