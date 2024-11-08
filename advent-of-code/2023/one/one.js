const fs = require("fs");
const path = require("path");

const readlines = (filename) => {
  let filepath = path.join(__dirname, filename);
  return fs
    .readFileSync(filepath, "utf8", (err, data) => {
      if (err) {
        console.error(err);
        return;
      }
      return data;
    })
    .trim();
};

let filedata = readlines("lines.txt");
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
