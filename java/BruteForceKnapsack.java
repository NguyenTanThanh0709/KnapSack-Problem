public class BruteForceKnapsack {

    /**
     * Solve the 0/1 KnapSack problem using the Brute-Force approach.
     *
     * @param weights Array of weights of the items.
     * @param values Array of values corresponding to the items.
     * @param capacity Capacity of the knapsack.
     * @return Array containing the decision to choose or not choose each item, total value, and total weight.
     */
    public static int[] bruteForceKnapsack(int[] weights, int[] values, int capacity) {
        int n = weights.length; // Number of items in the list

        int[] bestChoice = new int[n]; // Array to store the decision to choose or not choose each item.
        int bestValue = 0; // Best total value found.
        int bestWeight = 0; // Best total weight found.
        int[] tempChoice = new int[n];

        // Iterate through all possible combinations of items, represented by binary numbers from 0 to 2^n - 1.
        for (int i = 0; i < Math.pow(2, n); i++) {
            int j = n - 1; // Variable j to track the position of the item in the bestChoice array.

            int tempWeight = 0; // Temporary weight of each combination.
            int tempValue = 0; // Temporary value of each combination.
            // Create a loop to generate different combinations by changing the values 0 and 1 in the bestChoice array.
            while (j >= 0) {
                // If the value at position j is not 0 (meaning the item is chosen),
                // set the value of bestChoice[j] to 0 (meaning not choosing the item)
                // and decrease the value of j by 1 (move to the previous item).
                if (bestChoice[j] != 0) {
                    bestChoice[j] = 0;
                    j--;
                } else {
                    // If bestChoice[j] is 0,
                    // set the value of bestChoice[j] to 1 (meaning choosing the item) and break out of the loop.
                    // Exiting this loop is important as it ensures that we only change the value at position j,
                    // without affecting positions before that.
                    bestChoice[j] = 1;
                    break;
                }
            }

            // Iterate through each item and calculate the temporary weight and value of each combination.
            for (int k = 0; k < n; k++) {
                if (bestChoice[k] == 1) {
                    tempWeight += weights[k];
                    tempValue += values[k];
                }
            }

            // Check if the current combination improves the result.
            if (tempValue > bestValue && tempWeight <= capacity) {
                // Update the variables storing the best result.
                bestValue = tempValue;
                bestWeight = tempWeight;
                tempChoice = bestChoice.clone();
            }
        }

        // Return an array containing the decision to choose or not choose each item,
        // the total value, and the total weight.
        // Extend the array by 2 units to store the best total value and total weight.
        int[] result = new int[n + 2];
        System.arraycopy(tempChoice, 0, result, 0, n);
        result[n] = bestValue;
        result[n + 1] = bestWeight;
        return result;
    }
}
