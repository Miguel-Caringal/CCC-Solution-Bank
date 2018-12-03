#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <sstream>
#include <iterator>
#include <string>
using namespace std;


int main() {
    map<string,string>mymap;
    int len;
    string temp;
    vector <string> list;
    cin >> len;
    for (int i = 0; i <= len;i++)
    {
        getline(cin, temp);
        std::istringstream stream(temp);
        string token1;
        string token2;
        stream >> token1 >> token2;
        mymap [token1] = token2;
    }
    for (int i = 0; i<= len-1;i++)
    {
        cin >>temp;
        if (mymap.find(temp) == mymap.end())
        {
            cout << "Not found" << endl;
        }
        else
        {
          cout << temp << "=" << mymap[temp] << endl;
        }
    }

    return 0;
}

