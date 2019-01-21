package bill;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;

public class BillBuilder {
    protected int width;
    protected int height;
    protected boolean active;

    FXMLLoader loader;

    private void init() throws Exception
    {
        this.loader = new FXMLLoader(getClass().getResource("BillView.fxml"));
        this.loader.load();
    }
    public BillBuilder() throws Exception
    {
        height = 450;
        width = 880;
        active = true;
        init();
    }

    public BillBuilder(int width, int height) throws Exception
    {
        this.height = height;
        this.width = width;
        this.active = true;
        init();
    }

    public BillBuilder(int width, int height, boolean active) throws Exception
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

    public BillController getController() throws Exception
    {
        return (BillController) this.loader.getController();
    }
}
