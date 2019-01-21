package bill;

import connection.Collector;
import connection.ProductsFromJSON;
import data.Product;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;

public class BillController implements Initializable {

    private final ObservableList<Product> productObsList = FXCollections.observableArrayList();

    private String id;

    @FXML
    private TableView table;
    @FXML
    private Label tableNameLabel;
    @FXML
    private TableColumn productCol;
    @FXML
    private TableColumn quantCol;
    @FXML
    private TableColumn priceCol;
    @FXML
    private Button acceptButton;
    @FXML
    private Button cancelButton;
    @FXML
    private TextArea requestTextField;

    @Override
    public void initialize(URL location, ResourceBundle resource){
        // Set the item's scheme to the table
        productCol.setCellValueFactory(new PropertyValueFactory<Product, String>("name"));
        quantCol.setCellValueFactory(new PropertyValueFactory<Product, Integer>("quantity"));
        priceCol.setCellValueFactory(new PropertyValueFactory<Product, Double>("price"));

        // Set the actions for accept and cancel button
        acceptButton.setOnMouseClicked((event) -> {
            sendOrderStatus("accepted");
            // Close the window
            Stage stage = (Stage) acceptButton.getScene().getWindow();
            stage.close();
        });

        cancelButton.setOnMouseClicked((event) -> {
            sendOrderStatus("canceled");

            // Close the window
            Stage stage = (Stage) cancelButton.getScene().getWindow();
            stage.close();
        });
    }

    // Set data to the window
    public void setData(String id, String tableName, Double totalValue){
        this.id = id;
        tableNameLabel.setText("Table " + tableName);
        updateTable();
    }

    private void updateTable(){
        // Get the order's items from server
        Collector collector = new Collector();
        String data = collector.getDataFrom(String.format("/table/%s/getOrder", this.id));

        // Check if the data is valid
        if(data.contains("None")){
            return;
        }

        // Extract and add to table
        this.productObsList.addAll(ProductsFromJSON.convert(data));
        this.table.setItems(this.productObsList);
    }

    // Send the order's status to the server fo
    private void sendOrderStatus(String status){
        try {

            //this.collector.setAddress("http://127.0.0.1:5000/status/" + status + '/' + this.id);
            Collector collector = new Collector();
            String data = collector.getDataFrom(String.format("/status/%s/%s", status, this.id ));
            if(data.equals("None"))
                System.out.println("No answer on " + this.id + " for action: " + status);
            else{
                System.out.println(data);
            }
        }catch (Exception ex){
            ex.printStackTrace();
        }
    }
}
