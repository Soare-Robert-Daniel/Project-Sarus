package connection;

import data.Order;
import data.Product;

import javax.json.Json;
import javax.json.JsonReader;
import javax.json.JsonObject;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.List;

public class OrderFromJSON {
    public static List<Order> convert(String data){
        // TO-DO
        return new ArrayList<Order>();
    }

    public static Order getOrder(String data){
        JsonReader reader = Json.createReader(new StringReader(data));
        JsonObject orderObj = reader.readObject();
        reader.close();

        return new Order(
                orderObj.getString("id"),
                orderObj.getString("date"),
                orderObj.getString("table_name"),
                Double.valueOf(orderObj.getString("total_value")),
                orderObj.getString("status")
        );
    }
}
