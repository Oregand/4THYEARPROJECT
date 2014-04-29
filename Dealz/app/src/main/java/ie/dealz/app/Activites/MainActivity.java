package ie.dealz.app.Activites;

import android.content.Intent;
import android.os.StrictMode;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;

import java.util.List;

import ie.dealz.app.Fragments.BrandListFragment;
import ie.dealz.app.Fragments.ItemFragment;
import ie.dealz.app.Fragments.ListFragment;
import ie.dealz.app.R;
import ie.dealz.app.models.Golf;
import ie.dealz.app.services.GolfService;
import retrofit.RestAdapter;

public class MainActivity extends ActionBarActivity implements ListFragment.OnFragmentInteractionListener, BrandListFragment.OnFragmentInteractionListener {


    FragmentManager fragmentManager = getSupportFragmentManager();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
//        StrictMode.ThreadPolicy policy = new StrictMode().ThreadPolicy.Builder().permitAll().build();
//        StrictMode.setThreadPolicy(policy);



        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//        apiTest();
        Fragment listFrag = new BrandListFragment();
        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
        transaction.replace(R.id.frame, listFrag);
        transaction.commit();
    }


    private void replaceListWithCars(String title) {
        ListFragment yoloFragment = new ListFragment();
        Bundle arguments = new Bundle();
        arguments.putString("make of car",title);

        yoloFragment.setArguments(arguments);
        yoloFragment.setHasOptionsMenu(true);


        FragmentTransaction transaction = fragmentManager.beginTransaction();
        transaction.replace(R.id.frame, yoloFragment, "CarsListFrag");
        transaction.setTransition(FragmentTransaction.TRANSIT_FRAGMENT_FADE);
        transaction.addToBackStack("CountriesListFragment");
//        transaction.remove(fragmentManager.findFragmentByTag("CountriesListFragment"));

        transaction.commit();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {

//        MenuInflater inflater = getMenuInflater();
//        inflater.inflate(R.menu.main, menu);


        return true;
    }



    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    public static void getGolfs() {
        RestAdapter restAdapter;
        List<Golf> golfs;

        restAdapter = new RestAdapter.Builder()
                .setServer("http://127.0.0.1")
                .build();

        GolfService golfService = restAdapter.create(GolfService.class);
        golfs = golfService.listGolfs();

        for (Golf golf : golfs) {
            Log.d("title", golf.title);
        }
    }

    @Override
    public void onFragmentInteraction(String id) {

        if (id.equals("Golf")) {
            replaceListWithCars(id); // Brings to list

        }
    }








}
