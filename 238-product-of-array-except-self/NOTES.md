2 ways,
​
We can maintain 2 arrays, one which contains the prefix products and one which contains the postfix products and then finally multiply the elements of both to get the final product.
​
Example:
​
[4,51,8,2]
​
Prefix array elements would start like :
​
[ 1 (product of all elements before 4), 4 (product of all elements before 5), 20 (product of all elements before 1) , 20 (product of all elements before 1) ... and so on]
​
Postfix would start from end, so the array we work thorugh would look like
[2,8,1,5,4]
​
So the result for post array would look something like this:
[80,16,16,2,1]
​
To get the solution you just need to multiply index *`i` of prefix array to index `i` of postfix array
​