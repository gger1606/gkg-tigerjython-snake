Informatik Auftrag
Funktionsweise des Spiels:
Das Spiel ist sehr simple gestaltet. Im Spiel hat es eine Schlange, die Äpfel fressen muss, 
aber es darf nicht die herumliegenden Steine berühren oder das Spielfeld verlassen, 
ansonsten ist das Spiel vorbei. Wenn die Schlange stirbt hört man einen senkenden Ton und wenn die Schlange einen Apfel frisst hört man einen erhebenden Ton. 
Damit das Spiel beginnt muss man zuerst auf die grüne Play-Taste klicken. Dann sollte das Spiel starten. Nun kann man mit den vier Tasten oben,
unten, links und rechts die Schlange steuern und die Äpfel fressen. Jeder gefressene Apfel ergibt +100 Punkte für den Spieler. 
Wenn die Schlange nun durch einen Stein oder durch das Verlassen der Spielfläche stirbt, so steht die Anzahl erreichte Punkte unten links. 
Damit man das Spiel neu starten kann (und nicht immer ein neues Fenster öffnen muss), muss man einfach einmal auf die Enter-Taste klicken und alles beginnt von hinten los.
Aufbau des Codes:
Mein Programm ist so aufgebaut, dass die Turtle zuerst die Spielfläche zeichnet.
Die Fläche wird mit hideTurtle() erstellt, sodass man nicht immer warten muss bis das Quadrat fertig gezeichnet wurde.
Dann habe ich in die Funktion snakeTurtleIsAlive() einige Regeln programmiert z.B. wenn sie sich die Schlange 
ausserhalb des Quadrates befindet dann ist sie tot oder wenn sie einen Stein berührt.
Anschliessend kommt die Funktion waitForInputName(), die dafür sorgt, dass der/die Spieler/in zuerst seinen Namen eingeben muss, um das Spiel zu starten. 
Als nächstes habe ich den Apfel erstellt, der immer wieder irgendwo auf der Spielfläche auftaucht. Mit eatApple() sollten die Äpfel von der Schlange gefressen werden und einen 
Ton hinterlassen.
Nun habe ich auch noch die Steine erstellt. Insgesamt sind es elf Stück. Die Funktion ist so aufgebaut, dass am Anfang des Spiels 11 Steine irgendwo auf 
der Fläche platziert werden und der Schlange im Weg stehen sollten.
Mit der Funktion deleteStone() sollten die Steine nicht mehr auf der Fläche zu sehen sein. 
In der Funktion Play werden alle obenstehenden Funktionen wieder aufgerufen. Dazu ist noch die Funktion drinnen, mit der man die Schlange steuert in einer While schleife.
Nach der schleife ist die Funktion für den Neustart definiert und der Ton, wenn die Schlange sterben sollte.
Schlussendlich wird die Play und die waitForInputName() Funktion in die Main() Funktion eingefügt, damit man eine kurze Funktion am Ende hat. 
Wichtige Funktion: 
Eine wichtige Funktion (meiner Meinung nach) ist die deleteStone(), denn ohne diese Funktion könnte man das Spiel nicht neustarten, 
da die Steine bleiben und dazu noch 11 weitere Steine auftauchen würden wenn man einen Neustart machen würde ohne die Funktion waitForInputName().
Hoger Teimouri 18.11.2020
