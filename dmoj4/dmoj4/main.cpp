//
//  main.cpp
//  dmoj4
//
//  Created by Miguel Caringal on 2018-11-11.
//  Copyright © 2018 Miguel Caringal. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    vector <int> list;
    for (int i = 0; i<5;i++)
    {
        string str1,str2;
        int counter = 0;
        getline(cin,str1);
        getline(cin,str2);
        for (int i = 0; i< str1.length(); i++)
        {
            if (i != str2.length())
            {
                if (str1[i] == str2[i])
                {
                    counter +=1;
                }
                else
                {
                    counter = 0;
                    break;
                }
            }
            else
            {
                break;
            }
        }
        list.push_back(counter);
    }
    for (int i = 0; i< list.size();i++)
    {
        cout << list[i] << endl;
    }
    return 0;
}
