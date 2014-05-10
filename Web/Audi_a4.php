<?php
// Connect to MySQL

//Everytime I change this file,
//From terminal get into git folder(4thYEARPROGECT)
//git commit -am 'Commit message'
//git push
//
// Log into server 
// ssh david@web.raven.com
// cd 4THYEARPROJECT
// git pull
//
//
// david.pimyride.com
//
$link = mysql_connect( '192.168.100.101:3306', 'david', 'apUJP5VxBTZ9atXD' );
if ( !$link ) {
  die( 'Could not connect: ' . mysql_error() );
}

// Select the data base
$db = mysql_select_db( 'david', $link );
if ( !$db ) {
  die ( 'Error selecting database \'david\' : ' . mysql_error() );
}

// Fetch the data
$query = "
  SELECT *
  FROM a4Dealz
  ORDER BY title ASC";
$result = mysql_query( $query );

// All good?
if ( !$result ) {
  // Nope
  $message  = 'Invalid query: ' . mysql_error() . "\n";
  $message .= 'Whole query: ' . $query;
  die( $message );
}

// Print out rows
$prefix = '';
// echo "[\n";

$entries = array();

while ( $row = mysql_fetch_assoc( $result ) ) {
  // echo $prefix . " {\n";
  // echo '  "title": "' . $row['title'] . '",' . "\n";
  // echo '  "link": "' . $row['link'] . '",' . "\n";
  // echo '  "price": "' . $row['price'] . '",' . "\n";
  // echo '  "carYear": ' . $row['carYear'] . ',' . "\n";
  // echo '  "location": "' . $row['location'] . '",' . "\n";
  // echo '  "mileage": "' . $row['mileage'] . '",' . "\n";
  // echo '  "engine": ' . $row['engine'] . '' . "\n";
  // echo " }";
  // $prefix = ",\n";
	$entry = array();
	$entry['title'] = utf8_encode($row['title']);
	$entry['link'] = utf8_encode($row['link']);
	$entry['location'] = utf8_encode($row['location']);
	$entry['Colour'] = utf8_encode($row['Colour']);
	$entry['predictedPrice'] = utf8_encode($row['predictedPrice']);



	// $test =  string json_encode ( mixed $row [, int $options = 0 [, int $depth = 512 ]] );
	// echo $test;
	// print_r($test);
	// var_dump($entry);

	$entries[] = $entry;

}
// echo "\n]";
// var_dump($entries);
echo json_encode($entries);

// Close the connection
mysql_close($link);
?>