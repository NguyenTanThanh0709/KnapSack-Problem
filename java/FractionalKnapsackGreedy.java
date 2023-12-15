

public class FractionalKnapsackGreedy {

    /**
     * Solve the Fractional KnapSack problem using the Greedy  approach.
     *
     * @param weights Array of weights of the items.
     * @param values Array of values corresponding to the items.
     * @param capacity Capacity of the knapsack.
     * @return Tuple<double[], Double> contains the list of selected items and the best value that can be obtained
     */
    public static Tuple<double[], Double, Double> fractionalKnapsack(int[] values, int[] weights, int capacity) {

        int n = values.length;
        // Create an array of indices to represent the original order
// Create an array 'indices' to represent the initial order of items.
// Sort 'indices' based on the value-to-weight ratio using the merge sort algorithm.
// Greedily choose items based on the highest value-to-weight ratio.
// Calculate the total value and remaining capacity of the knapsack after each selection.
// Return the result as a Tuple object.

        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        // Sort indices based on the ratio of value to weight using merge sort
        mergeSort(indices, values, weights, 0, n - 1);


        double totalValue = 0;
        double totalWeght = 0;
        // List to store selected quantities in the original order
        double[] selectedQuantities = new double[n];

        // Greedily choose items based on the highest ratio
        for (int index : indices) {
            if (capacity == 0) {
                break;
            }
            if (weights[index] <= capacity) {
                // Take the whole item
                selectedQuantities[index] = 1;
                totalValue += values[index];
                totalWeght += weights[index];
                capacity -= weights[index];
            } else {
                // Take a fraction of the item
                selectedQuantities[index] = (double) capacity / weights[index];
                totalValue += selectedQuantities[index] * values[index];
                totalWeght += selectedQuantities[index] * weights[index];
                capacity = 0;
            }
        }

        // Return the result in the original order
        return new Tuple<>(selectedQuantities, totalValue, totalWeght);
    }


//    This is the mert sort algorithm with O(nlogn) complexity,
//    which has been learned in data structures and algorithms, so I won't repeat it again.
    public static void mergeSort(Integer[] indices, int[] values, int[] weights, int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;

            mergeSort(indices, values, weights, low, mid);
            mergeSort(indices, values, weights, mid + 1, high);

            merge(indices, values, weights, low, mid, high);
        }
    }
    public static void merge(Integer[] indices, int[] values, int[] weights, int low, int mid, int high) {
        int n1 = mid - low + 1;
        int n2 = high - mid;

        Integer[] left = new Integer[n1];
        Integer[] right = new Integer[n2];

        for (int i = 0; i < n1; ++i) {
            left[i] = indices[low + i];
        }
        for (int j = 0; j < n2; ++j) {
            right[j] = indices[mid + 1 + j];
        }

        int i = 0, j = 0;
        int k = low;

        while (i < n1 && j < n2) {
            if ((double) values[left[i]] / weights[left[i]] >= (double) values[right[j]] / weights[right[j]]) {
                indices[k] = left[i];
                i++;
            } else {
                indices[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            indices[k] = left[i];
            i++;
            k++;
        }

        while (j < n2) {
            indices[k] = right[j];
            j++;
            k++;
        }
    }
}
