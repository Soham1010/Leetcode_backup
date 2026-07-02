import java.util.Arrays;

public class insertion_sort {
    public static void main(String[] args) {
        int arr[] = {4, 1, 3, 9, 7};

        InsertionSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    private static void InsertionSort(int arr[]) {
        for (int i=1; i<arr.length; i++) {
            int temp = arr[i];
            int j = i-1;
            // Only the adjecent sawp, we go right to left
            while (j >= 0 && arr[j]>temp) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
    }
    

}
