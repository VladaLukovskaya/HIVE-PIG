# HIVE-PIG (Relational DBs)

This is my project for the 3-rd laboratory work of Hadoop named Relational DBs. 

<h2><b>Example of an input file</b></h2><br/>
1,Ivanov,Ivan,technical writer,3<br/>
2,Petrov,Petr,developer,2<br/>
3,Alinova,Alina,recruiter,1<br/>
4,Anikina,Anna,researcher,2<br/>


<h2><b>The requests</b></h2><br/>
<h3><b>The first SQL request</b></h3><br/>
SELECT * FROM employees;

<h3><b>The second SQL request</b></h3><br/>
SELECT surname, name FROM heads WHERE dep_id = 3;<br/>

<h3><b>The third SQL request</b></h3><br/>
SELECT d.dep_id, d,dep_name, d.num_of_emp, h.surname, h.name FROM departments d JOIN heads h ON (d.dep_id = h.dep_id);

<h3><b>The fourth SQL request</b></h3><br/>
SELECT h.surname, h.name, e.position FROM employees e JOIN heads h ON (e.dep_id = h.dep_id);


<h3><b>The fifth SQL request</b></h3><br/>
SELECT * FROM employees e inner JOIN departments d ON (e.dep_id = d.dep_id);
