use std::clone::Clone;
use std::cmp::PartialOrd;
use std::marker::Copy;

fn merge_sort<T>(arr: &Vec<T>, n: usize) -> Vec<T>
    where T: Copy + Clone + PartialOrd
{
    fn merge<T>(x: Vec<T>, y: Vec<T>, l: usize) -> Vec<T>
        where T: Copy + Clone + PartialOrd
    {
        let mut m: Vec<T> = Vec::new();
        let mut i = 0;
        let mut j = 0;
        let xlim = x.len();
        let ylim = y.len();
        let mut idx = 0;
        while idx < l {
            if i < xlim && j < ylim {
                if x[i] < y[j] {
                    m.push(x[i]);
                    i += 1;
                } else {
                    m.push(y[j]);
                    j += 1;
                }
            } else if i >= xlim {
                m.push(y[j]);
                j += 1;
            } else {
                m.push(x[i]);
                i += 1;
            }
            idx += 1;
        }
        m
    }
    if n == 1 { return arr.to_vec(); }
    let a = merge_sort(&arr[..n/2].to_vec(), n/2);
    let b = merge_sort(&arr[n/2..].to_vec(), n - n/2);
    merge(a, b, n)
}

fn main() {
    let a = vec![2, 1, 5, 3, 10, 8];
    println!("{:?}", merge_sort(&a, a.len()));
    println!("{:?}", a);
}
