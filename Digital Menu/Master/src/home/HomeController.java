package home;

import connection.Collector;
import connection.OrderFromJSON;
import data.Order;
import javafx.animation.Animation;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.stage.Stage;
import javafx.util.Duration;
import login.LoginBuilder;
import login.LoginController;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;
import java.util.stream.Collectors;

public class HomeController implements Initializable {

    private List<Order> orderList = new ArrayList<Order>();
    private List<Order> filteredOrderList = new ArrayList<Order>();
    private List<String> choiceListOptions = new ArrayList<String>();
    private final ObservableList<Order> ordersObsList = FXCollections.observableList(filteredOrderList);
    private final ObservableList<String> choiceObsList = FXCollections.observableArrayList();
    private Stage stage;

    @FXML
    private TableView<Order> table;
    @FXML
    private TableColumn idCol;
    @FXML
    private TableColumn dateCol;
    @FXML
    private TableColumn tableNameCol;
    @FXML
    private TableColumn valueCol;
    @FXML
    private TableColumn statusCol;
    @FXML
    private TableColumn optionsCol;
    @FXML
    private Label statusLabel;
    @FXML
    private Button connectServerButton;
    @FXML
    private ChoiceBox<String> tableFilter;

    @Override
    public void initialize(URL location, ResourceBundle resource) {
        // Set the item's scheme to the table
        idCol.setCellValueFactory(new PropertyValueFactory<Order, String>("id"));
        dateCol.setCellValueFactory(new PropertyValueFactory<Order, String>("date"));
        tableNameCol.setCellValueFactory(new PropertyValueFactory<Order, String>("table"));
        valueCol.setCellValueFactory(new PropertyValueFactory<Order, Double>("value"));
        statusCol.setCellValueFactory(new PropertyValueFactory<Order, String>("status"));
        optionsCol.setCellValueFactory(new PropertyValueFactory<Order, Button>("show"));

        // Add a timer to check if there are new orders
        Timeline timeline = new Timeline(new KeyFrame(
                Duration.millis(500),
                (e) -> AddLastOrder()));
        timeline.setCycleCount(Animation.INDEFINITE);
        timeline.play();

        // Set the default filter
        addChoiceOption("All");
        tableFilter.setValue("All");

        // Set the selection mode
        tableFilter.getSelectionModel().selectedItemProperty().addListener(
                (ObservableValue<? extends String> observable, String oldValue, String newValue) -> applyFilter()
        );

        // Set the acton for connect button
        connectServerButton.setOnAction(event -> connectToServer());
    }

    private void AddLastOrder() {

        // Get an order from server
        Collector collector = new Collector();
        String data = collector.getDataFrom("/lastrecord");

        // Set connection status to GUI
        if (data.equals("offline")) {
            setStatusServe("offline");
            return;
        } else {
            setStatusServe("online");
        }

        // No data
        if (data.equals("None")) {
            return;
        }

        // Extract the information from the server response
        Order newOrder = OrderFromJSON.getOrder(data);
        System.out.print(newOrder.toString());

        // Add the table name to filter GUI
        addChoiceOption(newOrder.getTable());

        // delete the outdated request (e.g: Pending request after they were evaluated
        orderList = orderList.stream()
                .filter(ord -> !ord.getId().equals(newOrder.getId()))
                .collect(Collectors.toCollection(ArrayList<Order>::new));

        // Add the new order to the list
        orderList.add(0, newOrder);

        // Apply the table filter to check the new order
        applyFilter();
    }

    // delete the outdated request (e.g: Pending request after they were evaluated
    private void checkUpdate(Order order) {
        for (Order ord : orderList) {
            if (ord.getId().equals(order.getId())) {
                ordersObsList.remove(ord);
            }
        }
    }

    // Add a new table name to the filter option
    private void addChoiceOption(String optionName) {
        if(!choiceObsList.contains(optionName)) {
            choiceObsList.add(optionName);
            tableFilter.setItems(choiceObsList);
        }
    }

    // Set items on the table based on their table's name
    private void applyFilter(){
        String filterName = tableFilter.getValue();
        System.out.println(filterName);

        // Filter the orders
        if(filterName.equals("All")){
            filteredOrderList = orderList;
        }
        else{
            filteredOrderList = orderList.stream()
                    .filter(ord -> ord.getTable().equals(filterName))
                    .collect(Collectors.toCollection(ArrayList<Order>::new));
        }

        // Set items to table
        ObservableList<Order> ordersObsList = FXCollections.observableList(filteredOrderList);
        table.setItems(ordersObsList);
        table.refresh();
    }

    private void connectToServer(){
        enterLoginWindow();
        // Close the window
        Stage stage = (Stage) connectServerButton.getScene().getWindow();
        stage.close();
    }

    // Create a new Server Config / Login window
    private void enterLoginWindow(){
        stage = new Stage();
        try {
            // Create the window
            LoginBuilder builder = new LoginBuilder(600, 400);
            LoginController controller = builder.getController();

            // Window Options
            stage.setTitle("Login");
            stage.setScene(builder.buildScene());
            stage.setResizable(false);
            stage.show();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void setStatusServe(String status) {
        if (status.equals("online")) {
            statusLabel.setText("Online");
            statusLabel.setTextFill(Color.GREEN);
        }
        if (status.equals("offline")) {
            statusLabel.setText("Offline");
            statusLabel.setTextFill(Color.RED);
        }
    }
}
