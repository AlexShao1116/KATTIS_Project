import java.util.*;

public class Main {

    public static int[] countSortInverse(int[] serialNumbers) {
        if (serialNumbers.length == 0) {
            return new int[0];
        }

        int n = serialNumbers.length;

        // find max
        int maxSerial = 0;
        for (int s : serialNumbers) {
            if (s > maxSerial) {
                maxSerial = s;
            }
        }

        // create frequency array
        int[] countArr = new int[maxSerial + 1];

        for (int serial : serialNumbers) {
            countArr[serial]++;
        }

        // compute suffix sums for descending order
        for (int i = maxSerial - 1; i >= 0; i--) {
            countArr[i] += countArr[i + 1];
        }

        // output array
        int[] sortedSerials = new int[n];

        // iterate in reverse to keep it stable
        for (int i = n - 1; i >= 0; i--) {
            int serial = serialNumbers[i];
            sortedSerials[countArr[serial] - 1] = serial;
            countArr[serial]--;
        }

        return sortedSerials;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int nbPiecesReceived = sc.nextInt();
        int[] serialNumbers = new int[nbPiecesReceived];

        for (int i = 0; i < nbPiecesReceived; i++) {
            serialNumbers[i] = sc.nextInt();
        }

        int[] sortedSerials = countSortInverse(serialNumbers);

        // print in one line with spaces
        for (int i = 0; i < sortedSerials.length; i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(sortedSerials[i]);
        }
        System.out.println();
    }
}