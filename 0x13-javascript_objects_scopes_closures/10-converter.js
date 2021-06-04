#!/usr/bin/node
exports.converter = function (base) {
  function hex (number) {
    return number.toString(base);
  }
  return hex;
};
