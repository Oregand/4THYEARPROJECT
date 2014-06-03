<?php

/**
* 
*/
class connect 
{
	
$str = "Hello world!";

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
}
 
?>