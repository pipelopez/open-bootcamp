public class Main {
    public static void main(String[] args) {
        Persona persona = new Persona();

        persona.setEdad(18);
        persona.setNombre("Luna Lunera");
        persona.setTelefono("2345678");

        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Edad: " + persona.getEdad());
        System.out.println("Teléfono: " + persona.getTelefono());
    }
}