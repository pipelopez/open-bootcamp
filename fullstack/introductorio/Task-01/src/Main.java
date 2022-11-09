public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        int resultSum = sum(1,2,3);
        System.out.println(resultSum);

        Coche miCoche = new Coche();
        miCoche.addDoors();
        System.out.println(miCoche.doors);
    }

    public static int sum(int a, int b, int c) {
            return a + b + c;
    }
}

class Coche {
    public int doors = 0;

    public void addDoors() {
        this.doors++;
    }
}

