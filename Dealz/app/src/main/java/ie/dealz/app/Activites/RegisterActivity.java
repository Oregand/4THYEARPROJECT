package ie.dealz.app.Activites;

/**
 * Created by davidoregan on 03/06/2014.
 */
import org.json.JSONException;
import org.json.JSONObject;

import ie.dealz.app.R;
import ie.dealz.app.Registration.DatabaseHandler;
import ie.dealz.app.Registration.UserFunctions;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class RegisterActivity extends Activity {
    Button btnRegister;
    Button btnLinkToLogin;
    EditText inputFullName;
    EditText inputEmail;
    EditText inputPassword;
    TextView registerErrorMsg;

    // JSON Response node names
    private static String KEY_SUCCESS = "success";
    private static String KEY_ERROR = "error";
    private static String KEY_ERROR_MSG = "error_msg";
    private static String KEY_UID = "uid";
    private static String KEY_NAME = "name";
    private static String KEY_EMAIL = "email";
    private static String KEY_CREATED_AT = "created_at";

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.register);

        // Importing all assets like buttons, text fields
        inputFullName = (EditText) findViewById(R.id.registerName);
        inputEmail = (EditText) findViewById(R.id.registerEmail);
        inputPassword = (EditText) findViewById(R.id.registerPassword);
        btnRegister = (Button) findViewById(R.id.btnRegister);
        btnLinkToLogin = (Button) findViewById(R.id.btnLinkToLoginScreen);
        registerErrorMsg = (TextView) findViewById(R.id.register_error);

        // Register Button Click event
        btnRegister.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                String name = inputFullName.getText().toString();
                String email = inputEmail.getText().toString();
                String password = inputPassword.getText().toString();
                new MyAsyncTask().execute(name, email, password);
        }
    });

        btnLinkToLogin.setOnClickListener(new View.OnClickListener(){

            public void onClick (View view){
                Intent i = new Intent(getApplicationContext(),LoginRegActivity.class);
                startActivity(i);
                finish();
            }
        });

    }

class MyAsyncTask extends AsyncTask<String, Void, JSONObject> {

        protected JSONObject doInBackground(String... params) {
            UserFunctions userFunction = new UserFunctions();
            if (params.length != 3)
                return null;
            JSONObject json = userFunction.registerUser(params[0], params[1], params[2]);
            return json;
        }

        protected void onPostExecute(JSONObject json) {
            // check for login response
            try {
                if (json != null && json.getString(KEY_SUCCESS) != null) {
                    registerErrorMsg.setText("");
                    String res = json.getString(KEY_SUCCESS);
                    if(Integer.parseInt(res) == 1){
                        // user successfully registred
                        // Store user details in SQLite Database
                        DatabaseHandler db = new DatabaseHandler(getApplicationContext());
                        JSONObject json_user = json.getJSONObject("user");

                        // Clear all previous data in database
                        UserFunctions userFunction = new UserFunctions();
                        userFunction.logoutUser(getApplicationContext());
                        db.addUser(json_user.getString(KEY_NAME), json_user.getString(KEY_EMAIL), json.getString(KEY_UID), json_user.getString(KEY_CREATED_AT));

                        Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                        startActivity(intent);

                        finish();
                    }else{
                        // Error in registration
                        registerErrorMsg.setText("Error in registration");
                    }
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }
}