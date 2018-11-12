//
//  main.cpp
//  dmoj5
//
//  Created by Miguel Caringal on 2018-11-11.
//  Copyright © 2018 Miguel Caringal. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, const char * argv[]) {
    double times, maxdist, x, y ,prevx, prevy, combo = 1, currentdist, xdist, ydist, maxcombo = 1;
    cin >> times;
    cin >> maxdist;
    for (int i = 0; i < times; i++)
    {
        cin >> x;
        cin >> y;
        if (i != 0)
        {
            xdist = (x-prevx)*(x-prevx);
            ydist = (y-prevy)*(y-prevy);
            currentdist = sqrt(xdist+ydist);
            //cout <<currentdist << endl;
            if (currentdist<=maxdist)
            {
                combo +=1;
            }
            else
            {
                if (maxcombo < combo)
                {
                    maxcombo = combo;
                }
                combo = 0;
            }
            prevx = x;
            prevy = y;
        }
        else
        {
            prevx = x;
            prevy = y;
        }
    }
    cout << maxcombo << endl;
    return 0;
}
