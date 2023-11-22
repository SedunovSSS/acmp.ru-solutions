#include <iostream>
using namespace std;

int main() {
    int k;
    cin >> k;
    int h = 0, w = 0;
    int pretty = INT_MAX;

    for (int i = 1; i <= k; i++) {
        for (int j = 1; j <= k; j++) {
            if (k >= i * j) {
                int p = abs(i - j) + (k - i * j);
                if (p <= pretty) {
                    h = i;
                    w = j;
                    pretty = p;
                }
            }
            else {
                break;
            }
        }
    }

    cout << min(h, w) << " " << max(h, w) << endl;

    return 0;
}