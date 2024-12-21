use std::{
    fs::File,
    io::{self, BufRead},
};

struct FileContents {
    lines: Vec<Vec<i32>>,
}

fn main() -> Result<(), std::io::Error> {
    let path = "/home/alex/dev/advent-of-code-2024/day1/rust/puzzle-input.txt";

    let file_lines = read_lines(path)?;

    let lines: Vec<Vec<i32>> = file_lines
        .filter_map(Result::ok)
        .map(|line| {
            line.split_whitespace()
                .filter_map(|s| s.parse::<i32>().ok())
                .collect()
        })
        .collect();

    let file_contents = FileContents { lines };

    Ok(())
}

fn read_lines(filename: &str) -> io::Result<io::Lines<io::BufReader<File>>> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
