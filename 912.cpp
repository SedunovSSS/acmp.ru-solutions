#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> colors(n);
    for (int i = 0; i < n; i++) {
        cin >> colors[i];
    }

    int a = *max_element(colors.begin(), colors.end(), [&colors](int i, int j) {
        return count(colors.begin(), colors.end(), i) < count(colors.begin(), colors.end(), j);
        });

    int m = count(colors.begin(), colors.end(), a);

    unordered_set<int> xz;
    for (int i : colors) {
        if (count(colors.begin(), colors.end(), i) == m) {
            xz.insert(i);
        }
    }

    if (xz.size() > 1) {
        cout << 0 << endl;
    }
    else {
        cout << a << endl;
    }

    return 0;
}