#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <limits.h>

using namespace std;

int main ()
{
    vector <int> a;
    int len, temp, curr, mindiff = INT_MAX;
    cin >> len;
    for (int i =0; i<len;i++)
    {
        cin >> temp;
        a.push_back(temp);
    }
    sort(a.begin(),a.end());
    for (int i = 0; i<len-1;i++)
    {
        curr = abs(a[i] - a[i+1]);
        if (curr < mindiff)
        {
            mindiff = curr;
        }
    }
    cout << mindiff << endl;
}