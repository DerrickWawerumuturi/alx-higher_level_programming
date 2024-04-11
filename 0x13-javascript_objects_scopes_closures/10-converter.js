#!/usr/bin/node

exports.converter = function (base) {
  if (base < 2 || base > 36) {
    console.log('Invalid base');
  }
  return  function (num) {
   return num.toString(base);
  };
};
