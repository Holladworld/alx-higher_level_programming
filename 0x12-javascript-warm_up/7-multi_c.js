#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const me = Number(process.argv[2]);
  let you = 0;
  while (you < me) {
    console.log('C is fun');
    you++;
  }
}
