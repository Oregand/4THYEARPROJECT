package ie.dealz.app.services;

import java.util.List;

import ie.dealz.app.models.Cars;
import retrofit.http.GET;
import retrofit.http.Query;

/**
 * Created by davidoregan on 09/04/2014.
 */
public interface CarService {
    @GET("/info.php")
    List<Cars> listGolfs(@Query("make") String makeQ);







    //?make={golf}
//    @GET("/yolo.php?make={makeQuery}")
//    List<Cars> listGolfs(@Path("makeQuery") @Query("make") String make); //String make);

}
