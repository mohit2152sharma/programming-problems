import { aocFile } from "@utils/utils";
import * as process from 'process'
import * as fs from 'fs';

// Assuming the nubmer's index is i and the number of digits is d, 
// and L is the total number of characters in the line, then the position
// I need to check for special characters are: 
// i + d + 1 (for the index immediately after the number)
// i - 1 (for the index before the number)
// i - L + d + 1 (for the index in top right corner)
// i - L - 1 (for the index in top left corner)
// i + L + d + 1 (for the index in bottom right corner)
// i + L - 1 (for the index in bottom left corner)
// There are special cases when i is equal to 0 or L
//
const allDot = (arr: string): boolean => {
  return arr === ".".repeat(arr.length)
}

const extractDigits = (input: string, index: number, firstDigit: string): { digits: string, k: number } => {
  let digits = firstDigit
  let k = 0
  while (true) {
    let nextDigit = parseInt(input[index + k + 1])
    if (!isNaN(nextDigit)) {
      digits = digits + nextDigit.toString()
      k++
    } else { break }
  }
  return { digits, k }
}

const checkNextPosition = (input: string, index: number): boolean => {
  return input[index + 1] !== "."
}

const checkPrevPosition = (input: string, index: number): boolean => {
  return input[index - 1] !== "."
}

const checkLeftRight = (input: string, startingIndex: number, endingIndex: number): boolean => {
  return checkPrevPosition(input, startingIndex) || checkNextPosition(input, endingIndex)
}

const checkLine = (line: string, startingIndex: number, endingIndex: number): boolean => {
  let block = line.slice(startingIndex, endingIndex + 1)
  return !allDot(block)
}

const checkTopBottomLine = (topLine: string, bottomLine: string, startingIndex: number, endingIndex: number): boolean => {
  return checkLine(topLine, startingIndex, endingIndex) || checkLine(bottomLine, startingIndex, endingIndex)
}


const getAnswer = (input: string): number => {
  let lines = input.split("\n").map(x => x.trim()).filter(x => x)
  let correctNumbers: Array<string> = []
  for (let N = 0; N < lines.length; N++) {
    if (N === 0) {
      for (let i = 0; i < lines[N].length; i++) {
        let firstDigit = parseInt(lines[N][i])
        if (firstDigit) {
          let { digits, k } = extractDigits(lines[N], i, firstDigit.toString())
          if (i === 0) {
            if (checkNextPosition(lines[N], i + k) || checkLine(lines[N + 1], i, i + k + 1)) correctNumbers.push(digits)
            // i + k for multi digit number which are in the end
            // like ....530
          } else if (i + k === lines[N].length - 1) {
            if (checkPrevPosition(lines[N], i) || checkLine(lines[N + 1], i - 1, i)) correctNumbers.push(digits)
          } else {
            if (checkLeftRight(lines[N], i, i + k) || checkLine(lines[N + 1], i - 1, i + k + 1)) correctNumbers.push(digits)
          }
          i += k
        }
      }
    } else if (N === lines.length - 1) {
      for (let i = 0; i < lines[N].length; i++) {
        let firstDigit = parseInt(lines[N][i])
        if (firstDigit) {
          let { digits, k } = extractDigits(lines[N], i, firstDigit.toString())
          if (i === 0) {
            if (checkNextPosition(lines[N], i + k) || checkLine(lines[N - 1], i, i + k + 1)) correctNumbers.push(digits)
          } else if (i + k === lines[N].length - 1) {
            if (checkPrevPosition(lines[N], i) || checkLine(lines[N - 1], i - 1, i)) correctNumbers.push(digits)
          } else {
            if (checkLeftRight(lines[N], i, i + k) || checkLine(lines[N - 1], i - 1, i + k + 1)) {
              correctNumbers.push(digits)
            }
          }
          i += k
        }
      }
    } else {
      for (let i = 0; i < lines[N].length; i++) {
        let firstDigit = parseInt(lines[N][i])
        if (firstDigit) {
          let { digits, k } = extractDigits(lines[N], i, firstDigit.toString())
          if (i === 0) {
            if (checkNextPosition(lines[N], i + k) || checkTopBottomLine(lines[N - 1], lines[N + 1], i, i + k + 1)) correctNumbers.push(digits)
          } else if (i + k === (lines[N].length - 1)) {
            if (checkPrevPosition(lines[N], i) || checkTopBottomLine(lines[N - 1], lines[N + 1], i - 1, i)) correctNumbers.push(digits)
          } else {
            if (checkLeftRight(lines[N], i, i + k) || checkTopBottomLine(lines[N - 1], lines[N + 1], i - 1, i + k + 1)) correctNumbers.push(digits)
          }
          i += k
        }
      }
    }
  }

  return correctNumbers.map(x => parseInt(x)).reduce((a, b) => a + b, 0)
}

if (process.argv[2]) {
  const inputFilePath = process.argv[2]
  const inputFile = fs.readFileSync(inputFilePath, 'utf-8')
  const answer = getAnswer(inputFile)
  console.log("🪚 answer:", answer);
} else {
  const inputFile = aocFile(3, 2023);
  const answer = getAnswer(inputFile)
  console.log("🪚 answer:", answer);
}
