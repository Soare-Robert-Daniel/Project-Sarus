package connection;


import data.Product;

import javax.json.*;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.List;

public class ProductsFromJSON {

    public static List<Product> convert(String data){

        System.out.println(data);
        List<Product> products = new ArrayList<Product>();

        JsonReader reader = Json.createReader(new StringReader(data));
        JsonObject productsObj = reader.readObject();
        reader.close();

        JsonArray productsArray = productsObj.getJsonArray("products");
        for (JsonValue productValue : productsArray) {
            products.add(getProduct(productValue.toString()));
        }

        return products;
    }

    public static Product getProduct(String data){
        JsonReader reader = Json.createReader(new StringReader(data));
        JsonObject productObj = reader.readObject();
        reader.close();

        return new Product(productObj.getString("name"), 1, Double.parseDouble(productObj.getString("value")));
    }
}
/*
String personJSONData =
            "  {" +
            "   \"name\": \"Jack\", " +
            "   \"age\" : 13, " +
            "   \"isMarried\" : false, " +
            "   \"address\": { " +
            "     \"street\": \"#1234, Main Street\", " +
            "     \"zipCode\": \"123456\" " +
            "   }, " +
            "   \"phoneNumbers\": [\"011-111-1111\", \"11-111-1111\"] " +
            " }";

        JsonReader reader = Json.createReader(new StringReader(personJSONData));

        JsonObject personObject = reader.readObject();

        reader.close();

        System.out.println("Name   : " + personObject.getString("name"));
        System.out.println("Age    : " + personObject.getInt("age"));
        System.out.println("Married: " + personObject.getBoolean("isMarried"));

        JsonObject addressObject = personObject.getJsonObject("address");
        System.out.println("Address: ");
        System.out.println(addressObject.getString("street"));
        System.out.println(addressObject.getString("zipCode"));

        System.out.println("Phone  : ");
         JsonArray phoneNumbersArray = personObject.getJsonArray("phoneNumbers");
        for (JsonValue jsonValue : phoneNumbersArray) {
            System.out.println(jsonValue.toString());
        }
 */
