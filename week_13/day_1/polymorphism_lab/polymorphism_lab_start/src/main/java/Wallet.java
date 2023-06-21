import java.util.ArrayList;

public class Wallet {
    private String name;
    private ArrayList<IScan> walletItems;;

    public Wallet(String name) {
        this.name = name;
        this.walletItems = new ArrayList<IScan>();
    }

    public String getName() {
        return name;
    }

    public int getNumberOfItems() {
        return this.walletItems.size();
    }

    public void addItem(IScan item) {
        this.walletItems.add(item);
    }
}
