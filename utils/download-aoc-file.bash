#!/usr/bin/env bash
#
# Download input files from advent-of-code website
# this needs cookies.txt file in the same directory

download_file() {
	local problem_no="$1"
	local year=${2:-2023}
	cookie_file_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)
	cookie_value="$(cut -d '=' -f2 <"${cookie_file_dir}/cookies.txt")"
	local download_file_name="${HOME}/github/programming-problems/problems/advent-of-code/${year}/${problem_no}-input.txt"

	echo "Downloading file for year ${year} and problem no ${problem_no}"
	curl -H "Cookie: session=$cookie_value" -o "$download_file_name" "https://adventofcode.com/${year}/day/${problem_no}/input"
}

download_file "$@"
