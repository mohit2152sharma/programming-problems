#!/usr/bin/env bash
#
# Download input files from advent-of-code website
# this needs cookies.txt file in the same directory

download_file() {
	local problem_no="$1"
	cookie_file_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)
	cookie_value="$(cut -d '=' -f2 <"${cookie_file_dir}/cookies.txt")"
	local download_file_name=input.txt

	curl -H "Cookie: session=$cookie_value" -o "$download_file_name" "https://adventofcode.com/2023/day/${problem_no}/input"
}

download_file "$@"
