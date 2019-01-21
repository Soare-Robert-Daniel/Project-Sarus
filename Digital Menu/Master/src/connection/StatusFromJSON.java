package connection;

import data.Order;

import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonReader;
import java.io.StringReader;

public class StatusFromJSON {
    public static boolean getStatusConnection(String data){
        JsonReader reader = Json.createReader(new StringReader(data));
        System.out.println(data);
        JsonObject statusObj = reader.readObject();
        reader.close();

        if(statusObj.getString("valid").equals("Yes")){
            return true;
        }
        else{
            System.out.println(statusObj.getString("log"));
            return false;
        }
    }
}
