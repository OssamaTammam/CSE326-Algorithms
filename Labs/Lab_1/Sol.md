# Lab 1

## Problem 1: Binary Search
Develop an algorithm for recursive Binary Search.

Python solution:
```python
def binary_search(arr, low, high, key):  
    if low > high:  
        return -1  
  mid = (low + high) // 2  
  if arr[mid] == key:  
        return mid  
    if key < arr[mid]:  
        return binary_search(arr, low, mid - 1, key)  
    return binary_search(arr, mid + 1, high, key)
```

Java solution:
```java
public static int binarySearch(int[] A, int x) {  
    return binarySearchInternal(A, x, 0, A.length - 1);  
}  
  
public static int binarySearchInternal(int[] A, int x, int i, int j) {  
    if (i > j) {  
        return -1;  
    }  
  
    int mid = (i + j) / 2;  
  
    if (A[mid] == x) {  
        return mid;  
    } else if (A[mid] > x) {  
        return binarySearchInternal(A, x, i, mid - 1);  
    } else {  
        return binarySearchInternal(A, x, mid + 1, j);  
    }  
}
```

## Problem 2: Palindrome Check
Develop a recursive algorithm to check for a given string if it's palindrome or not.

Very similar LeetCode Problem: https://leetcode.com/problems/valid-palindrome/

Python solution:
```python
def check_palindrome(s, low, high):  
    if low >= high:  
        return True  
 if s[low] == s[high]:  
        return check_palindrome(s, low + 1, high - 1)  
    return False
```

Java solution:
```java
public static boolean isPalindrome(String s) {  
    return isPalindromeInternal(s, 0, s.length() - 1);  
}  
  
public static boolean isPalindromeInternal(String s, int i, int j) {  
    if (i > j) {  
        return true;  
    }  
  
    if (s.charAt(i) != s.charAt(j)) {  
        return false;  
    }  
      
    return isPalindromeInternal(s, i + 1, j - 1);  
}
```

## Problem 3: Power
https://leetcode.com/problems/powx-n/

Python solution:
```python
def pow(x, n):  
    if n == 0:  
        return 1  
  elif n < 0:  
        return 1 / pow(x, -n)  
    else:  
        y = pow(x, n // 2)  
        if n % 2 == 0:  
            return y * y  
        else:  
            return y * y * x
```

Java solution:
```java
public static double pow(double x, int n) {  
    if (n == 0) {  
        return 1;  
    }  
  
    if (n % 2 == 0) {  
        return pow(x * x, n / 2);  
    } else {  
        if (n < 0) {  
            return pow(x * x, n / 2) / x;  
        } else {  
            return pow(x * x, n / 2) * x;  
        }  
    }  
}
```

## Problem 4: Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Note: The two solutions below are fundamentally different, unlike the ones for the previous problems which were mostly identical.

Python solution:
```python
def rotated_binary_search(arr, low, high, key):  
    if low > high:  
        return -1  
  
  mid = (low + high) // 2  
  if key == arr[mid]:  
        return mid  
    elif key < arr[mid]:  
        if key >= arr[low] or arr[mid] < arr[high]:  
            return rotated_binary_search(arr, low, mid - 1, key)  
        else:  
            return rotated_binary_search(arr, mid + 1, high, key)  
    else:  
        if key <= arr[high] or arr[low] < arr[mid]:  
            return rotated_binary_search(arr, mid + 1, high, key)  
        else:  
            return rotated_binary_search(arr, low, mid - 1, key)
```

Java solution:
```java
public static int rotatedBinarySearch(int[] A, int x) {  
    if (A.length == 0) {  
        return -1;  
    }  
  
    int offset = findOffset(A, 0, A.length - 1);  
  
    return rotatedBinarySearchInternal(A, x, offset, A.length - 1 + offset);  
}  
  
public static int findOffset(int[] A, int i, int j) {  
    if (i == j) {  
        return i;  
    }  
  
    int mid = (i + j) / 2;  
  
    if (A[mid] < A[j]) {  
        return findOffset(A, i, mid);  
    } else {  
        return findOffset(A, mid + 1, j);  
    }  
}  
  
public static int rotatedBinarySearchInternal(int[] A, int x, int i, int j) {  
    if (i > j) {  
        return -1;  
    }  
  
    int mid = (i + j) / 2;  
  
    if (A[mid % A.length] == x) {  
        return mid % A.length;  
    } else if (A[mid % A.length] > x) {  
        return rotatedBinarySearchInternal(A, x, i, mid - 1);  
    } else {  
        return rotatedBinarySearchInternal(A, x, mid + 1, j);  
    }  
}
```