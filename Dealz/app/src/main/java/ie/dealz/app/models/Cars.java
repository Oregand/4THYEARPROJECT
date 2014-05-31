package ie.dealz.app.models;

import ie.dealz.app.Facade.ListItem;

/**
 * Created by davidoregan on 09/04/2014.
 */
public class Cars implements ListItem{
    public long id;
    public String title;
    public String link;
    public String predictedPrice;
    public String askingPrice;
    public String difference;
    public String carYear;
    public String location;
    public String mileage;
    public String Colour;
    public String Owners;



    public long getId() {
        return id;
    }

    @Override
    public String getTitle() {
        return title;
    }

    @Override
    public String getpredictedPrice() {
        return  predictedPrice;
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

    @Override
    public String getAskingPrice() {
        return askingPrice;
    }

    @Override
    public String getDifference() {
        return difference;
    }

    @Override
    public String getCarYear() {
        return carYear;
    }

    @Override
    public String getMileage() {
        return mileage;
    }

    @Override
    public String getOwners() {
        return Owners;
    }

}


