package ie.dealz.app.Activites;

/**
 * Created by davidoregan on 03/06/2014.
 */

import org.json.JSONException;
import org.json.JSONObject;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import ie.dealz.app.R;
import ie.dealz.app.Registration.DatabaseHandler;
import ie.dealz.app.Registration.UserFunctions;

public class LoginRegActivity extends Activity {
    Button btnLogin;
    Button btnLinkToRegister;
    EditText inputEmail;
    EditText inputPassword;
    TextView loginErrorMsg;

    // JSON Response node names
    private static String KEY_SUCCESS = "success";
    private static String KEY_UID = "uid";
    private static String KEY_NAME = "name";
    private static String KEY_EMAIL = "email";
    private static String KEY_CREATED_AT = "created_at";

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.loginreg);

        // Importing all assets like buttons, text fields
        inputEmail = (EditText) findViewById(R.id.loginEmail);
        inputPassword = (EditText) findViewById(R.id.loginPassword);
        btnLogin = (Button) findViewById(R.id.btnLogin);
        btnLinkToRegister = (Button) findViewById(R.id.btnLinkToRegisterScreen);
        loginErrorMsg = (TextView) findViewById(R.id.login_error);

        // Login button Click Event
        btnLogin.setOnClickListener(new View.OnClickListener() {

            public void onClick(View view) {
                String email = inputEmail.getText().toString();
                String password = inputPassword.getText().toString();
                new MyAsyncTask().execute(email, password);

            }
        });

        // Link to Login Screen
        btnLinkToRegister.setOnClickListener(new View.OnClickListener() {

            public void onClick(View view) {
                Intent i = new Intent(getApplicationContext(),RegisterActivity.class);
                startActivity(i);
                // Close Registration View
                finish();
            }
        });



    }


class MyAsyncTask extends AsyncTask<String, Void, JSONObject> {

    protected JSONObject doInBackground(String... params) {
        UserFunctions userFunction = new UserFunctions();
        if (params.length != 2)
            return null;
        JSONObject json = userFunction.loginUser(params[0], params[1]);
        return json;
    }

    protected void onPostExecute(JSONObject json) {
        try {
            if (json != null && json.getString(KEY_SUCCESS) != null) {
                loginErrorMsg.setText("");
                String res = json.getString(KEY_SUCCESS);
                if (Integer.parseInt(res) == 1) {
                    // user successfully logged in
                    // Store user details in SQLite Database
                    DatabaseHandler db = new DatabaseHandler(getApplicationContext());
                    JSONObject json_user = json.getJSONObject("user");

                    // Clear all previous data in database
                    UserFunctions userFunction = new UserFunctions();
                    userFunction.logoutUser(getApplicationContext());
                    db.addUser(json_user.getString(KEY_NAME), json_user.getString(KEY_EMAIL), json.getString(KEY_UID), json_user.getString(KEY_CREATED_AT));


                    Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                    startActivity(intent);

                    // Close Login Screen
                    finish();
                } else {
                    // Error in login
                    loginErrorMsg.setText("Incorrect username or password");
                }
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    }
}