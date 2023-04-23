#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
