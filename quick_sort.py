/**
 * Created by swagatb on 5/7/17.
 */
import java.util.*;
import java.lang.*;
public class H46 {

    static void swap(int[] ar, int a , int b)
    {
        int t = ar[a];
        ar[a] = ar[b];
        ar[b] = t;
    }
    static int partition(int[] ar, int low, int high)
    {
        int i=low;
        int j=high;
        int pivot = ar[i];
        // terminating condition
        while(i<j)
        {
            // the 2nd condition is needed so that it does not go out of bounds
            while(i<=high && ar[i] <= pivot)
                i++;
            while(j>= low && ar[j] > pivot)
                j--;

            // if the pointers are stuck
            // 5 7 2 3 8 1
            // pointers will be stuck at (7) and (1)
            // so we swap and then move ahead
            if(i<=j)
            {
                swap(ar, i, j);
                i++;
                j--;
            }
        }

        swap(ar, low, j);
        return j;

    }
    static void qSort(int[] ar, int low, int high)
    {
        if (high <= low)
            return;
        int k = partition(ar, low, high);
        qSort(ar, low, k - 1);
        qSort(ar, k + 1, high);
    }
    static void quickSort(int[] ar) {
        qSort(ar, 0, ar.length-1);

    }

    static void printArray(int[] ar) {
        for(int n: ar){
            System.out.print(n+" ");
        }
        System.out.println("");
    }

    public static void main(String[] args)
    {
        int[] ar = {5, 8, 1, 3, 7, 9, 2};
        quickSort(ar);
        printArray(ar);
    }
}
