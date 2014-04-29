package ie.dealz.app.services;

import java.util.List;

import ie.dealz.app.models.Golf;
import retrofit.http.GET;

/**
 * Created by davidoregan on 09/04/2014.
 */
public interface GolfService {
    @GET("/yolo.php")
    List<Golf> listGolfs();
}
