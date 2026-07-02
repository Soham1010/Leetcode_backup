public class bubble_sort {
    public static void main(String[] args) {
        // Write your code here
        int arr[] = {4, 1, 3, 9, 7};
        
        bubbleSort(arr);
        
        System.out.print(arr);
    }

    private static void bubbleSort(int[] arr) {
        // code here
        // int arr[] = [4, 1, 3, 9, 7];
        
        for (int i=0; i<arr.length-1; i++) {
            for (int j=i; j<arr.length; j++) {
                if (arr[j] < arr[i]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }
}