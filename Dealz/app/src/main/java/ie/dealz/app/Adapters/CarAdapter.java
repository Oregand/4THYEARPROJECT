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
import ie.dealz.app.models.Cars;
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


    public void add(Cars object) {
        cars.add(object);

    }

    //If I put a space after the word, the search bar does not work anymore.
    //Fix


    public boolean findByAnything(String anything) {
        List<ListItem> items = new LinkedList<ListItem>();
        for (ListItem car : cars) {
            String mil = car.getMileage();
            String year = car.getCarYear();
            String diff = car.getDifference();

            if (year.trim().equalsIgnoreCase(anything.trim())) {
                items.add(car);
            } else if ((mil.trim().equalsIgnoreCase(anything.trim()))) {
                items.add(car);
            }
          else if ((diff.trim().equalsIgnoreCase(anything.trim()))) {
                items.add(car);
            }
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

        String savings = "You Save: ";
        TextView PP = (TextView) view.findViewById(R.id.carDiff);
        PP.setText(savings + cars.get(position).getDifference());

        String age = "Years old: ";
        TextView Age = (TextView) view.findViewById(R.id.carAge);
        Age.setText(age + cars.get(position).getCarYear());

        String mil = "Mileage: ";
        TextView Mileage = (TextView) view.findViewById(R.id.carMileage);
        Mileage.setText(mil + cars.get(position).getMileage());


        return view;

    }
}

