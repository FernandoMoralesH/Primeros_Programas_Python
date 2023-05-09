public class Main {
    public static void main(String[] args) {
        // Imprimimos los mensajes de bienvenida al juego
        String mensaje_juego = "La lotería local del pueblo del Espinal, Oaxaca: Presenta: ".center(80);
        String mensaje2 = "Juego de la Lotería".center(80);
        System.out.println("\n" + mensaje_juego + "\n" + mensaje2 + "\n");

        // Imprimimos las instrucciones del menú
        String instrucciones_menu = "A. Menú con las opciones: \n 1.-Comprar boleto / imprimir boleto \n 2.-Generar número ganador/ con un método(generar números aleatorios) \n 3.-Verificar si gano el boleto comprado \n 4.-Mostrar resultado (si el boleto fue premiado y con cuanto) \n 5.-Salir";
        System.out.println(instrucciones_menu.indent(15, '-'));

        // Imprimimos la tabla de premios en la consola
        System.out.println("+---------------------------------+----------------------+-----------------+");
        System.out.println("|Números de digitos acertados     |Monto del Premio en % |Premio en $      |");
        System.out.println("+---------------------------------+----------------------+-----------------+");

        List<Map<String, Object>> lugares = new ArrayList<>();
        lugares.add(Map.of("Numeros de digitos acertados", 6, "Monto del Premio", 100.0, "Premio base", 30000.0));
        lugares.add(Map.of("Numeros de digitos acertados", 5, "Monto del Premio", 0.050, "Premio base", 1500.0));
        lugares.add(Map.of("Numeros de digitos acertados", 4, "Monto del Premio", 0.025, "Premio base", 750.0));
        lugares.add(Map.of("Numeros de digitos acertados", 3, "Monto del Premio", 0.010, "Premio base", 300.0));
        lugares.add(Map.of("Numeros de digitos acertados", 2, "Monto del Premio", 0.0089, "Premio base", 267.0));
        lugares.add(Map.of("Numeros de digitos acertados", 1, "Monto del Premio", 0.00033, "Premio base", 10.0));

        for (Map<String, Object> dato : lugares) {
            int numeros = (int) dato.get("Numeros de digitos acertados");
            double monto = (double) dato.get("Monto del Premio");
            double premio = (double) dato.get("Premio base");

            String cadena = String.format("|%33d|%22.3f|%17.2f|", numeros, monto, premio);
            System.out.println(cadena);
        }

        System.out.println("+---------------------------------+----------------------+-----------------+");
    }
}
