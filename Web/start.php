<?php

// Make a MySQL Connection
mysql_connect("localhost:8889", "root", "root") or die(mysql_error());
mysql_select_db("Carzone") or die(mysql_error());

// Retrieve all the data from the "example" table
$result = mysql_query("SELECT * FROM golf")
or die(mysql_error());  

// store the record of the "example" table into $row
$row = mysql_fetch_array( $result );
// Print out the contents of the entry 

echo "<table border='1'>";
echo "<tr> <th>title</th> <th>link</th> <th>price</th> <th>carYear</th> <th>location</th> <th>mileage</th> <th>engine</th> </tr>";
// keeps getting the next row until there are no more to get
while($row = mysql_fetch_array( $result )) {
	// Print out the contents of each row into a table
	echo "<tr><td>"; 
	echo $row['title'];
	echo "</td><td>"; 
	echo $row['link'];
	echo "</td><td>"; 
	echo $row['price'];
	echo "</td><td>"; 
	echo $row['carYear'];
	echo "</td><td>"; 
	echo $row['location'];
	echo "</td><td>"; 
	echo $row['mileage'];
	echo "</td><td>"; 
	echo $row['engine'];
	echo "</td></tr>"; 

} 

echo "</table>";



?>

