const fs = require("fs");
const path = require("path");

const readlines = (filename) => {
  // let filepath = path.join(__dirname, filename);
  return fs
    .readFileSync(filename, "utf8", (err, data) => {
      if (err) {
        console.error(err);
        return;
      }
      return data;
    })
    .trim();
};

// pass the input filename as command line argument
let filename = process.argv.slice(2)[0]
if (!filename) {
  throw new Error('Input filename is required with full path')
} 
let filedata = readlines(filename);
let lines = filedata.split("\n");
let sum = 0;

for (let j = 0; j < lines.length; j++) {
  let first_char;
  let last_char;
  let line = lines[j];

  for (let i = 0; i < line.length; i++) {
    if (!isNaN(parseInt(line[i]))) {
      first_char = line[i];
      break;
    }
  }

  for (let k = line.length - 1; k >= 0; k--) {
    if (!isNaN(parseInt(line[k]))) {
      last_char = line[k];
      break;
    }
  }

  let number = parseInt(first_char + last_char);
  sum += number;
}

console.log(sum);
