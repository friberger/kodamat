<?php
/*
* Code to query an SQLite database and return
* results as JSON.
*/

$param = $_GET["name"];
$param = '"%' . $param . '%"';
//echo $param;

// Specify your sqlite database name and path //
$dir = 'sqlite:livs.db';

// Instantiate PDO connection object and failure msg //
$dbh = new PDO($dir) or die("cannot open database");

// Define your SQL statement //
$query = "SELECT * FROM livs WHERE Livsmedelsnamn LIKE " . $param . "LIMIT 100 ;";


// Iterate through the results and pass into JSON encoder //
foreach ($dbh->query($query) as $row) {
  echo json_encode($row);
  echo '***';
}
?>
