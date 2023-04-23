#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const printcomp = {};
    const boddy = JSON.parse(body);
    boddy.forEach(task => {
      if (task.completed) {
        if (!printcomp[task.userId]) printcomp[task.userId] = 1;
        else printcomp[task.userId] += 1;
      }
    });
    console.log(printcomp);
  }
});
