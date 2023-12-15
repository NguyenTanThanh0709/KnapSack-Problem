// This is a generic data type representing a Tuple with two variables, X and Y.
public class Tuple<X, Y, Z> {
    public final X selectedObject; // Used to store the list of selected objects.
    public final Y bestValue; // Used to store the best value that the algorithm brings.
    public final Z bestWeight; // Used to store the best value that the algorithm brings.

    // Constructor to initialize the Tuple with values for selectedObject and bestValue.
    public Tuple(X first, Y second, Z third) {
        this.selectedObject = first;
        this.bestValue = second;
        this.bestWeight = third;
    }
}
