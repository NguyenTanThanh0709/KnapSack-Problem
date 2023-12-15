import java.util.Scanner;
import java.util.Random;
public class Main {
    public static void main(String[] args) {
        // Example data for the Knapsack problems
        int[] weights1 = {382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684};
        int[] values1 = {825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257, 369261};
        int capacity1 = 6404180;

        int[] weights2 = {70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120};
        int[] values2 = {135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240};
        int capacity2 = 750;

        int[] weights3 = {25, 35, 45, 5, 25, 3, 2, 2};
        int[] values3 = {350, 400, 450, 20, 70, 8, 5, 5};
        int capacity3 = 104;

        int[] weights4 = {41, 50, 49, 59, 55, 57, 60};
        int[] values4 = {442, 525, 511, 593, 546, 564, 617};
        int capacity4 = 170;

        int[] weights5 = {12, 7, 11, 8, 9};
        int[] values5 = {24, 13, 23, 15, 16};
        int capacity5 = 26;


        function("Data 1", weights1, values1, capacity1);
        function("Data 2", weights2, values2, capacity2);
        function("Data 3", weights3, values3, capacity3);
        function("Data 4", weights4, values4, capacity4);
        function("Data 5", weights5, values5, capacity5);

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of items: ");
        int numberOfItems = scanner.nextInt();

        System.out.println("Enter the maximum weight for each item: ");
        int maxWeight = scanner.nextInt();

        System.out.println("Enter the maximum value for each item: ");
        int maxValue = scanner.nextInt();

        System.out.println("Enter the maximum capacity of the knapsack: ");
        int maxCapacity = scanner.nextInt();

        int[] weight6 = generateRandomArray(numberOfItems, 1, maxWeight);
        int[] value6 = generateRandomArray(numberOfItems, 1, maxValue);
        int capacit6 = generateRandomValue(1, maxCapacity);

        System.out.println("Generated Data:");
        printArray("Weights", weight6);
        printArray("Values", value6);
        System.out.println("Capacity: " + capacit6);
        function("Data Random", weight6, value6, capacit6);

    }

    /**
     * Generates a random integer array of the specified size with values between minValue and maxValue (inclusive).
     *
     * @param size      The size of the array to generate.
     * @param minValue  The minimum value for each element in the array.
     * @param maxValue  The maximum value for each element in the array.
     * @return          The generated random integer array.
     */
    private static int[] generateRandomArray(int size, int minValue, int maxValue) {
        Random random = new Random();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(maxValue - minValue + 1) + minValue;
        }
        return array;
    }

    /**
     * Generates a random integer value between minValue and maxValue (inclusive).
     *
     * @param minValue  The minimum value for the random integer.
     * @param maxValue  The maximum value for the random integer.
     * @return          The generated random integer value.
     */
    private static int generateRandomValue(int minValue, int maxValue) {
        Random random = new Random();
        return random.nextInt(maxValue - minValue + 1) + minValue;
    }

    /**
     * Prints the elements of an integer array along with a specified name.
     *
     * @param name  The name to display before printing the array.
     * @param array The integer array to print.
     */
    private static void printArray(String name, int[] array) {
        System.out.print(name + ": ");
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }


    private static void function(String dataName,int[] weights, int[] values, int capacity){
        System.out.println(dataName);
        measureRunningTime("Brute Force Knapsack", () -> {
            int[] result = BruteForceKnapsack.bruteForceKnapsack(weights, values, capacity);
            printResult(result, weights.length, result[weights.length], result[weights.length+1]);
        });

        measureRunningTime("Fractional Knapsack Greedy", () -> {
            Tuple<double[], Double, Double> result = FractionalKnapsackGreedy.fractionalKnapsack(values, weights, capacity);
            printResultFractional(result.selectedObject, weights.length, result.bestValue, result.bestWeight);
        });

        measureRunningTime("0/1 Knapsack Dynamic Programming", () -> {
            Tuple<int[], Integer, Integer> result = KnapsackDynamic.knapsackDynamic(values, weights, capacity);
            printResult(result.selectedObject, weights.length, result.bestValue, result.bestWeight);
        });
        System.out.println("\n ======================================= \n");
    }

    private static void measureRunningTime(String algorithmName, Runnable algorithm) {
        System.out.println( algorithmName);

        long startTime = System.nanoTime();
        algorithm.run();
        long endTime = System.nanoTime();
        long runningTime = endTime - startTime;

        System.out.println("\nActual Running Time: " + runningTime + " ns \n");
    }

    private static void printResult(int[] selectItem, int n, int values, int weight){
        System.out.println("Best Values: " + values);
        System.out.println("Best weight: " + weight);
        for (int i = 0; i < n; i++){
            System.out.print(selectItem[i] + " - ");
        }
    }

    private static void printResultFractional(double[] selectItem, int n, double values  , double weight){
        System.out.println("Best Values: " + values);
        System.out.println("Best weight: " + weight);
        for (int i = 0; i < n; i++){
            System.out.print(selectItem[i] + " - ");
        }
    }

}



