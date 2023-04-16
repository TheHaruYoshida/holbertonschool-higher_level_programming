#!/usr/bin/node
exports.esrever = function (list) {
    let listreversed = [];
    for (let i = 0; i < list.length; i++) {
      listreversed.unshift(list[i]);
    }
    return listreversed;
  };
  