#include <iostream>
#include <vector>
using namespace std;

vector<int> count_sort_inverse(const vector<int>& serial_numbers) {
    int n = serial_numbers.size();
    if (n == 0) return {};

    // find max value
    int max_serial = 0;
    for (int s : serial_numbers) {
        if (s > max_serial) max_serial = s;
    }

    // create and initialize count array
    vector<int> countArr(max_serial + 1, 0);

    // count frequency
    for (int serial : serial_numbers) {
        countArr[serial]++;
    }

    // compute suffix sums for descending sort
    for (int i = max_serial - 1; i >= 0; i--) {
        countArr[i] += countArr[i + 1];
    }

    // output array
    vector<int> sorted_serials(n);

    // stable: iterate backwards
    for (int i = n - 1; i >= 0; i--) {
        int serial = serial_numbers[i];
        sorted_serials[countArr[serial] - 1] = serial;
        countArr[serial]--;
    }

    return sorted_serials;
}

int main() {
    int nb_pieces_received;
    cin >> nb_pieces_received;

    vector<int> serial_numbers(nb_pieces_received);
    for (int i = 0; i < nb_pieces_received; i++) {
        cin >> serial_numbers[i];
    }

    vector<int> sorted_serials = count_sort_inverse(serial_numbers);

    // print space-separated
    for (int i = 0; i < sorted_serials.size(); i++) {
        if (i > 0) cout << " ";
        cout << sorted_serials[i];
    }
    cout << endl;

    return 0;
}
