package ie.dealz.app.Adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.LinkedList;
import java.util.List;

import ie.dealz.app.Facade.ListItem;
import ie.dealz.app.models.Golf;
import ie.dealz.app.R;


/**
 * Created by davidoregan on 11/04/2014.
 */


public class CarAdapter extends BaseAdapter {

    //Make generic, list item interface

    LinkedList<ListItem> cars = new LinkedList<ListItem>();

    Context context;

    public CarAdapter(Context context) {
        super();
        this.context = context;
    }

    public void add(Golf object) {
        cars.add(object);

    }

    public List<ListItem> findByColor(String color){
        List<ListItem> items = new LinkedList<ListItem>();
        for(ListItem car : cars){
            if(car.getColour().equalsIgnoreCase(color))
                items.add(car);
        }
        return items;
    }

    public List<ListItem> findByLocation(String location){
        List<ListItem> items = new LinkedList<ListItem>();
        for(ListItem car : cars){
            if(car.getLocation().equalsIgnoreCase(location))
                items.add(car);
        }
        return items;
    }

    public List<ListItem> findByPrice(String price){
        List<ListItem> items = new LinkedList<ListItem>();
        for(ListItem car : cars){
            if(car.getPrice().equalsIgnoreCase(price))
                items.add(car);
        }
        return items;
    }

    @Override
    public int getCount() {
        return cars.size();
    }

    @Override
    public Object getItem(int position) {
        return cars.get(position);
    }

    @Override
    public long getItemId(int position) {
        return 0;
    }


    @Override
    public View getView(int position, View convertView, ViewGroup parent) {



        View view = convertView;

        if (view == null) {
            LayoutInflater inflater = (LayoutInflater) context
                    .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            view = inflater.inflate(R.layout.list_item, null);
        }


        assert view != null;


        String titleText = cars.get(position).getTitle();

        if (titleText != null) {
            TextView title = (TextView) view.findViewById(R.id.carTitle);
            title.setText(titleText);
        }

        TextView PP = (TextView) view.findViewById(R.id.carPP);
        PP.setText(cars.get(position).getPrice());

        TextView Location = (TextView) view.findViewById(R.id.carLocation);
        Location.setText(cars.get(position).getLocation());

        TextView Colour = (TextView) view.findViewById(R.id.carColour);
        Colour.setText(cars.get(position).getColour());


        return view;

    }
}

