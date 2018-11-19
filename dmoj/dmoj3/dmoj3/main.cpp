//
//  main.cpp
//  dmoj3
//
//  Created by Miguel Caringal on 2018-11-11.
//  Copyright © 2018 Miguel Caringal. All rights reserved.
//

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int a;
    bool b = false;
    map<char,int>mymap;
    cin >>a;
    string str;
    vector <char> charlist;
    for (int i = 0; i < a; i++)
    {
        cin >> str;
        if (mymap.find(str[0]) == mymap.end() ) {
            mymap[str[0]] = 1;
        } else {
            mymap[str[0]]++;
        }
    }
    for (auto& kv : mymap) {
        if (kv.second >= 5)
        {
            charlist.push_back(kv.first);
            b = true;
        }
    }
    if (b == false)
    {
        cout << "PREDAJA" << endl;
        return 0;
    }
    sort(charlist.begin(), charlist.end());
    for (int i = 0; i<= charlist.size();i++)
    {
        cout << charlist[i];
    }
    cout << endl;
    return 0;
}

