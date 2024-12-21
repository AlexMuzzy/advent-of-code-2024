use std::{
    fs::File,
    io::{self, BufRead, Read},
};

fn main() -> Result<(), std::io::Error> {
    let path = "/home/alex/dev/advent-of-code-2024/day1/rust/puzzle-input.txt";

    let mut file = File::open(path)?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;
    println!("Contents of the file: {}", contents);

    if let Ok(lines) = read_lines(path) {
        let mut counter = 0;
        for line in lines {
            if let Ok(ip) = line {
                counter += 1;
                println!("line {}: {}", counter, ip);
            }
        }
    }

    Ok(())
}

fn read_lines(filename: &str) -> io::Result<io::Lines<io::BufReader<File>>> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
