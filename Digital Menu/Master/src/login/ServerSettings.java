package login;

import java.io.Serializable;
import java.util.prefs.Preferences;

public class ServerSettings implements Serializable {

    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }

    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }

    private String ip;
    private String port;
    private Preferences prefs;

    ServerSettings(){
        getSettings();
    }

    ServerSettings(String ip, String port){
        setIp(ip);
        setPort(port);
    }

    public void saveSettings(){
        prefs = Preferences.userRoot().node("HostSettings");
        prefs.put("ip", getIp());
        prefs.put("port", getPort());
    }

    public void getSettings(){
        prefs = Preferences.userRoot().node("HostSettings");
        setIp(prefs.get("ip", ""));
        setPort(prefs.get("port", ""));
    }

    public void clear(){
        setIp("");
        setPort("");
        saveSettings();
    }
}


