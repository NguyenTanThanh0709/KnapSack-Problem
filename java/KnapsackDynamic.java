public class KnapsackDynamic {

    /**
     * A helper method to return the maximum of two integers.
     * @param i First integer.
     * @param w Second integer.
     * @return The maximum of the two integers.
     */
    public static int maxValue(int i, int w) {
        if (i >= w) return i;
        return w;
    }

    /**
     * Solve the knapsack problem using the Dynamic  approach.
     *
     * @param weights Array of weights of the items.
     * @param values Array of values corresponding to the items.
     * @param capacity Capacity of the knapsack.
     * @return Tuple<int[], Integer> contains the list of selected items and the best value that can be obtained
     */
    public static Tuple<int[], Integer, Integer> knapsackDynamic(int[] values, int[] weights, int capacity) {
        int n = values.length;

        // Create a 2D table to store temporary results of subproblems
        int[][] table = new int[n + 1][capacity + 1];

        // Fill in the DP table
        // each item from 1 to n
        for (int i = 1; i <= n; i++) {
            //  each capacity from 0 to the total capacity
            for (int w = 0; w <= capacity; w++) {
                //Check if the weight of the current item is within the current capacity
                if (weights[i - 1] <= w) {
                    // Update the optimal value in table[i][w] with the maximum of:
                    // 1. Sum of the value of the current item and the optimal value when considering the reduced capacity
                    //    (values[i - 1] + table[i - 1][w - weights[i - 1]])
                    // 2. Optimal value when not choosing the current item (table[i - 1][w])
                    table[i][w] = maxValue(values[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w]);
                } else {
                    // If the weight of the current item exceeds the current capacity, use the optimal value without choosing this item
                    table[i][w] = table[i - 1][w];
                }
            }
        }


        //Create an array of selectedQuantities to store selections (1 is selected, 0 is not selected).
        int[] selectedQuantities = new int[n];
        int i = n, c = capacity;
        int bestweight = 0;
        //Start from the optimal result in table[n][capacity] and move backwards to determine the optimal choice.
        //Repeat the process until all items are considered or the remaining capacity is 0.
        while (i > 0 && c > 0) {
//            If the value at table[i][c] is different from the value when the item is not selected (table[i - 1][c]),
//             mark the ith item as selected and reduce the remaining space.
            if (table[i][c] != table[i - 1][c]) {
                selectedQuantities[i - 1] = 1;
                c -= weights[i - 1];
                bestweight += weights[i - 1];
            }

            i--;
        }

        // Return the array of selected quantities and the optimal value
        return new Tuple<>(selectedQuantities, table[n][capacity], bestweight);
    }


}
