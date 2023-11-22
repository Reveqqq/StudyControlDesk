<?php
include('inc/inc.php');
$quere = "SELECT * FROM `teacher`";
$res = $db->query("$quere",1);
if ($res)
{
    echo'<table cellspacing=5 cellpadding=5>
              <tr>
                    <th>Преподаватель</th>
                    <th>Часы</th>
              </tr>';
}
foreach ($res as $r) {

    echo "
              <tr valign='top' style='border-bottom:ridge'>
                    <td align='left'>$r[Преподаватель]</td>
                    <td style='text-align:left;'><span style='word-wrap:break-word; float:left; max-width:130px;'>$r[часы]</span></td>
                    <td align='center'>
                    </td>
                  </tr>";
}
echo '</table>';

