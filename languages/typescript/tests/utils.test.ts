import * as utils from '@utils/utils'
import * as utilEnums from '@utils/enums'
import * as process from 'process'

beforeAll(() => {
  process.env.HOME = "."
})


describe("Testing filepath functions", () => {
  test("problemFilePath", () => {
    expect(utils.problemFilePath("abc.txt")).toBe("problems/abc.txt")
  })
  test("aocFilePath", () => {
    expect(utils.aocFilePath(1, 2023)).toBe("problems/advent-of-code/2023/1-input.txt")
  })


  test("leet code file path", () => {
    expect(utils.leetcodeFilePath("abc.txt")).toBe("problems/leetcode/abc.txt")
  })
})
