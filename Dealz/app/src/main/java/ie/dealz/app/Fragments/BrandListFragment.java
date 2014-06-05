package ie.dealz.app.Fragments;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AbsListView;
import android.widget.AdapterView;
import android.widget.ListAdapter;
import android.widget.TextView;

import ie.dealz.app.Activites.ItemActivity;
import ie.dealz.app.Adapters.CarAdapter;
import ie.dealz.app.Facade.ListItem;
import ie.dealz.app.R;
import ie.dealz.app.Registration.UserFunctions;
import ie.dealz.app.models.Cars;

/**
 * A fragment representing a list of Items.
 * <p/>
 * Large screen devices (such as tablets) are supported by replacing the ListView
 * with a GridView.
 * <p/>
 * Activities containing this fragment MUST implement the {@link }
 * interface.
 */
public class BrandListFragment extends Fragment implements AbsListView.OnItemClickListener {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    private OnFragmentInteractionListener mListener;

    /**
     * The fragment's ListView/GridView.
     */
    private AbsListView mListView;

    /**
     * The Adapter which will be used to populate the ListView/GridView with
     * Views.
     */
    private CarAdapter mAdapter;

    // TODO: Rename and change types of parameters
    public static BrandListFragment newInstance(String param1, String param2) {
        BrandListFragment fragment = new BrandListFragment();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    /**
     * Mandatory empty constructor for the fragment manager to instantiate the
     * fragment (e.g. upon screen orientation changes).
     */
    public BrandListFragment() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }

        this.getArguments();

        // TODO: Change Adapter to display your content
        mAdapter = new CarAdapter(getActivity());
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_item, container, false);

        // Set the adapter
        mListView = (AbsListView) view.findViewById(android.R.id.list);
        ((AdapterView<ListAdapter>) mListView).setAdapter(mAdapter);

        // Set OnItemClickListener so we can be notified on item clicks
        mListView.setOnItemClickListener(this);

//        mAdapter.clear(item);


        Cars item = new Cars();
        item.title = "Volkswagen Golf";
        mAdapter.add(item);

        Cars item2 = new Cars();
        item2.title = "Audi A4";
        mAdapter.add(item2);
        mAdapter.notifyDataSetChanged();

        Cars item3 = new Cars();
        item3.title = "BMW 3 Series";
        mAdapter.add(item3);
        mAdapter.notifyDataSetChanged();

        Cars item4 = new Cars();
        item4.title = "BMW 5 Series";
        mAdapter.add(item4);
        mAdapter.notifyDataSetChanged();

        Cars item5 = new Cars();
        item5.title = "Ford Fiesta";
        mAdapter.add(item5);
        mAdapter.notifyDataSetChanged();

        Cars item6 = new Cars();
        item6.title = "Ford Focus";
        mAdapter.add(item6);
        mAdapter.notifyDataSetChanged();

        Cars item7 = new Cars();
        item7.title = "Ford Mondeo";
        mAdapter.add(item7);
        mAdapter.notifyDataSetChanged();

        Cars item8 = new Cars();
        item8.title = "Mercedes-Benz E-Class";
        mAdapter.add(item8);
        mAdapter.notifyDataSetChanged();

        Cars item9 = new Cars();
        item9.title = "Toyota Avensis";
        mAdapter.add(item9);
        mAdapter.notifyDataSetChanged();

        Cars item10 = new Cars();
        item10.title = "Toyota Corolla";
        mAdapter.add(item10);
        mAdapter.notifyDataSetChanged();

//        Cars item11 = new Cars();
//        item11.title = "Volkswagen Polo";
//        mAdapter.add(item11);
//        mAdapter.notifyDataSetChanged();


        return view;


    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        try {
            mListener = (OnFragmentInteractionListener) activity;
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mListener = null;
    }


    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        if (null != mListener) {
            // Notify the active callbacks interface (the activity, if the
            // fragment is attached to one) that an item has been selected.
            ListItem item = (ListItem) mAdapter.getItem(position);
            mListener.onFragmentInteraction(item.getTitle());

            Intent intent = new Intent(this.getActivity(), ItemActivity.class);
            Bundle arguments2 = new Bundle();

            arguments2.putString("title", item.getTitle());
            intent.putExtra("arguements", arguments2);

        }
    }


    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * */

     public interface OnFragmentInteractionListener {
        // TODO: Update argument type and name
        public void onFragmentInteraction(String id);
    }

}