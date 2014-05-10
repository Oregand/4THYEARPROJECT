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

    //Enable filtering


    //Make generic, list item interface
    //Origional Values
    List<ListItem> cars = new LinkedList<ListItem>();
    List<ListItem> originalList;

    Context context;

    public CarAdapter(Context context) {
        super();
        this.context = context;
    }


    public void add(Golf object) {
        cars.add(object);

    }

    public Boolean findByColor(String color) {
        List<ListItem> items = new LinkedList<ListItem>();
        for (ListItem car : cars) {
            String carColor = car.getColour();
            if (carColor.trim().equalsIgnoreCase(color.trim()))
                items.add(car);
        }

        if (items.size() > 0) {

            originalList = cars;
            cars = items;

            this.notifyDataSetChanged();

            return true;
        } else {
            if (originalList != null) {
                if (originalList.size() > 0) {

                    cars = originalList;
                    this.notifyDataSetChanged();
                }
            }

            return false;
        }

    }

    public boolean findByAnything(String anything) {
        List<ListItem> items = new LinkedList<ListItem>();
        for (ListItem car : cars) {
            String carColour = car.getColour();
            String carLocation = car.getLocation();
            String carPrice = car.getPrice();

            if (carLocation.trim().equalsIgnoreCase(anything.trim())) {
                items.add(car);
            } else if ((carColour.trim().equalsIgnoreCase(anything.trim()))) {
                items.add(car);
            }
//          else if ((carPrice.trim().equalsIgnoreCase(anything.trim()))) {
//                items.add(car);
//            }
        }

        if (items.size() > 0) {

            originalList = cars;
            cars = items;

            this.notifyDataSetChanged();

            return true;
        } else {
            if (originalList != null) {
                if (originalList.size() > 0) {

                    cars = originalList;
                    this.notifyDataSetChanged();
                }
            }

            return false;
        }

    }
    public boolean findByPrice(String price) {
        List<ListItem> items = new LinkedList<ListItem>();
        for (ListItem car : cars) {
            String carPrice = car.getPrice();
            if (carPrice.trim().equalsIgnoreCase(price.trim()))
                items.add(car);
        }

        if (items.size() > 0) {

            originalList = cars;
            cars = items;

            this.notifyDataSetChanged();

            return true;
        } else {
            if (originalList != null) {
                if (originalList.size() > 0) {

                    cars = originalList;
                    this.notifyDataSetChanged();
                }
            }

            return false;
        }

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
        return position;
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

