import java.util.*;

public class solution_correct {

    public static int[] countSortInverse(int[] serialNumbers) {
        if (serialNumbers.length == 0) {
            return new int[0];
        }

        int n = serialNumbers.length;

        // find-> max
        int maxSerial = 0;
        for (int s : serialNumbers) {
            if (s > maxSerial) {
                maxSerial = s;
            }
        }
        
        //freq of each
        int[] countArr = new int[maxSerial + 1];

        // get freq of each element
        for (int serial : serialNumbers) {
            countArr[serial]++;
        }

        //(special part for this question) compute sum backwards
        // freqArr[x] = nb of elements >= x
        for (int i = maxSerial - 1; i >= 0; i--) {
            countArr[i] += countArr[i + 1];
        }

        // build sorted array
        int[] sortedSerials = new int[n];

        // stable: iterate backwards
        for (int i = n - 1; i >= 0; i--) {
            int serial = serialNumbers[i];
            sortedSerials[countArr[serial] - 1] = serial;
            countArr[serial]--;
        }

        return sortedSerials;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int nb_pieces_received = sc.nextInt();
        int[] list_serial_nb = new int[nb_pieces_received];

        for (int i = 0; i < nb_pieces_received; i++) {
            list_serial_nb[i] = sc.nextInt();
        }

        int[] sorted_serial_nb_pieces = countSortInverse(list_serial_nb);

        // print in one line with spaces
        for (int i = 0; i < sorted_serial_nb_pieces.length; i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(sorted_serial_nb_pieces[i]);
        }
        System.out.println();
    }
}