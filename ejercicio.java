public class servicioBanquetesDonaCata {
    public static void  main (String[] args) {
        String nameCliente = "Fernando Morales";
        String namePlatillo1 = "Cohinita Pibil";
        String namePlatillo2 = "Tacos";
        String namePlatillo3 = "Quesadillas";

        float pricePlatillo1 = (float) 150.0;
        float pricePlatillo2 = (float) 130.0;
        float pricePlatillo3 = (float) 180.0;

        int countPlatillo1 =2;
        int countPlatillo2 =3;
        int countPlatillo3 =5;
        float iva = (float) 0.16;

        int countMeseros = 3;
        int invitados = 0;
        int priceServiceMesero = 0;
        float priceTotalWithIva = 0;
        float priceTotal = (float) 0;

        float priceTotalPlatillos = (pricePlatillo1*countPlatillo1)+(pricePlatillo2*countPlatillo2)+(pricePlatillo3*countPlatillo3);
        priceTotalWithIva = (priceTotalPlatillos * iva) + priceTotalPlatillos;
        priceServiceMesero = countMeseros*500;
        priceTotal = priceTotalWithIva+priceServiceMesero;

        System.out.println("**********************************************************************");
        System.out.println("El servicio de platillos del cliente: "+ nameCliente + " sera de: $" + priceTotalWithIva);
        System.out.println("El servicio de meseros tendra un costo total de: $" + priceServiceMesero);
        System.out.println("El costo total del servicio sera de: $" + priceTotal);
        System.out.println("***********************************************************************");
    }
}
