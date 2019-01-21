package data;

public class Product {

    private String name;
    private int quantity;
    private double price;

    public Product(){

    }

    public Product(String name, int quantity, double price){
       setName(name);
       setPrice(price);
       setQuantity(quantity);
    }

    public String toString(){
        return String.format("Name : %s, Quantity: %d, Price: %.2f", getName(), getQuantity(), getPrice());
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}
