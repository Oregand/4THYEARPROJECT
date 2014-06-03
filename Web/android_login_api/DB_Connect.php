<?php
 
class DB_Connect {
 
    // constructor
    function __construct() {
         
    }
 
    // destructor
    function __destruct() {
        // $this->close();
    }
 
$link = mysql_connect( '192.168.100.101:3306', 'david', 'apUJP5VxBTZ9atXD' );
if ( !$link ) {
  die( 'Could not connect: ' . mysql_error() );
}

// Select the data base
$db = mysql_select_db( 'david', $link );
if ( !$db ) {
  die ( 'Error selecting database \'david\' : ' . mysql_error() );
}
        // return database handler
        return $con;
    }
 
    // Closing database connection
    public function close() {
        mysql_close();
    }
 
}
 
?>