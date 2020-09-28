#include <iostream>
#include <string.h>

using namespace std;

long* partitio(long *arr, int left, int right)
{
    long ind1 = left;
    long ind2 = (right - left) / 2 + left;
    long ind3 = right - 1;
    if (arr[ind3] < arr[ind1]) {
        swap(ind1, ind3);
    }
    if (arr[ind3] < arr[ind2]) {
        swap(ind2, ind3);
    }
    if (arr[ind2] < arr[ind1]) {
        swap(ind1, ind2);
    }

    long pvt1 = left;
    long count_mid = 0;
    long mid = arr[ind2];
    long pvt2 = 0;

    for(long i = left; i < right; i++) {
        pvt2 = pvt1 + count_mid;
        if (arr[i] < mid) {
            swap(arr[pvt1], arr[i]);
            if (count_mid > 0) {
                swap(arr[pvt2], arr[i]);
            }
            pvt1++;
        } else if (arr[i] == mid) {
            swap(arr[pvt2], arr[i]);
            count_mid++;
        }
    }

    long* indxes = new long[2];
    indxes[0] = pvt1;
    indxes[1] = pvt1 + count_mid;
    return indxes;
}

long statist(long *arr, long left, long right, long k)
{
    long k_stat = 0;
    while (true) {
        long* indxes = partitio(arr, left, right);
        if (k <= indxes[0]) {
            right = indxes[0];
        } else if (k <= indxes[1]) {
            k_stat = arr[indxes[0]];
            delete [] indxes;
            return k_stat;
        } else {
            left = indxes[1];
        }
        delete [] indxes;
    }
}

int main()
{
    int n = 0;
    cin >> n;
    long* arr = new long[n];
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long m = 0;
    cin >> m;
    long i = 0;
    long j = 0;
    long k = 0;

    for(long p = 0; p < m; p++) {
        cin >> i >> j >> k;
        long* arr_part = new long[j - i + 1];
        for(long q = 0; q < j - i + 1; q++) {
            arr_part[q] = arr[q + i - 1];
        }
        long answer = statist(arr_part, 0, j - i + 1, k);
        delete [] arr_part;
        cout << answer << '\n';
    }

    delete [] arr;
    return 0;
}
