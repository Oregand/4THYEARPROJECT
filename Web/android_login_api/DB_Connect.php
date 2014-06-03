<?php
 
 
  $link = mysql_connect( '192.168.100.101:3306', 'david', 'apUJP5VxBTZ9atXD' );
  echo "Made it into db"
if ( !$link ) {
  die( 'Could not connect: ' . mysql_error() );
}

// Select the data base
$db = mysql_select_db( 'david', $link );
echo "double made it"
if ( !$db ) {
  die ( 'Error selecting database \'david\' : ' . mysql_error() );
}
 
?>