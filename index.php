<!DOCTYPE html>
<html>
<head>
    <title>Valores de la tabla room_data</title>
</head>
<body>
    <h1>Valores de la tabla room_data</h1>
    
    <table>
        <tr>
            <th>room_data_id</th>
            <th>room_id</th>
            <th>room_avg_temp</th>
            <th>room_max_temp</th>
            <th>room_min_temp</th>
            <th>tiempo_actual</th>
        </tr>
        
        <?php

        $host = '169.254.116.33';
        $port = 5433;
        $dbname = 'postgres';
        $username = 'postgres';
        $password = 'matigol';
        
        try {
            $conn = new PDO("pgsql:host=$host;port=$port;dbname=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $query = "SELECT * FROM room_data";
            $stmt = $conn->prepare($query);
            $stmt->execute();

            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                echo "<tr>";
                echo "<td>" . $row['room_data_id'] . "</td>";
                echo "<td>" . $row['room_id'] . "</td>";
                echo "<td>" . $row['room_avg_temp'] . "</td>";
                echo "<td>" . $row['room_max_temp'] . "</td>";
                echo "<td>" . $row['room_min_temp'] . "</td>";
                echo "<td>" . $row['tiempo_actual'] . "</td>";
                echo "</tr>";
            }
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
        
        $conn = null;
        ?>
        
    </table>
</body>
</html>
