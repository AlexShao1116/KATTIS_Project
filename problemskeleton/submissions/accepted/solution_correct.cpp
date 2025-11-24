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

    // get freq of each element
    for (int serial : serial_numbers) {
        countArr[serial]++;
    }

    //(special part for this question) compute sum backwards
    // freqArr[x] = nb of elements >= x
    for (int i = max_serial - 1; i >= 0; i--) {
        countArr[i] += countArr[i + 1];
    }

    // build sorted array
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

    vector<int> list_serial_nb(nb_pieces_received);
    for (int i = 0; i < nb_pieces_received; i++) {
        cin >> list_serial_nb[i];
    }

    vector<int> sorted_serial_nb_pieces = count_sort_inverse(list_serial_nb);

    // print space-separated
    for (int i = 0; i < sorted_serial_nb_pieces.size(); i++) {
        if (i > 0) cout << " ";
        cout << sorted_serial_nb_pieces[i];
    }
    cout << endl;

    return 0;
}
