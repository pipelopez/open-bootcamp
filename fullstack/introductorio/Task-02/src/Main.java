public class Main {
    public static void main(String[] args) {

        int numeroIf = -3;

        if (numeroIf > 0 ) {
            System.out.println("El valor es positivo");
        } else if (numeroIf == 0 ) {
            System.out.println("El valor es cero");
        } else {
            System.out.println("El valor es negativo");
        }

        int numeroWhile = 0;

        while ( numeroWhile < 3) {
            System.out.println("Este es el valor de numeroWhile " + numeroWhile);
            numeroWhile++;
        }

        int numeroDoWhile = 0;

        do {
            System.out.println("Este es el valor de numeroDoWhile " + numeroDoWhile);
            numeroDoWhile++;
        } while (numeroDoWhile < 1);


        for ( int numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println("Este es el valor de numeroFor " + numeroFor);
        }

        String estacion = "VERANO";

        switch (estacion) {
            case "OTOÑO" :
                System.out.println("Es Otoño");
                break;
            case "INVIERNO" :
                System.out.println("Es Invierno");
                break;
            case "PRIMAVERA" :
                System.out.println("Es Primavera");
                break;
            case "VERANO" :
                System.out.println("Es Verano");
                break;
            default:
                System.out.println("El clima está raro");

        }

    }
}