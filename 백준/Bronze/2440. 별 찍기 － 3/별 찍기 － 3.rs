use std::io;
fn main() {
    let mut input_number= String::new();
    io::stdin().read_line(&mut input_number).unwrap();
    let number:Vec<&str> = input_number.split_whitespace().collect();
    let n =number[0].parse::<i32>().unwrap();
    for i in 0..n
        {
            println!("{}","*".repeat((n-i) as usize));
        }
}
