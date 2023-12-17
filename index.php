<?php
include('inc/inc.php');

function get_sql_list($query) {
    global $db;
    return array_map(function ($res) { return $res[0]; }, $db->query($query));
}

if ($_FILES) {
    $hoursIndex = 2;
    $filename = $_FILES["file"]["tmp_name"];
    $data = array();
    if (($handle = fopen($filename, "r")) !== FALSE) {
        while (($row = fgetcsv($handle, 1000, "\t")) !== FALSE) {
            foreach ($row as $index => &$item) {
                $item = trim($item);
                if ($index == $hoursIndex)
                    $item = floatval($item);
            }
            $data[] = $row;
        }
        fclose($handle);
    }
    $db->query("TRUNCATE TABLE `data`");
    foreach ($data as $row) {
        $discipline = $db->escape($row[0]);
        $hours = $db->escape($row[2]);
        $teacher = $db->escape($row[3]);
        $group = $db->escape($row[4]);
        $db->query("INSERT INTO `data` (`discipline`, `hours`, `teacher`, `group`) VALUES ('$discipline', '$hours','$teacher','$group')");
    }
}

$teachers = get_sql_list('SELECT DISTINCT `teacher` FROM `data` ORDER BY `teacher`');
$groups = get_sql_list('SELECT DISTINCT `group` FROM `data` ORDER BY `group`');

$selectedTeacher = $_GET['teacher'];
$selectedGroup = $_GET['group'];
?>
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
<div>
    <form action="" method="get">
        <select name="group" onchange="this.form.submit()">
            <option disabled <?= empty($selectedGroup) ? "selected" : "" ?>>Выберите группу</option>
            <? foreach ($groups as $group) : ?>
                <option value="<?= $group ?>" <?= !empty($group) && $group == $selectedGroup ? "selected" : "" ?>><?= $group ?></option>
            <? endforeach; ?>
        </select>
    </form>
    <br>
    <form action="" method="get">
        <select name="teacher" onchange="this.form.submit()">
            <option disabled <?= empty($selectedTeacher) ? "selected" : "" ?>>Выберите преподавателя</option>
            <? foreach ($teachers as $teacher) : ?>
                <option value="<?= $teacher ?>" <?= !empty($selectedTeacher) && $teacher == $selectedTeacher ? "selected" : "" ?>><?= $teacher ?></option>
            <? endforeach; ?>
        </select>
    </form>
    <br>
    <form action="./" enctype="multipart/form-data" method="post">
        <input type="file" name="file">
        <input type="submit" value="Отправить">
    </form>
</div>
<br>
<br>
<div>
    <?php
    $teacher = $selectedTeacher;
    $group = $selectedGroup;
    if (!empty($teacher) || !empty($group)) {
        $teacher = $db->escape($teacher);
        $group = $db->escape($group);
        $field = !empty($teacher) ? 'teacher' : 'group';
        $fieldValue = !empty($teacher) ? $teacher : $group;
        $sql = "SELECT * FROM `data` WHERE `$field` = '$fieldValue'";
        $sql = "SELECT `$field`, `discipline`, SUM(`hours`) AS `hours` FROM `data` WHERE `$field` = '$fieldValue' GROUP BY `$field`,`discipline`";
        $data = $db->query($sql, MYSQLI_BOTH);
        ?>
        <table>
            <tr>
                <th><?= !empty($teacher) ? "Преподаватель" : "Группа" ?></th>
                <th>Предмет</th>
                <th>Часы</th>
            </tr>
            <?php foreach ($data as $row) : ?>
                <tr style='border-bottom:ridge'>
                    <td><?= $row[0] ?></td>
                    <td><?= $row['discipline'] ?></td>
                    <td style='text-align:left;'><span style='word-wrap:break-word; float:left; max-width:130px;'><?= floatval($row['hours']) / 18 ?></span></td>
                </tr>
            <?php endforeach; ?>
        </table>
    <?php } ?>
</div>
</body>
</html>
