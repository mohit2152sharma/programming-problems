import * as process from "process"
import { PROBLEM_ROOT_DIR } from "./const"
import * as path from "path"
import * as fs from "node:fs"
import { ProblemDirPaths } from "./enums"

function problemFilePath(filePath: string): string {
  let homeDir = process.env.HOME as string
  let basePath = path.join(homeDir, "github", "programming-problems", PROBLEM_ROOT_DIR)
  return path.join(basePath, filePath)
}

function aocFilePath(problemNo: number, year: number): string {
  let fileName = problemNo.toString() + "-input.txt"
  let filePath: string = path.join(ProblemDirPaths.AOC, year.toString(), fileName)
  return problemFilePath(filePath)
}

function leetcodeFilePath(filePath: string): string {
  return problemFilePath(path.join(ProblemDirPaths.LEETCODE, filePath))
}

function aocFile(problemNo: number, year: number = 2023): string {
  return fs.readFileSync(aocFilePath(problemNo, year), "utf-8")
}

function leetcodeFile(probleName: string): string {
  return fs.readFileSync(leetcodeFilePath(probleName), "utf-8")
}
export {
  problemFilePath,
  aocFilePath, 
  leetcodeFilePath,
  leetcodeFile,
  aocFile
}

