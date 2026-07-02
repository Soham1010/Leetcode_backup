#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    // Pre-compute: Create hash array for 26 characters
    int hash[26] = {0};
    for (int i = 0; i < s.size(); i++) {
        hash[s[i] - 'a']++;
    }

    int q;  
    cin >> q;
    while (q--) {
        char c;
        cin >> c;
        // Fetch and print frequency
        cout << hash[c - 'a'] << endl;
    }
    return 0;
}