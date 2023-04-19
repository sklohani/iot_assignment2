CREATE TABLE IF NOT EXISTS `dht11` (
    id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    humidity int(4),
    temperature int(4)
) CHARSET=utf8;

-- :: Run ::
-- mysql -u 19mcme16 -p dht11 < make_table.sql