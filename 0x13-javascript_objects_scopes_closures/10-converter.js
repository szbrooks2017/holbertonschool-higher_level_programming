#!/usr/bin/node
exports.converter = function (base) {
  function hex (number) {
    return number.tostring(base);
  }
  return hex;
};
