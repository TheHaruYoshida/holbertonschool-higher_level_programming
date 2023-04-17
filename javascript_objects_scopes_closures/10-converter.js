#!/usr/bin/node
exports.converter = function (base) {
  function conver (number) {
    return number.toString(base);
  }
  return conver;
};
