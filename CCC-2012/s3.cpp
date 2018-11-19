#include <bits/stdc++.h>

using namespace std;

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector <int> list;
    vector <int> key;
    vector <int> dictarr;
    vector <int> imsodone;
    map <int,int> mymap;
    int len, temp, max = 0, keymax, second,largest, highabs=0,secondkey = 0;
    cin >> len;
    for (int i = 0; i<len;i++)
    {
        cin >> temp;
        list.push_back(temp);
    }
    for (int i = 0; i< list.size();i++)
    {
        if (mymap.find(list[i]) == mymap.end())
        {
            mymap[list[i]] = 1;
        }
        else
        {
            mymap[list[i]]+=1;
        }
    }
    for (auto& kv : mymap) 
    {
        if (kv.second > max)
        {
            max = kv.second;
        }
        dictarr.push_back(kv.second);
    }
    for (auto& kv : mymap) 
    {
        if (kv.second == max)
        {
            key.push_back(kv.first);
        }
    }
    if (key.size() == 1)
    {
        if(dictarr[0]<dictarr[1]){ 
            largest = dictarr[1];
            second = dictarr[0];
        }
        else{ 
            largest = dictarr[0];
            second = dictarr[1];
        }
        for (int i = 2; i< dictarr.size() ; i ++) {
            if (dictarr[i] > largest) {
                second = largest;
                largest = dictarr[i];
            }
            else if (dictarr[i] > second && dictarr[i] != largest) {
                second = dictarr[i];
            }
        }
        int counter = 0;
        for (int i = 0; i < dictarr.size();i++)
        {
            if (dictarr[i] == second)
            {
                counter ++;
                secondkey = dictarr[i];
            }
        }
        for (auto& kv : mymap) 
        {
            if (kv.second == secondkey)
            {
                secondkey = kv.first;
            }
        }
        if (counter == 1)
        {
            cout << abs(key[0] - secondkey)  << endl;
        }
        else
        {
            for (auto& kv : mymap) 
            {
                if (kv.second == second)
                {
                    imsodone.push_back(kv.first);
                }
            }
            for (int i = 0; i< imsodone.size();i++)
            {
                if (abs(key[0]-imsodone[i])>highabs)
                {
                    highabs = (abs(key[0]-imsodone[i]));
                }
            }
            cout<< highabs << endl;
        }
    }
    else 
    {
        sort(key.begin(),key.end());
        cout << abs(key[key.size()-1] -key[0]) << endl; 
    }
}