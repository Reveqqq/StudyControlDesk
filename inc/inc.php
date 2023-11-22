<?php
include('db.php');

$db = new DB(
    "root",
    "",
    "Datateacher",
    "localhost"
);

if (!$db)
    exit("БД не работает");
session_start();

?>
