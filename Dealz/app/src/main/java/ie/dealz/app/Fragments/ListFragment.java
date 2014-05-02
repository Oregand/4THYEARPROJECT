package ie.dealz.app.Fragments;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AbsListView;
import android.widget.AdapterView;
import android.widget.ListAdapter;
import android.widget.SearchView;
import android.widget.TextView;
import android.view.Menu;
import android.view.MenuInflater;
import android.widget.Toast;


import org.androidannotations.annotations.Background;

import java.util.Arrays;
import java.util.List;
import java.util.logging.Handler;

import ie.dealz.app.Adapters.CarAdapter;
import ie.dealz.app.Activites.ItemActivity;
import ie.dealz.app.Facade.ListItem;
import ie.dealz.app.R;
import ie.dealz.app.models.Golf;
import ie.dealz.app.services.GolfService;
import retrofit.RestAdapter;

/**
 * A fragment representing a list of Items.
 * <p/>
 * Large screen devices (such as tablets) are supported by replacing the ListView
 * with a GridView.
 * <p/>
 * Activities containing this fragment MUST implement the {@link Callbacks}
 * interface.
 */
public class ListFragment extends Fragment implements AbsListView.OnItemClickListener {

    private String grid_currentQuery = null; // holds the current query...
    private SearchView.OnQueryTextListener queryListener;

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    private OnFragmentInteractionListener mListener;
    CarAdapter arrayOfCars;
    private Callbacks mCallbacks = sDummyCallbacks;


    /**
     * A callback taskinterfaces that all activities containing this fragment must
     * implement. This mechanism allows activities to be notified of item
     * selections.
     */
    public interface Callbacks {
        /**
         * Callback for when an item has been selected.
         */
        public void onItemSelected(String id, int returningClass);
    }


    /**
     * A dummy implementation of the {@link Callbacks} taskinterfaces that does
     * nothing. Used only when this fragment is not attached to an activity.
     */
    private static Callbacks sDummyCallbacks = new Callbacks() {
        @Override
        public void onItemSelected(String id, int returningClass) {

        }
    };


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
    public static ListFragment newInstance(String param1, String param2) {
        ListFragment fragment = new ListFragment();
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
    public ListFragment() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }

        // TODO: Change Adapter to display your content
        mAdapter = new CarAdapter(getActivity());

        setHasOptionsMenu(true);


        queryListener = new SearchView.OnQueryTextListener() {

            @Override
            public boolean onQueryTextChange(String newText) {


                if (TextUtils.isEmpty(newText)) {
                    // mAdapter.getFilter().filter("");
                    getActivity().getActionBar().setSubtitle("List");
                    grid_currentQuery = null;
                } else {
                    getActivity().getActionBar().setSubtitle("List - Searching for: " + newText);
                    grid_currentQuery = newText;
                    // mAdapter.getFilter().filter(newText.toString());

                    mAdapter.findByColor(grid_currentQuery);
//                    List<ListItem> itemsLoc = mAdapter.findByLocation(grid_currentQuery);
//                    List<ListItem> itemsPrice = mAdapter.findByPrice(grid_currentQuery);

                }


                return true;
            }

            @Override
            public boolean onQueryTextSubmit(String query) {
                Toast.makeText(getActivity(), "Searching for: " + query + "...", Toast.LENGTH_SHORT).show();
                return false;
            }
        };
    }


    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        inflater.inflate(R.menu.main, menu);

        // Add SearchWidget.
        SearchView searchView = (SearchView) menu.findItem(R.id.grid_default_search).getActionView();
        searchView.setOnQueryTextListener(queryListener);

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

        apiTest();
        return view;
    }


    @Background
    void apiTest() {

        //When MAMP starts, I need to change the ip to my public IP in order to access the files.
        RestAdapter restAdapter = new RestAdapter.Builder().setServer("http://192.168.44.9:8888").build();

        //Create link to gold service
        GolfService service = restAdapter.create(GolfService.class);

        //Create our list of cars
        List<Golf> golfs = service.listGolfs();

        //Populate the list with cars
        for (Golf golf : golfs)
            mAdapter.add(golf);

        mAdapter.notifyDataSetChanged();
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


            ListItem item = (ListItem) mAdapter.getItem(position);
            Intent intent = new Intent(this.getActivity(), ItemActivity.class);

            Bundle arguments = new Bundle();
            arguments.putString("title", item.getTitle());
            arguments.putString("link", item.getLink());
            arguments.putString("predictedPrice", item.getPrice());
            arguments.putString("location", item.getLocation());
            arguments.putString("Colour", item.getColour());

            intent.putExtra("arguements", arguments);


            //Start a new activity instead of replacing with fragement, on second click
            startActivity(intent);


        }
    }

    /**
     * The default content for this Fragment has a TextView that is shown when
     * the list is empty. If you would like to change the text, call this method
     * to supply the text it should use.
     */
    public void setEmptyText(CharSequence emptyText) {
        View emptyView = mListView.getEmptyView();

        if (emptyText instanceof TextView) {
            ((TextView) emptyView).setText(emptyText);
        }
    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * <p/>
     * See the Android Training lesson <a href=
     * "http://developer.android.com/training/basics/fragments/communicating.html"
     * >Communicating with Other Fragments</a> for more information.
     */
    public interface OnFragmentInteractionListener {
        // TODO: Update argument type and name
        public void onFragmentInteraction(String id);
    }

}
