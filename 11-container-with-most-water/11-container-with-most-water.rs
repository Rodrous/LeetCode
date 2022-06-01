impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut mh = 0;
        let mut it = height.into_iter().enumerate();
        let (mut left, mut right) = (it.next(), it.next_back());
        while let (Some((left_pos, left_height)), Some((right_pos, right_height))) = (left, right) {
            let base = (right_pos - left_pos) as i32;
            let min_height = match (left_height, right_height) {
                (height_left, height_right) if height_left < height_right => {
                    left = it.next();
                    height_left
                }
                (_, height_right) => {
                    right = it.next_back();
                    height_right
                }
            };
            mh = mh.max(base * min_height);
        }
        mh
    }
}