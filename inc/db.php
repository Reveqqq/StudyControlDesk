<?php

class DB
{
    protected $hostname;
    protected $username;
    protected $password;
    protected $database;
    protected $link = null;

    public function __construct($username = null, $password = null, $database = null, $hostname = null)
    {
        $hostname ? $this->hostname = $hostname : $this->hostname = $GLOBALS['mysql_host'];
        $username ? $this->username = $username : $this->username = $GLOBALS['mysql_user'];
        $password ? $this->password = $password : $this->password = $GLOBALS['mysql_pass'];
        $database ? $this->database = $database : $this->database = $GLOBALS['mysql_base'];
    }

    protected function _open()
    {
        if($this->link === null)
        {
            $this->link = mysqli_connect($this->hostname, $this->username, $this->password, $this->database);
            if(mysqli_connect_errno())
                exit('<br/><br/><b>Ошибка подключения к серверу MySQL: </b>'.mysqli_connect_error());
            if (!mysqli_set_charset($this->link, 'utf8'))
                exit('<br/><br/><b>Ошибка установки кодировки соединения MySQL. Текущая кодировка: </b>'.mysqli_character_set_name($this->link));
        }
    }

    protected  function _close()
    {
        if ($this->link)
            mysqli_close($this->link);
        $this->link = null;
    }

    public function query($sql, $fetch_mode = 2) //Fetch mode: MYSQL_NUM = 2; MYSQL_ASSOC = 1; MYSQL_BOTH = 3
    {
        global $debug;
        $this->_open();
        $res_ = mysqli_query($this->link, $sql);
        if ($debug !== 0 && $res_ === false)
            echo('<br/><br/><b>Ошибка MySQL запроса: </b>'.mysqli_error($this->link).'<br/>');
        if (is_bool($res_))
            $res = $res_;
        elseif (mysqli_affected_rows($this->link) === 0)
        {
            $res = false;
        }
        else
        {
            while ($row = mysqli_fetch_array($res_, $fetch_mode))
                $a[] = $row;
            $res = $a;
        }
        if (!is_bool($res_))
            mysqli_free_result($res_);
        $this->_close();
        return $res;
    }

    public function escape($str)
    {
        if (!isSet($this->link))
            $this->_open();
        return trim(mysqli_real_escape_string($this->link, $str));
    }

}