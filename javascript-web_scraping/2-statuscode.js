#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request.get(args[0], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
});
