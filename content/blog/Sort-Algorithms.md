Title: Sort Algorithms
Tags: Algorithm,cpp
lang: zh
Slug: sort-algorithms
Summary: 排序算法总结
Date: 2018-08-05


------------------------


# 工具函数

```cpp
#include <iostream>
#include <ctime>

using namespace std;

void swap(int &a,int &b){
    int tmp = a;
    a = b;
    b = tmp;
}

void printarr(int *a,int n){
    for(size_t i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}
```

# Bubble Sort 冒泡排序

```cpp
void bubble_sort(int *a, int n){
    for(size_t i = n-1; i > 0;--i){
        for(size_t j = i; j > 0;--j)
        {
            if(a[j] < a[j-1])
                swap(a[j],a[j-1]);
        }
    }
}

void bubble_sort_speedup(int *a, int n){
    for(size_t i = 0; i < n-1; i++){
        int flag = 0;
        for(size_t j = 0; j < n-1-i; ++j){
            if(a[j] > a[j+1]){
                swap(a[j],a[j+1]);
                flag = 1;
            }
        }
        if(!flag)
            break;
    }
}
```

# Cocktail Sort 鸡尾酒排序

```cpp
void cocktail_sort(int *a,int n){
    int left = 0;
    int right = n-1;
    while(left < right){
        for(size_t i = left; i<right;++i){
            if(a[i] > a[i+1])
                swap(a[i],a[i+1]);
        }
        right--;
        for(size_t j = right;j>left;--j){
            if(a[j-1] > a[j]){
                swap(a[j-1],a[j]);
            }
        }
        left++;
    }
}
```

```cpp
void cocktail_sort_speedup(int *a,int n){
    bool sorted = false;
    while(!sorted){
        sorted = true;
        for( int i = 0; i < n - 1; i++ ){
            if( a[i] > a[i + 1] ){
                swap( a[i], a[i + 1] );
                sorted = false;
            }
        }
        if(sorted)
            break;
        sorted = true;
        for( int j = n - 1; j > 0; j-- ){
            if( a[j - 1] > a[j] ){
                swap( a[j], a[j - 1] );
                sorted = false;
            }
        }
    }
}
```

# Selection Sort 选择排序

```cpp
void selection_sort(int *a, int n){
    for(size_t i = 0;i < n-1;i++){
        int index = i;
        for(size_t j = i+1;j < n;j++){
            if(a[j] < a[index])
                index = j;
        }
        if(i!=index)
            swap(a[i],a[index]);
    }
}
```

# Insertion Sort 插入排序

```cpp
void insertion_sort(int *a, int n){
    for(size_t i = 1;i < n;i++){
        int tmp = a[i];
        size_t j = i;
        while(j > 0 && tmp < a[j-1]){
            a[j] = a[j-1];
            --j;
        }
        a[j] = tmp;
    }
}
```

# Shell Sort 希尔排序

```cpp
void shell_sort(int *a,int n){
    int h,i,j,t;
    for(h = n;h/=2;){
        // iterator
        for(i=h;i<n;i++){
            t=a[i];
            for(j=i;j>=h && t<a[j-h];j-=h){
                a[j] = a[j-h];
            }
            a[j] = t;
        }
    }
}
```

```cpp
void shell_sort_speedup(int *a,int n){
    int i,j,tmp,step;
    step = n;
    while(step>1){
        step = step/3+1;
        // insert sort
        for(i=step;i<n;i++){
            tmp = a[i];
            for(j=i;j>0 && a[j] < a[j-step];j-=step){
                a[j] = a[j-step];
            }
            a[j] = tmp;
        }
    }
}
```

# Merge Sort归并排序

递归版本

```cpp
void merge_arr(int *a,int m,int n){
    int i,j,k;
    int *temp = new int[n];
    // 0 ---> n
    for(i=0,j=m,k=0;k<n;k++){
        temp[k] = j == n ?
            a[i++]:i == m ?
            a[j++]:a[j] < a[i]?
            a[j++]:a[i++];
    }
    for(k=0;k<n;k++){
        a[k] = temp[k];
    }
    delete [] temp;
}
void merge_sort(int *a,int n){
    if(n < 2)
        return;
    int m = n/2;
    merge_sort(a,m);
    merge_sort(a+m,n-m);
    merge_arr(a,m,n);
}
```

非递归版本

```cpp
void merge_arr2(int *a,int left,int mid,int right){
    int i = left;
    int j = mid + 1;
    int k = 0;
    int len = right-left+1;
    int *temp = new int[len];
    // while(i <= mid && j <= right){
    //     temp[k++] = a[i] <= a[j] ? a[i++] : a[j++];
    // }
    // while(i <= mid){
    //     temp[k++] = a[i++];
    // }
    // while(j <= right){
    //     temp[k++] = a[j++];
    // }
    for(;k<len;k++){
        temp[k] = j > right?
                a[i++]:i > mid?
                a[j++]:a[i] < a[j]?
                a[i++]:a[j++];
    }
    for(k = 0; k< len;){
        a[left++] = temp[k++];
    }

    delete [] temp;
}
void merge_sort(int *a,int len){
    // int left,mid,right,n;
    int left,n;
    for(int i = 2;i/2 < len;i*=2){
        // left = 0;
        // for(left=0;left+i<len;){
        //     mid = left + i - 1;
        //     right = mid + i < len ? mid + i : len - 1;
        //     n = mid + i < len ? 2*i : len - left+1;
        //     merge_arr(a+left,mid,n);
        //     left = right + 1 ;
        // }
        for(left = 0;left < len;left+=i){
            // mid = left + i/2;
            n = left + i < len?i:len-left;
            merge_arr(a+left,i/2,n);
        }
    }
}
```

# Qucik Sort 快速排序


```cpp
void quick_sort(int *a,int len){
    if(len<2)
        return;
    int i,j;
    int pivot = a[len/2];
    for(i=0,j=len-1;;i++,j--){
        while(a[i] < pivot) i++;
        while(a[j] > pivot) j--;
        if(i >= j) break;
        // swap value
        swap(a[i],a[j]);
    }
    quick_sort(a,i);
    quick_sort(a+i,len-i);
}
```

```cpp
void quick_sort2(int *a,int n){
    if(n<2) return;
    int mid=a[0]; // pivot
    int i=0,j=n-1;
    while(i<j){
        while(j>i && a[j]>=mid) j--;
        if(j>i){
            a[i]=a[j];
            i++;
        }
        while(i<j && a[i]<mid) i++;
        if(i<j){
            a[j]=a[i];
            j--;
        }
    }
    a[i]=mid;
    quick_sort2(a,i);
    quick_sort2(a+i+1,n-i-1);
}
```
# Heap Sort 堆排序

递归版本

```cpp
// i is index of array,the left child index is 2*i+1,the right one is 2*i+2,the father index is floor((i-1)/2)
void siftDown(int *a, int i, int n)
{
    int lhs=2*i+1;
    int rhs=2*i+2;
    int maxid=i;
    if(lhs<n && a[maxid]<a[lhs]) maxid=lhs;
    if(rhs<n && a[maxid]<a[rhs]) maxid=rhs;
    if(maxid!=i)
    {
        swap(a[i],a[maxid]);
        siftDown(a,maxid,n);
    }
}

// void makeHeap(int *a, int n){
//     for(int i=n/2-1; i>=0; i--)
//     {
//         siftDown(a,i,n);
//     }
// }

void heap_sort(int *a,int n){
    // makeHeap(a,n);
    for(int i=n/2-1; i>=0; i--){
        siftDown(a,i,n);
    }
    for(int i=n-1; i>0; i--){
        swap(a[0],a[i]);
        siftDown(a,0,i);
    }
}
```

非递归版本

```cpp
void heap_down(int *a,int i,int n){
    int lc = 2*i+1;
    for(;lc<n;i=lc,lc=2*i+1){
        // lc + 1 < n right chid index can't greater than the array length
        if(lc+1 < n && a[lc]<a[lc+1])
            lc++;
        if(a[i] >= a[lc])
            break;
        else
            swap(a[i],a[lc]);
    }
}

void heap_sort2(int *a,int n){
    // makeHeap(a,n);
    for(int i=n/2-1; i>=0; i--){
        heap_down(a,i,n);
    }
    for(int i=n-1; i>0; i--){
        swap(a[0],a[i]);
        heap_down(a,0,i);
    }
}
```

# Counting Sort 计数排序

```cpp
void couting_sort(int *a,int n){
    int range = 20;
    int *C = new int[range];
    int *temp = new int[n];
    for(int i = 0;i < range;i++){
        C[i] = 0;
        if(i<n)
            temp[i]=0;
    }
    for(int j = 0;j < n;j++){
        C[a[j]]++;
    }
    for(int i = 1;i < range;i++){
        C[i]+=C[i-1];
    }
    for(int j = n-1;j >= 0;j--){
        temp[--C[a[j]]] = a[j];
    }
    for (int j = 0; j < n; j++){
        a[j] = temp[j];
    }
    delete [] C;
    delete [] temp;
}
```

# 算法对比

> 稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。

> 不稳定：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。

> 时间复杂度：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。

> 空间复杂度：是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。


|算法名称|时间复杂度（最好）|时间复杂度（平均）|时间复杂度（最坏）|空间复杂度|稳定性|
|:---|:---:|:---:|:---:|:---:|:---:|
|Insertion Sort|O(n)|O(n^2)|O(n^2)|O(1)|稳定|
|Shell Sort|O(n)|O(n^1.3)|O(n^2)|O(1)|不稳定|
|Selection Sort|O(n^2)|O(n^2)|O(n^2)|O(1)|不稳定|
|Heap Sort|O(nlog n)|O(nlog n)|O(nlog n)|O(1)|稳定|
|Bubble Sort|O(n)|O(n^2)|O(n^2)|O(1)|稳定|
|Cocktail Sort|O(n)|O(n^2)|O(n^2)|O(1)|稳定|
|Qucik Sort|O(nlog n)|O(nlog n)|O(n^2)|O(nlog n)~O(n)|不稳定|
|Merge Sort|O(nlog n)|O(nlog n)|O(nlog n)|O(n)|稳定|
|Counting Sort|O(n+k)|O(n+k)|O(n+k)|O(n+k)|稳定|
|Bucket Sort|O(n)|O(n+k)|O(n^2)|O(n+k)|稳定|
|Radix Sort|O(n\*k)|O(n\*k)|O(n\*k)|O(n+k)|稳定|

# 引用

- [Moondark](http://liaoxl.github.io/blog/20140907/sort/)
- [SteveWang](https://www.cnblogs.com/eniac12/p/5329396.html)
- [rosettacode](http://rosettacode.org/wiki/Sorting_algorithms)
- [一像素](https://www.cnblogs.com/onepixel/articles/7674659.html)