<?php 
 	$db = new SQLite3('analytics.sqlite', SQLITE3_OPEN_CREATE | SQLITE3_OPEN_READWRITE);
	$db->query('CREATE TABLE IF NOT EXISTS "scoreboard" (
	    "user_id" VARCHAR PRIMARY KEY,
	    "score" VARCHAR,
	    "react_time" VARCHAR
	)');

	if ($_SERVER['REQUEST_METHOD'] === 'POST') {

		$correct=0;
		$ans=['diff', 'same', 'same'];
		for($i=1; $i < 4; $i++){                               //判斷對錯
			if($_POST["t${i}_response"] == $ans[$i-1])         //"t${i}_responce"==t1_response
				$correct += 1;
		}
		$ave_time =($_POST['t1_rt']+$_POST['t2_rt']+$_POST['t3_rt'])/3000;
		$id = str_replace(' ', '', $_POST['id']);
		echo "Hi $id!!!Your correct rate : $correct/3 <br>";
		echo "The average react time : $ave_time second <br><br>";

		$result = @$db->querySingle('SELECT*FROM scoreboard WHERE user_id="'.$id.'"',TRUE);
		if($result){
			$statement = $db->prepare('UPDATE "scoreboard" SET score=:score,react_time=:react_time WHERE user_id=:uid');
			$statement->bindValue(':uid', $id);
			$statement->bindValue(':score', $correct);
			$statement->bindValue(':react_time', $ave_time);
			$statement->execute(); 
		}
		else{
			$statement = $db->prepare('INSERT INTO "scoreboard" ("user_id", "score", "react_time")
			VALUES (:uid, :score, :react_time)');
			$statement->bindValue(':uid', $id);
			$statement->bindValue(':score', $correct);
			$statement->bindValue(':react_time', $ave_time);
			$statement->execute(); 
		}
		
		
	}
	else{
		if($_GET['id']){
			$id = str_replace(' ', '', $_GET['id']);
		}
		else{
			echo "Give me your id with: <br>";
			echo "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]?id=[]";
			die();
		}
	}

	$statement = $db->prepare('SELECT * FROM scoreboard ORDER by score DESC');
	$result = $statement->execute();
	echo("Here is the RanK:<br>");
	while ($r = $result->fetchArray(SQLITE3_NUM)) {
		echo("Id: $r[1], Score: $r[2], React_time: $r[3]<br>");
	}

?>