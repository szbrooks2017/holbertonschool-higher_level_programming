#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const x in list) {
    if (list[x] === searchElement) {
      count++;
    }
  }
  return count;
};
