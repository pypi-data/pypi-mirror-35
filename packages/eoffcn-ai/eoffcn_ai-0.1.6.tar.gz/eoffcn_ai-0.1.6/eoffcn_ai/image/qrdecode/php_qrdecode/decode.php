<?php
require "vendor/autoload.php";


if (!isset($argv[1])) {
    exit("file_path require\r\n[Usage] php {$argv[0]} file_path");
}

$path = $argv[1];


$qrcode = new \Zxing\QrReader($path);
echo $qrcode->text();

