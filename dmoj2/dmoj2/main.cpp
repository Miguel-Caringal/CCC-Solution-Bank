//
//  main.cpp
//  dmoj2
//
//  Created by Miguel Caringal on 2018-11-11.
//  Copyright © 2018 Miguel Caringal. All rights reserved.
//

#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    
    map<char,char>mymap;
    mymap ['0'] = 'O';
    mymap ['1'] = 'l';
    mymap ['3'] = 'E';
    mymap ['4'] = 'A';
    mymap ['5'] = 'S';
    mymap ['6'] = 'G';
    mymap ['8'] = 'B';
    mymap ['9'] = 'g';
    string str;
    cin >> str;
    for (int i =0; i <= str.length(); i++)
    {
        if (mymap.find(str[i]) == mymap.end() ) {
            // not found
        } else {
            str[i] = mymap[str[i]];
        }
    }
    cout <<str;
    return 0;
}
