package ie.dealz.app.Fragments;

import android.app.Activity;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.text.util.Linkify;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.AbsListView;
import android.widget.TextView;


import org.androidannotations.annotations.Background;

import java.util.List;
import java.util.regex.Pattern;

import ie.dealz.app.Adapters.CarAdapter;
import ie.dealz.app.R;
import ie.dealz.app.models.Cars;
import ie.dealz.app.services.CarService;
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
public class ItemFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    private OnFragmentInteractionListener mListener;
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
    public ItemFragment() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


//        getActivity().setTitle("Cars");
//        arrayOfCars = new CarAdapter(getActivity(), R.layout.list_item);

        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }

        // TODO: Change Adapter to display your content
        mAdapter = new CarAdapter(getActivity());
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        Bundle bundle = this.getArguments();
        View view = inflater.inflate(R.layout.singlecar, container, false);
        TextView tv = (TextView) view.findViewById(R.id.sc_title);
        TextView cv = (TextView) view.findViewById(R.id.sc_colour);
        TextView pv = (TextView) view.findViewById(R.id.sc_PP);
        TextView lv = (TextView) view.findViewById(R.id.sc_location);
        TextView linkv = (TextView) view.findViewById(R.id.sc_link);
//        linkv.setMovementMethod(LinkMovementMethod.getInstance());
//
//
//        String text = "Dealz";
//        String link = bundle.getString("link");
//        Pattern pattern = Pattern.compile(link);
//        Linkify.addLinks(linkv, pattern, "");
//        linkv.setText(Html.fromHtml(text));



        WebView wv = (WebView) view.findViewById(R.id.sc_webView);



        tv.setText(bundle.getString("title"));
        cv.setText(bundle.getString("Colour"));
        pv.setText(bundle.getString("location"));
        lv.setText(bundle.getString("predictedPrice"));
        wv.getSettings().setJavaScriptEnabled(true);
        wv.loadUrl(bundle.getString("link"));
        linkv.setText(bundle.getString("link"));

        return view;
    }

    @Background
    void apiTest() {

        String makeQ = "golf";


        RestAdapter restAdapter = new RestAdapter.Builder().setServer("http://david.pimyride.com").build();
        CarService service = restAdapter.create(CarService.class);
        List<Cars> golfs = service.listGolfs(makeQ);


        for (Cars golf : golfs)
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
