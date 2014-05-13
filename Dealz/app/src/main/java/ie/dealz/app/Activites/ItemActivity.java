package ie.dealz.app.Activites;


import android.os.StrictMode;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import java.util.List;
import ie.dealz.app.Fragments.ItemFragment;
import ie.dealz.app.R;
import ie.dealz.app.models.Cars;
import ie.dealz.app.services.CarService;
import retrofit.RestAdapter;

public class ItemActivity extends ActionBarActivity implements  ItemFragment.OnFragmentInteractionListener {


    FragmentManager fragmentManager = getSupportFragmentManager();


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.item_activity);
//        apiTest();

        //Replace with Itemfragment?
        Bundle bundle = this.getIntent().getBundleExtra("arguements");
        Fragment listFrag = new ItemFragment();
        listFrag.setArguments(bundle);

        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
        transaction.replace(R.id.Itemframe, listFrag);
        transaction.commit();
    }



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {

            return super.onCreateOptionsMenu( menu );
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
        List<Cars> golfs;
        String makeQ = "golf";

        restAdapter = new RestAdapter.Builder()
                .setServer("http://david.pimyride.com")
                .build();

        CarService golfService = restAdapter.create(CarService.class);
        golfs = golfService.listGolfs(makeQ);

        for (Cars golf : golfs) {
            Log.d("title", golf.title);
        }
    }

    @Override
    public void onFragmentInteraction(String id) {
    }






}
