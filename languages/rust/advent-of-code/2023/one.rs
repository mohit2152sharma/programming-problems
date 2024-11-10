// Read file from the system

use std::env;
use std::fs;
use std::path::PathBuf;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_name = &args[1];

    let current_dir: PathBuf = match env::current_dir() {
        Ok(path) => path,
        Err(e) => {
            println!("Error getting the current directory: {}", e);
            return;
        }
    };

    let file_path = current_dir.join(file_name);
    let content = match fs::read_to_string(&file_path) {
        Ok(content) => content,
        Err(e) => {
            println!("Unable to read the content of file: {}", file_name);
            return;
        }
    };


    let mut sum: i32 = 0;
    for line in content.lines() {
        let mut first_digit: char = '\0';
        let mut second_digit: char = '\0';
        for ch in line.chars() {
            if ch.is_digit(10) {
                first_digit = ch;
                break;
            };
        };

        for ch in line.chars().rev() {
            if ch.is_digit(10) {
                second_digit = ch;
                break;
            };
        };
        match format!("{}{}", first_digit, second_digit).parse::<i32>() {
            Ok(value) => sum += value,
            Err(e) => return,
        }
    };
    println!("{}", sum)
}
