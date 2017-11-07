var admin = require("firebase-admin");

var serviceAccount = require("config.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://studycat-f990d.firebaseio.com"
});

// Get a reference to the database service
var database = admin.database();

module.exports = database;