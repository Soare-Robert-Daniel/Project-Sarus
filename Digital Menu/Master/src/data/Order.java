package data;

import bill.BillBuilder;
import bill.BillController;
import connection.Collector;
import javafx.beans.property.SimpleStringProperty;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

import java.io.IOException;

public class Order {

    private String id;
    private String table;
    private double value;
    private String status;
    private String date;
    private Button show;


    private Stage stage;

    public Order() {

    }

    public Order(String id, String date, String table, double value, String status) {
        setId(id);
        setTable(table);
        setStatus(status);
        setValue(value);
        setDate(date);
        this.stage = new Stage();
        show = new Button("Show");
        show.setOnMouseClicked(
                (event) -> {
                    try {
                        // Construct the bill window
                        BillBuilder builder = new BillBuilder(600, 626);
                        BillController controller = builder.getController();

                        // Make a server request to get the items
                        controller.setData(getId(), getTable(), getValue());

                        // Window settings
                        stage.setTitle("Bill");
                        stage.setScene(builder.buildScene());
                        stage.setResizable(false);
                        stage.show();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
        );
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTable() {
        return table;
    }

    public void setTable(String table) {
        this.table = table;
    }

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = value;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Button getShow() {
        return show;
    }

    public void setShow(Button show) {
        this.show = show;
    }

    public String toString(){
        return String.format("ID : %s, Date: %s, Table Name: %s, Total Value: %.2f, Status: %s \n", getId(), getDate(), getTable(), getValue(), getStatus());
    }
}
