<!DOCTYPE html>
<html>
    <head>
        <title>First site</title>
    </head>
    <body>
        <form enctype="multipart/form-data", method="post">
            <input type="file" name="file">
            <input type="submit" value="Отправить">
        </form>
    </body>
</html>
<?php
include('inc/inc.php');
$row = 0;
$tmp = $_FILES["file"]["tmp_name"];
$array = array();
if (($handle = fopen("$tmp", "r")) !== FALSE) {
    while (($data = fgetcsv($handle,1000, "\t")) !== FALSE) {
        $num = count($data);
        $row++;
        for ($c=0; $c < $num; $c++) {
            if ($c == 2)
                $data[$c] = floatval($data[$c]);
            else
                $data[$c] = trim($data[$c]);

        }
        $array[$row] = $data;
    }
    fclose($handle);
}
$db->query("TRUNCATE TABLE `teacher`");
for ($i = 1; $i != $row; $i++)
{
    $temp = $array[$i];
    $db->query("INSERT INTO `teacher` (`Дисциплина`, `часы`, `Преподаватель`, `Группа`) VALUES ('$temp[0]', '$temp[2]','$temp[3]','$temp[4]')");
}

?>
