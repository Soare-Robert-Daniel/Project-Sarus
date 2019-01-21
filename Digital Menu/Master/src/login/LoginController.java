package login;

import connection.Collector;
import home.HomeBuilder;
import home.HomeController;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.*;
import java.net.URL;
import java.util.ResourceBundle;

public class LoginController implements Initializable {
    @FXML
    private TextField ipTextField;
    @FXML
    private TextField portTextField;
    @FXML
    private Button connectButton;
    @FXML
    private CheckBox rememberCheck;

    private Stage stage;

    @Override
    public void initialize(URL location, ResourceBundle resource) {
        connectButton.setOnAction( event -> login());

        // Set the config server option
        ServerSettings serverSettings = new ServerSettings();
        ipTextField.setText(serverSettings.getIp());
        portTextField.setText(serverSettings.getPort());

        // if there are no past server config / login option set the checker on false
        if(!ipTextField.getText().isEmpty() && !portTextField.getText().isEmpty()){
            rememberCheck.setSelected(true);
        }

        rememberCheck.setOnAction( event -> remember());
    }

    private void login(){
        if(validation()){
            buildDefaultHostAddress();
            enterHomeWindow();

            // Close the window
            Stage stage = (Stage) connectButton.getScene().getWindow();
            stage.close();
        }
    }

    // Create e new Home window
    private void enterHomeWindow(){
        stage = new Stage();
        try {
            // Create the window
            HomeBuilder builder = new HomeBuilder(800, 600);
            HomeController controller = builder.getController();

            // Window Options
            stage.setTitle("Home");
            stage.setScene(builder.buildScene());
            stage.setResizable(false);
            stage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private boolean validation(){
        // TO-DO
        return true;
    }

    // Default are the setting that you set on Config Server / Login window
    private void buildDefaultHostAddress(){
        // http://127.0.0.1:5000/
        String defHostAddr = String.format("http://%s:%s", ipTextField.getText(), portTextField.getText());
        Collector.setDefaultAddress(defHostAddr);
        System.out.println(defHostAddr);
    }

    // Save the server config option or delete them
    private void remember(){
        ServerSettings newServerSettings = new ServerSettings(ipTextField.getText(), portTextField.getText());
        if(rememberCheck.isSelected()){
            newServerSettings.saveSettings();
        }
        else{
            newServerSettings.clear();
        }
    }

}
