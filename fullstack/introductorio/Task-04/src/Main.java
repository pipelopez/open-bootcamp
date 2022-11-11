public class Main {
    public static void main(String[] args) {

        Cliente cliente = new Cliente();
        cliente.setEdad(19);
        cliente.setNombre("Lupe Lupe");
        cliente.setTelefono("1234567");
        cliente.setCredito(1500.67);

        System.out.println("Cliente: " + cliente.getNombre());
        System.out.println("Edad: " +  cliente.getEdad());
        System.out.println("Teléfono: " +  cliente.getTelefono());
        System.out.println("Crédito: " +  cliente.getCredito());

        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(20);
        trabajador.setNombre("Lupe Luna");
        trabajador.setTelefono("1234569");
        trabajador.setSalario(1200.3);

        System.out.println("Trabajador: " + trabajador.getNombre());
        System.out.println("Edad: " +  trabajador.getEdad());
        System.out.println("Teléfono: " +  trabajador.getTelefono());
        System.out.println("Salario: " +  trabajador.getSalario());

    }
}