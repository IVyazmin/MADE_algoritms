#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    const long long POW_2_16 = pow(2, 16);
    const long long POW_2_30 = pow(2, 30);

    long n = 0;
    long long x = 0;
    long long y = 0;
    long long a_0 = 0;
    long m = 0;
    long long z = 0;
    long long t = 0;
    long long b_0 = 0;

    cin >> n >> x >> y >> a_0;
    cin >> m >> z >> t >> b_0;

    long long* pre_sum = new long long[n];
    long long a_next = a_0;

    pre_sum[0] = a_0;
    for(long i = 1; i < n; i++)
    {
        a_next = (x * a_next + y) % POW_2_16;
        pre_sum[i] = pre_sum[i - 1] + a_next;
    }

    long long b_first = b_0;
    long long b_second = (z * b_first + t) % POW_2_30;
    long c_first = 0;
    long c_second = 0;
    long left = 0;
    long right = 0;
    long long total_sum = 0;

    for(long i = 0; i < m; i++)
    {
        c_first = b_first % n;
        c_second = b_second % n;
        left = min(c_first, c_second);
        right = max(c_first, c_second);
        total_sum = total_sum + pre_sum[right];
        if (left > 0)
        {
            total_sum = total_sum - pre_sum[left - 1];
        }
        b_first = (z * b_second + t) % POW_2_30;
        b_second = (z * b_first + t) % POW_2_30;
    }
    cout << total_sum;
    delete [] pre_sum;
    return 0;
}
