//
//  main.cpp
//  dmoj6
//
//  Created by Miguel Caringal on 2018-11-12.
//  Copyright © 2018 Miguel Caringal. All rights reserved.
//

#include <iostream>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    map <string,string> mymap;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n , pointer;
    string key, value ,sentence, word ,finalstr = "";
    cin >> n;
    for (int i = 0;i < n;i++)
    {
        cin >> value;
        cin >> key;
        mymap[key] = value;
    }
    cin >> sentence;
    for (int i =0; i < sentence.length();i++)
    {
        if (sentence[i] == ' ')
        {
            if (mymap.find(word) != mymap.end())
            {
                word =
            }
        }
        else{
            word += sentence[i];
        }
    }
    return 0;
}
