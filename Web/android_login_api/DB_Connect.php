<?php
 
$str = "Hello world!";
echo $str;

 
$link = mysql_connect( '192.168.100.101:3306', 'david', 'apUJP5VxBTZ9atXD' );
echo $str;
if ( !$link ) {
  die( 'Could not connect: ' . mysql_error() );
}

// Select the data base
$db = mysql_select_db( 'david', $link );
echo $str;
if ( !$db ) {
  die ( 'Error selecting database \'david\' : ' . mysql_error() );
}
 
$query = "
  SELECT *
  FROM users WHERE title LIKE '%".$_GET['email']."%'
  ORDER BY name ASC";
$result = mysql_query( $query );

// All good?
if ( !$result ) {
  // Nope
  $message  = 'Invalid query: ' . mysql_error() . "\n";
  $message .= 'Whole query: ' . $query;
  die( $message );
}


?>