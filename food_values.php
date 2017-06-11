<?php
/*
* Code to query an SQLite database and return
* results as JSON.
*/

$foodStuff = $_GET["foodStuff"];
//echo $foodStuff;

$foodStuff=urldecode($foodStuff);
//$db = new SQLite3('livs.db');

class MyDB extends SQLite3
{
    function __construct()
    {
        $this->open('livs.db');
    }
}

$db = new MyDB();
//Testar lite
//$foodStuff="'Ister gris', 'Kokosfett'";


// Define your SQL statement //
//$queryString = "SELECT * FROM livs WHERE Livsmedelsnamn IN '" . $foodStuff . "';";
$queryString = "SELECT * FROM livs WHERE Livsmedelsnamn IN (" . $foodStuff . ");";



$result = $db->query($queryString);

$resultString = '';

while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
  $resultString=$resultString . json_encode($row) . '##';
};

$resultString = rtrim($resultString, '##');

echo $resultString;

?>
