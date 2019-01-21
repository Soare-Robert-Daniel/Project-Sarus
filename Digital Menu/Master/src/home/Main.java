package home;

import connection.Collector;
import connection.OrderFromJSON;
import connection.ProductsFromJSON;
import data.Order;
import data.Product;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.util.List;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
       // TestProductsList();
       // Parent root = FXMLLoader.load(getClass().getResource("ListViewModel.fxml"));
        Parent root = FXMLLoader.load(getClass().getResource("/login/LoginView.fxml"));
        primaryStage.setTitle("Master");
        primaryStage.setResizable(false);
        primaryStage.setScene(new Scene(root, 600, 400));
        primaryStage.show();
    }

    private void TestProductsList(){
        Collector test = new Collector("http://127.0.0.1:5000/getOrder");
        List<Product> productList =  ProductsFromJSON.convert(test.getDataFromServer());

        for(Product p : productList){
            System.out.println(p.toString());
        }
    }

    private void TestLastOrder(){
        Collector test = new Collector("http://127.0.0.1:5000/lastrecord");
        if(test.getDataFromServer().equals("None"))
            return;
        Order order = OrderFromJSON.getOrder(test.getDataFromServer());
        System.out.println(order.toString());
    }

    public static void main(String[] args) {
        launch(args);
    }
}
