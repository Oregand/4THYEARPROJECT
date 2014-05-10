package ie.dealz.app.models;

import ie.dealz.app.Facade.ListItem;

/**
 * Created by davidoregan on 09/04/2014.
 */
public class Golf implements ListItem{
    public long id;
    public String title;
    public String link;
    public String predictedPrice;
    public String location;
    public String Colour;



    public long getId() {
        return id;
    }

    @Override
    public String getTitle() {
        return title;
    }

    @Override
    public String getPrice() {
        return String.format("%.2f", predictedPrice);
    }

    @Override
    public String getLink() {
        return link;
    }

    @Override
    public String getLocation() {
        return location;
    }

    @Override
    public String getColour() {
        return Colour;
    }

}


