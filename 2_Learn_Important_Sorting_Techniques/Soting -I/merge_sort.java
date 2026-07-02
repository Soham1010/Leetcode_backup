import java.util.Arrays;

public class merge_sort {
    public static void main(String[] args) {
        int[] arr1 = {1, 3};
        int[] arr2 = {2, 4};

        int[] merged = new int[arr1.length + arr2.length];
        int index = 0;

        for (int value : arr1) {
            merged[index++] = value;
        }

        for (int value : arr2) {
            merged[index++] = value;
        }

        System.out.println(Arrays.toString(merged));
    }
}
