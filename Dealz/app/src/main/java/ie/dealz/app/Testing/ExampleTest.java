package ie.dealz.app.Testing;

import android.test.InstrumentationTestCase;

/**
 * Created by davidoregan on 17/05/2014.
 */

public class ExampleTest extends InstrumentationTestCase {
        public void test() throws Exception {
            final int expected = 1;
            final int reality = 5;
            assertEquals(expected, reality);
        }
}
