
# Ex04 Time Table
## Date: 17/11/2026

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create an App inside the Django project.

### STEP 2
Create a static folder uder the created App and insert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html with the relevant attributes.

### STEP 4
Add rows using ```<tr>``` tag.

### STEP 5
Add your course schedule using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM
```
<html>
    <head>
        <title>slot time table 2026</title>
    </head>
    <body>
		<center><img src="logo.png" width="500"></center>
   <center><table border="1" cellspacing="2" cellpadding="10"></center>
	<caption>Slot time table 2026 - KANISHKA B(26010203)</caption>
		<tr bgcolor="dark green">
			<th>DAY/TIME</th>
			<th>MONDAY</th>
			<th>TUESDAY</th>
			<th>WEDNESDAY</th>
            <th>THURSDAY</th>
            <th>FRIDAY</th>
            <th>SATURADY</th>
		</tr>
        <tr bgcolor="pink">
			<td bgcolor="Burgundy">08-9:30</td>
			<td> EDM</td>
			<td>-</td>
			<td>EDM</td>
            <td>PY</td>
            <td>STAT</td>
            <td>-</td>
            <td bgcolor="white"></td>
		</tr>
        <tr bgcolor="grey">
			<td bgcolor="Royal Blue">09:45-11:15</td>
			<td>EDM</td>
			<td>FWAD</td>
			<td bgcolor="Yellow">-</td>
            <td>STAT</td>
            <td>FWAD</td>
            <td>CM</td>
		</tr>
        <tr bgcolor="Yellow">
        <td bgcolor="cyan">11:30-12:15</td>
        <td colspan="6"><center>LUNCH</center></td>
		</tr>
        <tr bgcolor="Yellow">
        <td bgcolor="dark green">12:15-1:00</td>
        <td colspan="6"><center>Mentor meet</center></td>
		</tr>
         <tr bgcolor="Yellow">
			 <td bgcolor="cyan">1:15-2:45</td>
			<td>FWAD</td>
			<td>BEEE</td>
			<td bgcolor="lime">-</td>
            <td>CE</td>
            <td bgcolor="lime">-</td>
            <td bgcolor="lime">-</td>
		</tr>
         <tr bgcolor="grey">
			<td bgcolor="Peach">3:00-4:30</td>
			<td > CA</td>
			<td>PY</td>
			<td>CE</td>
            <td>-</td>
            <td bgcolor="lime">-</td>
            <td bgcolor="lime">-</td>
		</tr>


        <center><table border="1" cellspacing="2" cellpadding="10"></center>
<tr bgcolor="cyan">
			<th>S.NO</th>
			<th>SUBJECT CODE</th>
			<th>SUBJECT NAME</th>
		</tr>
        <tr>
			<td  bgcolor="purple">1</td>
			<td>19AI414</td>
			<td>Fundamentals of Web Application Development(FWAD)</td>
		</tr>
         <tr>
			<td  bgcolor="purple">2</td>
			<td>19AI301 </td>
			<td>Python programming (PY)</td>
		</tr>
        <tr>
			<td  bgcolor="purple">3</td>
			<td>19MA211</td>
			<td> Statistics and Numerical(STAT)</td>
		</tr>
         <tr>
			<td  bgcolor="purple">4</td>
			<td>19EN101 </td>
			<td>Communicative English(CE)</td>
		</tr>
         <tr>
			<td  bgcolor="purple">5</td>
			<td>19AI302 </td>
			<td>Engineering Design and Modelling(EDM)</td>
		</tr>
         <tr>
			<td  bgcolor="purple">6</td>
			<td>19CS305 </td>
			<td>Computer Architecture(CA)</td>
		</tr>
         <tr>
			<td  bgcolor="purple">7</td>
			<td>19EEE305 </td>
			<td> Basic Electrical, Electronics and Measurement Engineering(BEEE)</td>
		</tr>
	</tabel>

	</body>
		</html>
```

## OUTPUT
![alt text](<Screenshot 2026-11-17 110200-1.png>)

##Result

The program for creating slot timetable using basic HTML tags is executed successfully.
