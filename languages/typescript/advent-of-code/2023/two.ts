// this runs with deno only
import * as path from "jsr:@std/path" 

// check runtime 
function runtime(): string {
  if (globalThis.Deno) {
    return "deno"
  } else if (globalThis.Bun) {
    return "bun"
  } else {
    return "node"
  }
}

// for simplicity I will assume that file is running via deno
function fileContent(filepath: string): string {
  return Deno.readTextFileSync(filepath).trim()
}

function readLines(fileContent: string): Array<string> {
  return fileContent.split(/\r?\n/).map(line => line.trim())
}

function questionContent(): Array<string> {
  const __dirname = import.meta.dirname 
  const questionFile = path.join(__dirname, "input.txt")
  let content = fileContent(questionFile)
  return readLines(content)
}

// use deno runtime to run this file
const RED_CUBES: number  = 12
const GREEN_CUBES: number = 13
const BLUE_CUBES: number = 14
const ALLOWED_SUM = RED_CUBES + GREEN_CUBES + BLUE_CUBES

function getNumbers(line: string): Array<number> | null {
  let pattern: RegExp = /\d+/g
  let matches = line.match(pattern)
  if (matches && matches.length > 0) {
    return matches.map(x => Number(x))
  } else {
    return null
  }
}

function colorpattern(color: string): RegExp{
  return new RegExp("\\d+ " + color, "g")
}

function colorBalls(line: string, color: string): Array<number|undefined> | null{
  let pattern = colorpattern(color)
  let matches = line.match(pattern)
  if (matches && matches.length > 0) {
    let numbers = matches.map(x => getNumbers(x)?.[0])
    return numbers 
  } else { return null }
}


function ballsSum(line: string): {gameId: number, games: {red:Array<number|undefined>|null, blue:Array<number|undefined>|null, green:Array<number|undefined>|null}} {
  let [idString, gamesString] = line.split(":")
  let gameId = Number(getNumbers(idString)?.[0])
  let red = colorBalls(gamesString, "red")
  let blue = colorBalls(gamesString, "blue")
  let green = colorBalls(gamesString, "green")
  let games = {red, blue, green}
  return {gameId, games}
}

function answer(): number {
  let lines = questionContent()
  let output: number  = 0
  for(let i = 0; i<lines.length; i++) {
    let { gameId, games } = ballsSum(lines[i])
    let {red, blue, green} = games
    if (red.some(x => x > RED_CUBES) || blue.some(x => x > BLUE_CUBES) || green.some(x => x > GREEN_CUBES)) {
      continue
    }  else {
      output = output + gameId
    }
  }
  return output
}

console.log(answer())
