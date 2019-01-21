package home;

import bill.BillController;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;

public class HomeBuilder {
    protected int width;
    protected int height;
    protected boolean active;

    FXMLLoader loader;

    private void init() throws Exception
    {
        this.loader = new FXMLLoader(getClass().getResource("ListViewModel.fxml"));
        this.loader.load();
    }
    public HomeBuilder() throws Exception
    {
        height = 450;
        width = 880;
        active = true;
        init();
    }

    public HomeBuilder(int width, int height) throws Exception
    {
        this.height = height;
        this.width = width;
        this.active = true;
        init();
    }

    public HomeBuilder(int width, int height, boolean active) throws Exception
    {
        this.height = height;
        this.width = width;
        this.active = active;
        init();
    }

    public Scene buildScene() throws Exception
    {
        Parent root = this.loader.getRoot();

        return new Scene(root, width, height);
    }

    public HomeController getController() throws Exception
    {
        // this.loader.load(getClass().getResource("Login.fxml"));
        return (HomeController) this.loader.getController();
    }
}
