package connection;

import java.net.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Collector {

    private URL link; // this contain the address of the server
    private int TIMEOUT = 100;

    private static String defaultAddress;

    public Collector() {
        setAddress(defaultAddress);
    }

    public Collector(String linkAddress) {
        setAddress(linkAddress);
    }

    public static void setDefaultAddress(String defaultAddr){
        defaultAddress = defaultAddr;
    }

    public void setAddress(String linkAddress){
        try {
            setLink(new URL(linkAddress));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public URL getLink() {
        return link;
    }

    public void setLink(URL link) {
        this.link = link;
    }

    /*
        http://127.0.0.1:5000 -> is the root
        http://127.0.0.1:5000/lastorder -> is a branch and "/lastorder" is the name
     */
    public void setBranch(String branchName){
        setAddress(defaultAddress + branchName);
    }

    public String getDataFrom(String branchName){
        setBranch(branchName);
        return getDataFromServer();
    }

    public String getDataFromServer() {
        // This list will contains all the data from the response
        List<String> rawData = new ArrayList<String>();

        try {
            // Set Up the connection with the server
            URLConnection conn = this.link.openConnection();
            conn.setConnectTimeout(TIMEOUT);

            // Check the connection with the server
            try{
                conn.connect();
            } catch (Exception ex){
                System.out.println("Can't reach the server!");
                return "offline";
            }

            // Get the response
            BufferedReader response = new BufferedReader(
                    new InputStreamReader(
                            conn.getInputStream()));

            // Get the data from the response
            String inputLine;
            while ((inputLine = response.readLine()) != null) {
               // System.out.println(inputLine);
                rawData.add(inputLine);
            }
            response.close();

        } catch (Exception e) {
            e.printStackTrace();
        }

        if(rawData.isEmpty())
            return "None";
        // Transform the 'rawData' list to a single string and return it
        return String.join(System.lineSeparator(), rawData);
    }
}
