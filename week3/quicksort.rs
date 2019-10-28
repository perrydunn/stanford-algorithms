use std::cmp::PartialOrd;
use std::marker::Copy;

fn choose_first<T: Copy>(arr: &mut Vec<T>, l: usize, _: usize) -> T {
    arr[l]
}

fn choose_last<T: Copy>(arr: &mut Vec<T>, l: usize, r: usize) -> T {
    let elem = arr[r-1];
    arr[r-1] = arr[l];
    arr[l] = elem;
    arr[l]
}

fn choose_of_three<T>(arr: &mut Vec<T>, l: usize, r: usize) -> T 
    where T: Copy + PartialOrd
{
    let n = r - l;
    let med: usize = if n % 2 == 0 {
        n / 2 - 1 
    } else {
        n / 2
    };
    let elem_0 = arr[l];
    let elem_m = arr[l+med];
    let elem_n = arr[r-1];
    if (elem_0 <= elem_m && elem_m <= elem_n) ||
            (elem_0 >= elem_m && elem_m >= elem_n) {
        arr[l+med] = arr[l];
        arr[l] = elem_m;
        arr[l]
    } else if (elem_m <= elem_0 && elem_0 <= elem_n) ||
            (elem_m >= elem_0 && elem_0 >= elem_n) {
        arr[l]
    } else {
        arr[r-1] = arr[l];
        arr[l] = elem_n;
        arr[l]
    }
}

fn quicksort<T>(arr: &mut Vec<T>, choose_pivot: fn(&mut Vec<T>, usize, usize) -> T) -> usize
    where T: PartialOrd + Copy
{
    let l = 0;
    let r = arr.len();
    let mut n = 0;

    fn rec_quicksort<T>(
            arr: &mut Vec<T>, l: usize, r: usize,
            choose_pivot: fn(&mut Vec<T>, usize, usize) -> T,
            n: &mut usize
        ) -> () 
        where T: PartialOrd + Copy
    {
        if r - l < 2 {
            return ()
        }
        // This could be < 0 so it's important this follows the above if and return
        *n += r - l - 1;
        let p = choose_pivot(arr, l, r);
        let mut i = l;  // i splits the < p and >= p
        let mut elem;
        for j in l+1..r {
            if arr[j] < p {
                i += 1;
                elem = arr[i];
                arr[i] = arr[j];
                arr[j] = elem;
            }
        }
        arr[l] = arr[i];
        arr[i] = p;
        rec_quicksort(arr, l, i, choose_pivot, n);
        rec_quicksort(arr, i+1, r, choose_pivot, n);
    }

    rec_quicksort(arr, l, r, choose_pivot, &mut n);
    n
}

fn main() {
    let mut a = vec![2, 1, 5, 3, 10, 8];
    println!("{:?}", &a);
    let ops = quicksort(&mut a, choose_first);
    println!("{} -> {:?}", ops, a);
    let mut a = vec![2, 1, 5, 3, 10, 8];
    let ops = quicksort(&mut a, choose_last);
    println!("{} -> {:?}", ops, a);
    let mut a = vec![2, 1, 5, 3, 10, 8];
    let ops = quicksort(&mut a, choose_of_three);
    println!("{} -> {:?}", ops, a);
}
