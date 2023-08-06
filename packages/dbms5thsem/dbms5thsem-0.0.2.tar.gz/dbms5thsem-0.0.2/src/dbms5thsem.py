""" sql_programs = 1 library ,2 order ,3 movie ,4 college ,5 company]"""

def library():
    print("""
/* drop database test027_LIBRARY; */
create database test027_LIBRARY;
use test027_LIBRARY;
create table PUBLISHER
(
	Name varchar(25),
	Address varchar(25),
	Phone bigint,
	primary key(Name)
);
create table BOOK
(
	Book_id int,
	Title varchar(25),
	Publisher_name varchar(25),
	Pub_year int,
	primary key(Book_id),
	foreign key(Publisher_name) references PUBLISHER(Name) on delete cascade
);
create table BOOK_AUTHORS
(
	Book_id int,
	Author_name varchar(25),
	primary key(Book_id),
	foreign key(Book_id) references BOOK(Book_id) on delete cascade
);
create table LIBRARY_BRANCH
(
	Branch_id int,
	Branch_name varchar(25),
	Address varchar(25),
	primary key(Branch_id)
);
create table BOOK_COPIES
(
	Book_id int,
	Branch_id int,
	No_of_copies int,
	primary key(Book_id,Branch_id),
	foreign key(Book_id) references BOOK(Book_id) on delete cascade,
	foreign key(Branch_id) references LIBRARY_BRANCH(Branch_id) on delete cascade
);
create table BOOK_LENDING
(
	Book_id int,
	Branch_id int,
	Card_no int,
	Date_out date,
	Due_date date,
	primary key(Book_id,Branch_id,Card_no),
	foreign key(Book_id) references BOOK(Book_id) on delete cascade,
	foreign key(Branch_id) references LIBRARY_BRANCH(Branch_id) on delete cascade
);

desc PUBLISHER;
desc BOOK;
desc BOOK_AUTHORS;
desc LIBRARY_BRANCH;
desc BOOK_COPIES;
desc BOOK_LENDING;

insert into PUBLISHER values
('a','a',12345),
('b','b',23456),
('c','c',34567);
insert into BOOK values
(1,'a','a',2001),
(2,'b','b',2005),
(3,'c','c',2010);
insert into BOOK_AUTHORS values
(1,'a'),
(2,'b'),
(3,'c');
insert into LIBRARY_BRANCH values
(1,'a','a'),
(2,'b','b');
insert into BOOK_COPIES values
(1,1,10),
(1,2,11),
(2,1,12),
(2,2,15);
insert into BOOK_LENDING values
(1,1,1,'2017-01-10','2017-06-10'),
(1,2,2,'2017-01-11','2017-06-11'),
(2,1,1,'2017-01-12','2017-06-12'),
(2,2,2,'2017-01-13','2017-06-13'),
(3,1,1,'2017-01-14','2017-06-14'),
(3,2,2,'2017-01-15','2017-06-15'),
(1,2,3,'2017-01-16','2017-06-16');

select * from PUBLISHER;
select * from BOOK;
select * from BOOK_AUTHORS;
select * from LIBRARY_BRANCH;
select * from BOOK_COPIES;
select * from BOOK_LENDING;

/*  1  */
select b.Book_id, b.Title, p.Name, ba.Author_Name, bc.No_of_Copies, l.Branch_Name
from BOOK b,PUBLISHER p,BOOK_AUTHORS ba,BOOK_COPIES bc,LIBRARY_BRANCH l
where b.Publisher_Name = p.Name and b.Book_id = ba.Book_id and b.Book_id = bc.Book_id and bc.Branch_id = l.Branch_id;

/*  2  */
select bl.Card_No, count(*) as Number_of_books
from BOOK_LENDING bl
where bl.Date_Out between '2017-01-01' and '2017-07-01'
group by bl.Card_No
having count(*) >= 3;

/*  3  */
delete from BOOK where Book_id = 3;

/*  4  */
create table PBOOK
(
	Book_id int,
	Title varchar(25),
	Publisher_name varchar(25),
	Pub_year int,
	primary key(Book_id,Pub_year)
)
partition by range (Pub_Year)
(
  partition p1 values less than (2002),
  partition p2 values less than (2006),
  partition p3 values less than (maxvalue)
);
insert into PBOOK values
(1,'a','a',2001),
(2,'b','b',2005),
(3,'c','c',2010);
select * from PBOOK partition(p1);
select * from PBOOK partition(p2);
select * from PBOOK partition(p3);

/*  5  */
create view available as
(
	select Book_id, sum(No_of_copies) - (select count(Card_no) from BOOK_LENDING where b.Book_id = Book_id) as avail_copies
	from BOOK_COPIES b
	group by Book_id
);
select * from available;    
    """)

def order():
    print("""
/* drop database test027_ORDER; */
create database test027_ORDER;
use test027_ORDER;
create table SALESMAN
(
	Salesman_id int,
	Name  varchar(25),
	City  varchar(25),
	Commission int,
	primary key(Salesman_id)
);
create table CUSTOMER
(
	Customer_id int,
	Cust_name varchar(25),
	City  varchar(25),
	Grade int,
	Salesman_id int,
	primary key(Customer_id),
	foreign key(Salesman_id) references SALESMAN(Salesman_id) on delete cascade
);
create table ORDERS
(
	Ord_no int, 
	Purchase_amt int,
	Ord_date date, 
	Customer_id int, 
	Salesman_id int, 
	primary key(Ord_no),
	foreign key(Customer_id) references CUSTOMER(Customer_id) on delete cascade, 
	foreign key(Salesman_id) references SALESMAN(Salesman_id) on delete cascade
);

desc SALESMAN;
desc CUSTOMER;
desc ORDERS;

insert into SALESMAN values
(1,'a','a',1),
(2,'b','b',2),
(3,'c','c',3);
insert into CUSTOMER values
(1,'a','d',1,1),
(2,'b','b',2,2),
(3,'c','c',3,1),
(4,'d','d',4,2),
(5,'d','d',3,3);
insert into ORDERS values
(1,100,'2020-01-01',1,1),
(2,200,'2020-01-01',1,2),
(3,300,'2020-01-02',2,1),
(4,400,'2020-01-02',2,2),
(5,500,'2020-01-03',3,1),
(6,600,'2020-01-03',3,2),
(7,700,'2020-01-04',4,1),
(8,600,'2020-01-04',4,2);

select * from SALESMAN;
select * from CUSTOMER;
select * from ORDERS;

/*  1  b = Bangalore  count = 2(c,d has more)*/
select count(*)
from CUSTOMER
where Grade > (select avg(Grade) from CUSTOMER where City = 'b');

/* 2 */
select Salesman_id,Name
from SALESMAN
where Salesman_id in (select Salesman_id from CUSTOMER group by Salesman_id having count(*) > 1);

/* 3 */
select s.Name,'exists' as Same_city 
from SALESMAN s
where City in (select City from CUSTOMER where s.Salesman_id= Salesman_id) 
union 
select Name,'not exists' as Same_city 
from SALESMAN s 
where City not in (select City from CUSTOMER where s.Salesman_id = Salesman_id);

/* 4  (aa dina yarige heccu amount got)*/
create view Highest_order as 
select s.Salesman_id,s.Name,o.Purchase_amt,o.Ord_date
from SALESMAN s,ORDERS o
where s.Salesman_id = o.Salesman_id;

select Name,Ord_date
from Highest_order h
where Purchase_amt = (select max(Purchase_amt) from Highest_order where h.Ord_date = Ord_date);

/* 5 */
delete from SALESMAN where Salesman_id=3;

select * from SALESMAN;
select * from CUSTOMER;
select * from ORDERS;    
    """)

def movie():
    print("""
/* drop database test027_MOVIE; */
create database test027_MOVIE;
use test027_MOVIE;
create table ACTOR
(
	Act_id int,
	Act_name varchar(25),
	Act_gender varchar(6),
	primary key(Act_id)
);
create table DIRECTOR
(
	Dir_id int,
	Dir_name varchar(25),
	Dir_phone bigint,
	primary key(Dir_id)
);
create table MOVIES
(
	Mov_id int,
	Mov_title varchar(25),
	Mov_year int,
	Mov_lang varchar(25),
	dir_id int,
	primary key(Mov_id),
	foreign key(Dir_id) references DIRECTOR(Dir_id) on delete cascade
);
create table MOVIE_CAST
(
	Act_id int,
	Mov_id int,
	Role varchar(25),
	primary key(Act_id,Mov_id),
	foreign key(Act_id) references ACTOR(Act_id) on delete cascade,
	foreign key(Mov_id) references MOVIES(Mov_id) on delete cascade
);
create table RATING
(
	Rat_id int,
	Mov_id int,
	Rev_stars int,
	primary key(Rat_id),
	foreign key(Mov_id) references MOVIES(Mov_id) on delete cascade
);

desc ACTOR;
desc DIRECTOR;
desc MOVIES;
desc MOVIE_CAST;
desc RATING;

insert into ACTOR values
(1,'a','m'),
(2,'b','f');
insert into DIRECTOR values
(1,'h',12345),
(2,'ss',23456);
insert into MOVIES values
(1,'a',1990,'eng',1),
(2,'b',2001,'eng',1),
(3,'c',2017,'eng',2);
insert into MOVIE_CAST values
(1,1,'a'),
(1,2,'b'),
(1,3,'b'),
(2,1,'b'),
(2,2,'d');
insert into RATING values
(1,1,2),
(2,2,4),
(3,1,5),
(4,3,2);

select * from ACTOR;
select * from DIRECTOR;
select * from MOVIES;
select * from MOVIE_CAST;
select * from RATING;

/* 1  h= Hitchcock */
select m.Mov_title from MOVIES m,DIRECTOR d where m.Dir_id=d.Dir_id and d.Dir_name='h';

/* 2  */
select distinct m.Mov_title from MOVIES m,MOVIE_CAST mc
where m.Mov_id = mc.Mov_id and (select count(Mov_id) from MOVIE_CAST where Act_id=mc.Act_id)>=2;

/* 3  only a acted before and after  (copy of same in ()) */
select a.Act_name from ACTOR a,MOVIE_CAST mc,MOVIES m
where a.Act_id = mc.Act_id and mc.Mov_id = m.Mov_id and m.Mov_year<2000 
and a.Act_name in (select a.Act_name from ACTOR a,MOVIE_CAST mc,MOVIES m
where a.Act_id = mc.Act_id and mc.Mov_id = m.Mov_id and m.Mov_year>2015);

/* 4  (having is optional same result)*/
select m.Mov_title, max(r.Rev_stars) 
from MOVIES m,RATING r
where m.Mov_id = r.Mov_id 
group by m.Mov_title 
having count(*) >= 1
order by m.Mov_title;

/* 5. ss=Steven Spielberg */ 
update RATING set rev_stars=5
where mov_id in (select m.mov_id from MOVIES m, DIRECTOR d where m.dir_id = d.dir_id and d.dir_name='ss');
/* OR */
update RATING r,MOVIES m,DIRECTOR d SET r.Rev_stars = 5
where r.Mov_id = m.Mov_id and m.Dir_id = d.Dir_id and d.Dir_Name = 'ss';

select * from RATING;    
    """)

def college():
    print("""
/* ssid semester-section ID ,   SUBJECT = COURSE  */
/* drop database test027_COLLEGE; */
create database test027_COLLEGE;
use test027_COLLEGE;
create table STUDENT
(
	Usn varchar(25),
	Sname varchar(25),
	Address varchar(25),
	Phone bigint,
	Gender varchar(6),
	primary key(Usn)
);
create table SEMSEC
(
	Ssid int,  
	Sem int,
	Sec varchar(1),
	primary key(Ssid)
);
create table CLASS
(
	Usn varchar(25),
	Ssid int,
	primary key(Usn),
	foreign key(Usn) references STUDENT(Usn) on delete cascade,
	foreign  key(Ssid) references SEMSEC(Ssid) on delete cascade
);
create table SUBJECT
(
	Sub_code varchar(25),
	Title varchar(25),
	Sem int,
	Credits int,
	primary key(Sub_code)
);
create table IAMARKS
(
	Usn varchar(25),
	Sub_code varchar(25),
	Ssid int,
	Test1 int,
	Test2 int,
	Test3 int,
	Finalia int,
	primary key(Usn,Sub_code,Ssid),
	foreign key(Usn) references STUDENT(Usn) on delete cascade,
	foreign key(Sub_code) references SUBJECT(Sub_code) on delete cascade,
	foreign key(Ssid) references SEMSEC(Ssid) on delete cascade
);

desc STUDENT;
desc SEMSEC;
desc CLASS;
desc SUBJECT;

insert into STUDENT values
('ai001','a','a',12345,'m'),
('ai002','b','b',23456,'f'),
('ai003','c','c',34567,'m'),
('ai004','d','d',45678,'f');
insert into SEMSEC values
(1,4,'c'),
(2,8,'a'),
(3,8,'b'),
(4,8,'b');
insert into CLASS values
('ai001',1),
('ai002',2),
('ai003',3),
('ai004',4);
insert into SUBJECT values
('41','a',4,1),
('81','b',8,2),
('82','c',8,3);
insert into IAMARKS(Usn,Sub_code,Ssid,Test1,Test2,Test3) values
('ai001','41',1,13,15,19),
('ai002','81',2,16,20,17),
('ai002','82',2,19,17,20),
('ai003','81',3,14,15,18),
('ai003','82',3,17,19,15),
('ai004','81',4,20,16,10),
('ai004','82',4,15,13,10);

select * from STUDENT;
select * from SEMSEC;
select * from CLASS;
select * from SUBJECT;
select * from IAMARKS;

/*  1  (no need of Phone in select )*/
SELECT s.Usn,s.Sname,s.Address,s.Phone,s.Gender
FROM STUDENT s,CLASS c,SEMSEC ss
where s.Usn = c.Usn and c.Ssid = ss.Ssid and ss.Sem = 4 AND ss.Sec = 'c';

/*  2  */
select Sem,Sec,Gender,count(*) as count
from STUDENT s, SEMSEC sc, CLASS c
where s.Usn = c.Usn and sc.Ssid = c.Ssid
group by Sem,Sec,Gender;
/* OR */
SELECT ss.Sem, ss.Sec,
	SUM(CASE WHEN s.Gender = 'M' THEN 1 ELSE 0 END) AS MaleCount,
	SUM(CASE WHEN s.Gender = 'F' THEN 1 ELSE 0 END) AS FemaleCount
FROM STUDENT s,CLASS c,SEMSEC ss
where s.USN = c.USN and c.SSID = ss.SSID
GROUP BY ss.Sem,ss.Sec;

/*  3  */
create view TEST1_MARKS as 
(select Usn,Test1,Sub_code 
from IAMARKS 
where Usn='ai001');

select * from TEST1_MARKS;

/*  4  */
UPDATE IAMARKS
SET Finalai = (CASE
                 WHEN Test1<greatest(Test1,Test2,Test3) AND Test1>least(Test1,Test2,Test3) THEN (greatest(Test1,Test2,Test3)+Test1)/2
                 WHEN Test2<greatest(Test1,Test2,Test3) AND Test2>least(Test1,Test2,Test3) THEN (greatest(Test1,Test2,Test3)+Test2)/2
                 ELSE (greatest(Test1,Test2,Test3)+Test3)/2
               END);
/* OR */
create table AVERAGE_FINDER
(
	select usn,sub_code,greatest(test1,test2,test3) as highest, 
	case
		when test1<greatest(Test1,Test2,Test3) and test1>least(Test1,Test2,Test3) then Test1
		when test2<greatest(Test1,Test2,Test3) and test2>least(Test1,Test2,Test3) then Test2
		else Test3
	end as second_highest from IAMARKS
);
select * from AVERAGE_FINDER;
update IAMARKS i set Finalia = (select (highest+second_highest)/2 from AVERAGE_FINDER
where i.usn=usn and i.sub_code=sub_code);

/*  5  */
select Usn,Sub_code, 
	case
		when Finalia>=17 and Finalia<=20 then 'Outstanding'
		when Finalia>=12 and Finalia<=16 then 'Average'
		when Finalia<12 then 'Weak'
	end as Category 
from IAMARKS
where Usn in (select Usn from SEMSEC sc,CLASS c where sc.Ssid=c.Ssid and Sem=8 and Sec in ('A','B','C'));    
    """)

def company():
    print("""
/* drop database test027_COMPANY; */
create database test027_COMPANY;
use test027_COMPANY;
create table DEPARTMENT
(
	Dno int,
	Dname varchar(25),
	Mgrssn int,
	Mgrstartdate date,
	primary key(Dno)
);
create table EMPLOYEE
(
	Ssn int,
	Name varchar(25),
	Address varchar(25),
	Sex varchar(6),
	Salary int,
	Superssn int,
	Dno int,
	primary key(Ssn)
);
create table DLOCATION
(
	Dno int,
	Dloc varchar(25),
	primary key (Dno,Dloc),
	foreign key(Dno) references DEPARTMENT(Dno) on delete cascade
);
create table PROJECT
(
	Pno int,
	Pname varchar(25),
	Plocation varchar(25),
	Dno int,
	primary key(Pno),
	foreign key(Dno) references DEPARTMENT(Dno) on delete cascade
);
create table WORKS_ON
(
	Ssn int,
	Pno int,
	Hours int,
	primary key(Ssn,Pno),
	foreign key(Ssn) references EMPLOYEE(Ssn) on delete cascade,
	foreign key(Pno) references PROJECT(Pno) on delete cascade
);

desc DEPARTMENT;
desc EMPLOYEE;
desc DLOCATION;
desc PROJECT;
desc WORKS_ON;

insert into DEPARTMENT values
(1,'a',1,'2017-01-01'),
(2,'b',2,'2017-01-02');
insert into EMPLOYEE values
(1,'a scott','a','m',500000,1,1),
(2,'b','b','m',560000,2,2),
(3,'c','c','m',600000,1,1),
(4,'d','d','m',620000,2,2),
(5,'e','e','m',640000,2,2),
(6,'f','f','m',670000,2,2),
(7,'g','g','m',700000,2,2);
insert into DLOCATION values
(1,'a'),
(1,'b'),
(2,'b'),
(2,'c');
insert into PROJECT values
(1,'iot','a',1),
(2,'b','b',2),
(3,'c','c',1),
(4,'d','d',2);
insert into WORKS_ON values
(1,1,9),
(2,1,12),
(3,1,15),
(4,1,18),
(5,1,15),
(6,2,18),
(1,2,12),
(1,4,12);

alter table DEPARTMENT add foreign key(MgrSSN) references EMPLOYEE(SSN) on delete cascade;
alter table EMPLOYEE add foreign key(SuperSSN) references EMPLOYEE(SSN) on delete cascade;
alter table EMPLOYEE add foreign key(DNo) references DEPARTMENT(DNo) on delete cascade;

/*alter table WORKS_ON add foreign key(SSN) references EMPLOYEE(SSN) on delete cascade;
alter table WORKS_ON add foreign key(PNo) references PROJECT(PNo) on delete cascade;
alter table PROJECT add foreign key(DNo) references DEPARTMENT(DNo) on delete cascade;
alter table DLOCATION add foreign key(DNo) references DEPARTMENT(DNo) on delete cascade;*/

select * from DEPARTMENT;
select * from EMPLOYEE;
select * from DLOCATION;
select * from PROJECT;
select * from WORKS_ON;

/*  1  */
select Pno
from PROJECT p,DEPARTMENT d,EMPLOYEE e
where p.Dno = d.Dno and e.Ssn = d.Mgrssn and e.Name LIKE '%scott'
UNION
select Pno
from WORKS_ON w,EMPLOYEE e
where w.Ssn = e.Ssn and e.Name LIKE '%scott';
/*  OR  */
select distinct Pno 
from PROJECT 
where Pno in (select Pno from PROJECT p,DEPARTMENT d,EMPLOYEE e where p.Dno = d.Dno and d.Mgrssn = e.Ssn and Name like '%scott') 
or Pno in (select Pno from WORKS_ON w, EMPLOYEE e where w.Ssn = e.Ssn and Name like '%scott');

/*  2  */
select e.Name, e.Salary * 1.1 AS Newsalary
FROM EMPLOYEE e,WORKS_ON w,PROJECT p
where e.Ssn = w.Ssn and w.Pno = p.Pno and p.Pname = 'ioT';
/*  OR  */
select e.Name, e.Salary*1.1 as new_salary 
from EMPLOYEE e, WORKS_ON w
where e.Ssn = w.Ssn and w.Pno in (select Pno from PROJECT where Pname ='ioT');

/*  3  a = accountant */
select sum(Salary), max(Salary), min(Salary), avg(Salary) 
from EMPLOYEE e,DEPARTMENT d
where d.Dno = e.Dno and d.Dname = 'a';
/*  OR  */
SELECT SUM(e.Salary) AS TotalSalary, MAX(e.Salary) AS MaxSalary, MIN(e.Salary) AS MinSalary, AVG(e.Salary) AS AverageSalary
FROM EMPLOYEE e
JOIN DEPARTMENT d ON e.DNo = d.DNo
WHERE d.DName = 'a';

/*  4  */
select e.Name 
from EMPLOYEE e
where not exists(select Pno from PROJECT where Dno='5' and Pno not in (select Pno from WORKS_ON where e.Ssn=Ssn));
/*  OR  */
SELECT e.Name 
FROM EMPLOYEE e
WHERE NOT EXISTS (SELECT 1 FROM PROJECT p WHERE p.DNo = 5 
AND NOT EXISTS (SELECT 1 FROM WORKS_ON w WHERE w.SSN = e.SSN AND w.PNo = p.PNo));
/*  This is often used as a convenient way to include a subquery in the WHERE clause of a SELECT statement, 
when the subquery itself does not need to return any specific values. */

/*  5  ( > is made as >= )*/
select d.Dno,count(*) as count 
from DEPARTMENT d,EMPLOYEE e
where d.DNo= e.DNo and Salary >600000 and d.DNo in (select DNo from EMPLOYEE group by DNo having count(*)>= 5)
group by d.DNo;    
    """)



def 1library():
    """Consider the following schema for a Library Database:
BOOK(Book_id, Title, Publisher_Name, Pub_Year)
BOOK_AUTHORS(Book_id, Author_Name)
PUBLISHER(Name, Address, Phone)
BOOK_COPIES(Book_id, Branch_id, No-of_Copies)
BOOK_LENDING(Book_id, Branch_id, Card_No, Date_Out, Due_Date)
LIBRARY_BRANCH(Branch_id, Branch_Name, Address)
Write SQL queries to
1. Retrieve details of all books in the library id, title, name of publisher, authors,number of copies in each branch, etc.
2. Get the particulars of borrowers who have borrowed more than 3 books, but from Jan 2017 to Jun 2017.
3. Delete a book in BOOK table. Update the contents of other tables to reflect this data manipulation operation.
4. Partition the BOOK table based on year of publication. Demonstrate its working with a simple query.
5. Create a view of all books and its number of copies that are currently available in the Library. """
    print("""
create table PUBLISHER
(
	Name varchar(10),
	Address varchar(10),
	Phone bigint,
	primary key(Name)
);
create table BOOK
(
	Book_id varchar(5),
	Title varchar(20),
	Publisher_Name varchar(10),
	Publisher_year int,
	primary key(Book_id),
	foreign key(Publisher_Name) references PUBLISHER(Name) on delete cascade
);
create table BOOK_AUTHORS
(
	Book_id varchar(5),
	Author_name varchar(15),
	primary key(Book_id),
	foreign key(Book_id) references BOOK(Book_id) on delete cascade
);
create table LIBRARY_BRANCH
(
	Branch_id varchar(5),
	Branch_name varchar(10),
	Address varchar(15),
	primary key(Branch_id)

);
create table BOOK_COPIES
(
	Book_id varchar(5),
	Branch_id varchar(5),
	No_of_copies int,
	primary key(Book_id,Branch_id),
	foreign key(Book_id) references BOOK(Book_id) on delete cascade,
	foreign key(Branch_id) references LIBRARY_BRANCH(Branch_id) on delete cascade
);
create table BOOK_LENDING
(
	Book_id varchar(5),
	Branch_id varchar(5),
	Card_no varchar(5),
	Date_out date,
	Due_date date,
	primary key(Book_id,Branch_id,Card_no),
	foreign key(Book_id) references BOOK(Book_id) on delete cascade,
	foreign key(Branch_id) references LIBRARY_BRANCH(Branch_id) on delete cascade
);

insert into PUBLISHER values('mcgraw','bangalore','9191919191'),('pearson','newdelhi','8181818181'),('planeta','bangalore','5151515151'),('livre','chennai','6161616161');

insert into BOOK values('1','ME','mcgraw','2001'),('2','PP','mcgraw','2001'),('3','DBMS','pearson','2009'),('4','ATC','planeta','2009'),('5','AI','pearson','2014');

insert into BOOK_AUTHORS values('1','navathe'),('2','navathe'),('3','edward'),('4','galvin'),('5','angel');

insert into LIBRARY_BRANCH values('11','RNSIT','bangalore'),('12','VTU','bangalore'),('13','NITTE','bangalore'),('14','MANIPAL','mangalore'),('15','VCET','udupi');

insert into BOOK_COPIES values('1','11',10),('1','13',20),('1','14',15),('2','11',9),('2','12',10),('2','13',5),('3','12',4),('4','14',3),('5','11',7);

insert into BOOK_LENDING values('5','11','101','2017-03-11','2017-05-10'),('3','14','102','2017-01-14','2017-04-04'),('4','12','105','2017-04-16','2017-06-07'),('1','12','103','2017-01-01','2017-06-11'),('2','11','103','2017-01-11','2017-06-10'),('3','15','103','2017-01-15','2017-06-15'),('4','14','103','2017-02-21','2017-06-20'),('3','15','104','2017-01-01','2017-06-20'),('4','11','104','2017-01-02','2017-06-21'),('2','11','104','2017-01-20','2017-05-18');

desc PUBLISHER;
desc BOOK;
desc BOOK_AUTHORS;
desc LIBRARY_BRANCH;
desc BOOK_COPIES;
desc BOOK_LENDING;

select * from PUBLISHER;
select * from BOOK;
select * from BOOK_AUTHORS;
select * from LIBRARY_BRANCH;
select * from BOOK_COPIES;
select * from BOOK_LENDING;

/* queries 1 -- Retrieve details of all books in the library - id, title, name of publisher, authors, number of copies 
in each branch, etc.*/

select B.Book_id, B.Title, B.Publisher_Name, BA.Author_name,BC.Branch_id,BC.No_of_copies
from BOOK B, BOOK_AUTHORS BA, BOOK_COPIES BC
where B.Book_id = BC.Book_id
and B.Book_id = BA.Book_id ;

/* queries 2 -- Get the particulars of borrowers who have borrowed more than 3 books, but from Jan 2017 to Jun
2017 */

select Card_no
from BOOK_LENDING B
where Date_out between '2017-01-01' and '2017-06-30'
group by card_no
having count(*)>3 ;

/* queries 3 -- Delete a book in BOOK table. Update the contents of other tables to reflect this data 
manipulation operation. */

delete from BOOK where Book_id='1';
select * from BOOK;

/* queries 4 -- Partition the BOOK table based on year of publication. Demonstrate its working with a simple
query. */

create view V_PUBLICATION as
select Publisher_year from BOOK;
select * from V_PUBLICATION;

/* queries 5 -- create a view of all books and its number of copies that are currently available in the library. */

create view available as
(
	select Book_id, sum(No_of_copies) - (select count(Card_no)
	from BOOK_LENDING
	where B.Book_id = Book_id) as avail_copies
	from BOOK_COPIES B
	group by Book_id
);
select * from available;

/* queries 4 alternative college */
create table BOOK1
(
	Book_id varchar(5),
	Title varchar(20),
	Publisher_Name varchar(10),
	Publisher_year int,
	primary key(Book_id,Publisher_year)
)
partition by range(Publisher_year)
(
	partition p1 values less than (2002), 
	partition p2 values less than (2010),
	partition p3 values less than (maxvalue)
);

insert into BOOK1 values('1','ME','mcgraw','2001'),('2','PP','mcgraw','2001'),('3','DBMS','pearson','2009'),('4','ATC','planeta','2009'),('5','AI','pearson','2014');

select * from BOOK1 partition(p1);
select * from BOOK1 partition(p2);
select * from BOOK1 partition(p3);
     """)



def 2order():
    """ Consider the following schema for Order Database: 
    SALESMAN(Salesman_id, Name, City, Commission) 
    CUSTOMER(Customer_id, Cust_Name, City, Grade, Salesman_id) 
    ORDERS(Ord_No, Purchase_Amt, Ord_Date, Customer_id, Salesman_id)
Write SQL queries to
1. Count the customers with grades above Bangalore's average.
2. Find the name and numbers of all salesman who had more than one customer.
3. List all the salesman and indicate those who have and don't have customers in their cities (Use UNION operation.)
4. Create a view that finds the salesman who has the customer with the highest order of a day.
5. Demonstrate the DELETE operation by removing salesman with id 1000. All his orders must also be deleted."""
    print("""
create table SALESMAN
(
	Salesman_id varchar(5), 
	Name varchar(15),
	City varchar(15), 
	Commission int,
	primary key(Salesman_id)
);
create table CUSTOMER
(
	Customer_id varchar(5), 
	Cust_name varchar(15), 
	City varchar(15), 
	Grade int,
	Salesman_id varchar(5), 
	primary key(Customer_id),
	foreign key(Salesman_id) references SALESMAN(Salesman_id) on delete cascade
);
create table ORDERS
(
	Ord_no varchar(5), 
	Purchase_amt int,
	Ord_date date, 
	Customer_id varchar(5), 
	Salesman_id varchar(5), 
	primary key(Ord_no),
	foreign key(Customer_id) references CUSTOMER(Customer_id) on delete cascade, 
	foreign key(Salesman_id) references SALESMAN(Salesman_id) on delete cascade
);

insert into SALESMAN values(1,'gimmi','Mangalore',5),(2,'Ravi','Bangalore',3),(3,'gagan','Hubli',3),(4,'Sagar','Bangalore',3),(5,'Raj','Mangalore',4);

insert into CUSTOMER values('C11','Srikanth','Bangalore',4,'2'),('C12','Sandeep','Mangalore',2,'3'),('C13','Uday','Bangalore',3,'2'),('C14','Mahesh','Hubli',2,'2'),('C15','Shivaram','Bangalore',2,'3'),('C16','Shyam','Mangalore',5,'1'),('C17','Sumith','Udupi',4,'5'),('C18','Shravan','Bangalore',3,'4');

insert into ORDERS values('111',2500,'2017-07-11','C11','2'),('112',1999,'2017-07-09','C12','3'),('113',999,'2017-07-12','C13','2'),('114',9999,'2017-07-12','C14','2'),('115',7999,'2017-07-11','C15','3'),('116',1099,'2017-07-09','C16','1');

desc SALESMAN;
desc CUSTOMER;
desc ORDERS;

select * from SALESMAN;
select * from CUSTOMER;
select * from ORDERS;

/* 1 Count the customers with grades above Bangalore's average.  */

select count(*) as Count
from CUSTOMER where Grade > (select avg(Grade) from CUSTOMER where City='Bangalore');

/* 2 Find the name and numbers of all salesman who had more than one customer. */

select s.Salesman_id, s.Name, count(Customer_id)
from SALESMAN s, CUSTOMER c
where s.Salesman_id = c.Salesman_id
group by s.Salesman_id, s.Name 
having count(Customer_id)>1;

/* 3 List all the salesman and indicate those who have and don't have customers in their cities (Use UNION operation.) */

select Name,'exists' as Same_city 
from SALESMAN s 
where city in (select city from CUSTOMER where s.Salesman_id= Salesman_id) 
union 
select Name,'not exists' as Same_city 
from SALESMAN s 
where city not in (select city from CUSTOMER where s.Salesman_id = Salesman_id);

/* 4 create a view that finds the salesman who has the customer with the highest order of a day */
 
create view Highest_order as 
select s.Salesman_id,s.Name,o.Purchase_amt,o.Ord_date
from SALESMAN s,ORDERS o
where s.Salesman_id = o.Salesman_id;
select Name,Ord_date
from Highest_order h
where Purchase_amt = (select max(Purchase_amt) from Highest_order where h.Ord_date = Ord_date);

/* 5 demonstrate the delete operation by removing salesman with id 1000 All his order musst also be deleted */

delete from SALESMAN where Salesman_id=3;

    """)





def 3movie():
    """Consider the schema for Movie Database:
ACTOR(Act_id, Act_Name, Act_Gender) DIRECTOR(Dir_id, Dir_Name, Dir_Phone) MOVIES(Mov_id, Mov_Title, Mov_Year, Mov_Lang, Dir_id) MOVIE_CAST(Act_id, Mov_id, Role)
RATING(Mov_id, Rev_Stars)
Write SQL queries to
1. List the titles of all movies directed by 'Hitchcock'.
2. Find the movie names where one or more actors acted in two or more movies.
3. List all actors who acted in a movie before 2000 and also in a movie after 2015 (use JOIN operation).
4. Find the title of movies and number of stars for each movie that has at least one rating and find the highest number of stars that movie received. Sort the result by movie title.
5. Update rating of all movies directed by 'Steven Spielberg' to 5.
"""
    print("""
create table ACTOR
(
	act_id varchar(5),
	act_name varchar(15),
	act_gender varchar(6),
	primary key(act_id)
);
create table DIRECTOR
(
	dir_id varchar(5),
	dir_name varchar(15),
	dir_phone bigint,
	primary key(dir_id)
);
create table MOVIES
(
	mov_id varchar(5),
	mov_title varchar(20),
	mov_year int,
	mov_lang varchar(10),
	dir_id varchar(5),
	primary key(mov_id),
	foreign key(dir_id) references DIRECTOR(dir_id) on delete cascade
);
create table MOVIE_CAST
(
	act_id varchar(5),
	mov_id varchar(5),
	role varchar(10),
	primary key(act_id,mov_id),
	foreign key(act_id) references ACTOR(act_id) on delete cascade,
	foreign key(mov_id) references MOVIES(mov_id) on delete cascade
);
create table RATING
(
	rat_id varchar(5),
	mov_id varchar(5),
	rev_stars int,
	primary key(rat_id),
	foreign key(mov_id) references MOVIES(mov_id) on delete cascade
);

insert into ACTOR values('A101','Rajgopal','M'),('A102','john','M'),('A103','Lepord','M'),('A104','Sarukhan','F'),('A105','lilly','F'),('A106','rocky','M'),('A107','Harrian','M');

insert into DIRECTOR values('D01','Hitchcock',9757563322),('D02','Steven',9342401533),('D03','Rajaram',1234758965),('D04','Nagraj',9342400533),('D05','kalyan',9938732432);

insert into MOVIES values('M10','kill bill',1960,'english','D01'),('M11','how it is',2017,'english','D04'),('M12','crime',1999,'english','D04'),('M13','doom3',1984,'english','D02'),('M14','hello',2016,'english','D04'),('M15','doctor',1982,'english','D02');

insert into MOVIE_CAST values('A101','M11','f_lead'),('A104','M11','supporting'),('A101','M12','f_lead'),('A106','M10','negative'),('A107','M13','m_lead'),('A104','M14','negative'),('A107','M14','supporting');

insert into RATING values('R1','M11',3),('R2','M10',4),('R3','M11',4),('R4','M12',4),('R5','M13',4),('R6','M15',3),('R7','M13',3);

desc ACTOR;
desc DIRECTOR;
desc MOVIES;
desc MOVIE_CAST;
desc RATING;

select * from ACTOR;
select * from DIRECTOR;
select * from MOVIES;
select * from MOVIE_CAST;
select * from RATING;

/* 1 list the titles of all movies directed by 'Hitchcock' */

select mov_title from MOVIES m,DIRECTOR d where m.dir_id=d.dir_id and d.dir_name='Hitchcock';

/* 2 find the movie names where one or more actors acted in 2 or more movies  */

select distinct mov_title from MOVIES m,MOVIE_CAST mc
where m.mov_id = mc.mov_id and (select count(mov_id) from MOVIE_CAST where act_id=mc.act_id)>=2;

/* 3 List all actors who acted in a movie before 2000 and also in a movie after 2015 join operation*/

select act_name from ACTOR a join MOVIE_CAST mc on a.act_id = mc.act_id join MOVIES m
on mc.mov_id = m.mov_id
where m.mov_year<2000 and act_name in (select act_name
from ACTOR a join MOVIE_CAST mc on a.act_id = mc.act_id join MOVIES m
on mc.mov_id = m.mov_id
where m.mov_year>2015);

/* 4 Find the title of movies and number of stars for each movie that has at least one rating and findthe highest number of stars that movie received. Sort the result by movie title. */

select mov_title, max(rev_stars) from MOVIES m, RATING r
where m.mov_id = r.mov_id group by m.mov_title order by m.mov_title;

/* 5. Update rating of all movies directed by 'Steven Spielberg' to 5 */ 

select * from RATING;

update RATING set rev_stars=5
where mov_id in (select m.mov_id from MOVIES m, DIRECTOR d where m.dir_id = d.dir_id and d.dir_name='Steven');

select * from RATING;

    """)




def 4college():
    """Consider the schema for College Database:
STUDENT(USN, SName, Address, Phone, Gender) SEMSEC(SSID, Sem, Sec)
CLASS(USN, SSID)
COURSE(Subcode, Title, Sem, Credits)
IAMARKS(USN, Subcode, SSID, Test1, Test2, Test3, FinalIA)
Write SQL queries to
1. List all the student details studying in fourth semester 'C' section.
2. Compute the total number of male and female students in each semester and in each section.
3. Create a view of Test1 marks of student USN '1BI15CS101' in all Courses.
4. Calculate the FinalIA (average of best two test marks) and update the corresponding table for all students.
5. Categorize students based on the following criterion: If FinalIA = 17 to 20 then CAT = 'Outstanding'
If FinalIA = 12 to 16 then CAT = 'Average' If FinalIA< 12 then CAT = 'Weak'
Give these details only for 8 th semester A, B, and C section students.
"""
    print("""
create table STUDENT
(
	usn varchar(10),
	sname varchar(15),
	address varchar(15),
	phone bigint,
	gender varchar(6),
	primary key(usn)
);
create table SEMSEC
(
	ssid varchar(5),
	sem int,
	sec varchar(1),
	primary key(ssid)
);
create table CLASS
(
	usn varchar(10),
	ssid varchar(5),
	primary key(usn),
	foreign key(usn) references STUDENT(usn) on delete cascade,
	foreign  key(ssid) references SEMSEC(ssid) on delete cascade
);
create table COURSE
(
	sub_code varchar(7),
	title varchar(15),
	sem int,credits int,
	primary key(sub_code)
);
create table IAMARKS
(
	usn varchar(10),
	sub_code varchar(7),
	ssid varchar(5),
	test1 int,
	test2 int,
	test3 int,
	finalia int,
	primary key(usn,sub_code,ssid),
	foreign key(usn) references STUDENT(usn) on delete cascade,
	foreign key(sub_code) references COURSE(sub_code) on delete cascade,
	foreign key(ssid) references SEMSEC(ssid) on delete cascade
);

insert into STUDENT values('4vp20ai100','vibav','kolkatta',9860054119,'f'),('4vp20ai101','ratan','viratpet',9762514991,'m'),('4vp20ai102','kshama','karwar',9000876129,'f'),('4vp20ai103','raghav','puttur',9900967408,'m'),('4vp20ai104','raj','bangalore',9973334422,'m'),('4vp20ai105','abhi','puttur',9989086125,'m');

insert into SEMSEC values('S01',1,'A'),('S04',4,'A'),('S05',4,'C'),('S06',8,'A'),('S07',8,'B'),('S08',8,'C');

insert into CLASS values('4vp20ai100','S04'),('4vp20ai101','S05'),('4vp20ai102','S01'),('4vp20ai103','S06'),('4vp20ai104','S07'),('4vp20ai105','S08');

insert into COURSE values('18cs14','DSA',1,4),('18cs41','Maths',4,3),('18cs43','microcontrooler',4,4),('18cs81','c++',8,4),('18cs82','Networks',8,4),('18cs83','DBMS',18,3);

insert into IAMARKS values('4vp20ai100','18cs41','S05',19,18,20,NULL),('4vp20ai101','18cs43','S04',15,18,19,NULL),('4vp20ai101','18cs41','S04',15,17,14,NULL),('4vp20ai102','18cs14','S01',10,11,8,NULL);,('4vp20ai103','18cs14','S01',13,17,15,NULL),('4vp20ai104','18cs81','S08',13,17,19,NULL),('4vp20ai104','18cs82','S06',12,09,10,NULL),('4vp20ai105','18cs81','S07',19,17,16,NULL),('4vp20ai105','18cs83','S08',19,17,18,NULL);

desc STUDENT;
desc SEMSEC;
desc CLASS;
desc COURSE;
desc IAMARKS;

select * from STUDENT;
select * from SEMSEC;
select * from CLASS;
select * from COURSE;
select * from IAMARKS;

/* 1. List all the student details studying in fourth semester 'C' section. */

select s.usn,sname,address,gender 
from STUDENT s,SEMSEC sc,CLASS c 
where s.usn=c.usn and sc.ssid=c.ssid and sc.sem=4 and sc.sec='C';

/* 2. Compute the total number of male and female students in each semester and in each section. */

select sem, sec, gender, count(*) as count
from STUDENT s, SEMSEC sc, CLASS c
where s.usn = c.usn and sc.ssid = c.ssid
group by sem, sec, gender;

/* 3. Create a view of Test1 marks of student USN '1BI15CS101' in all subjects. */

create view TEST1_MARKS as(select usn,test1,sub_code from IAMARKS where usn='4vp20ai101');

select * from TEST1_MARKS;

/* 4. Calculate the FinalIA (average of best two test marks) and update the corresponding table for all students.*/

create table AVERAGE_FINDER
(
select usn,sub_code,greatest(test1,test2,test3) as highest, 
case
when test1<greatest(test1,test2,test3) and test1>least(test1,test2,test3) then test1
when test2<greatest(test1,test2,test3) and test2>least(test1,test2,test3) then test2
else test3
end as second_highest from IAMARKS
);

select * from AVERAGE_FINDER;

update IAMARKS i set finalia = (select (highest+second_highest)/2 from AVERAGE_FINDER
where i.usn=usn and i.sub_code=sub_code);

select * from IAMARKS;

/*
 5. Categorize students based on the following criterion:
If FinalIA = 17 to 20 then CAT = 'Outstanding'
If FinalIA = 12 to 16 then CAT = 'Average'
If FinalIA< 12 then CAT = 'Weak'
Give these details only for 8 th semester A, B, and C section students.
 */
 
select usn,sub_code, 
case
when finalia>=17 and finalia<=20 then 'Outstanding'
when finalia>=12 and finalia<=16 then 'Average'
when finalia<12 then 'Weak'
end as category
from IAMARKS
where usn in (select usn from SEMSEC sc,CLASS c where sc.ssid=c.ssid and sem=8 and sec in ('A','B','C'));

    """)



def 5company():
    """ Consider the schema for Company Database:
EMPLOYEE(SSN, Name, Address, Sex, Salary, SuperSSN, DNo) DEPARTMENT(DNo, DName, MgrSSN, MgrStartDate) DLOCATION(DNo, DLoc)
PROJECT(PNo, PName, PLocation, DNo) WORKS_ON(SSN, PNo, Hours)
Write SQL queries to
1. Make a list of all project numbers for projects that involve an employee whose last name is 'Scott', either as a worker or as a manager of the department that controls the project.
2. Show the resulting salaries if every employee working on the 'IoT' project is given a 10 percent raise.
3. Find the sum of the salaries of all employees of the 'Accounts' department, as well as the maximum salary, the minimum salary, and the average salary in this department
4. Retrieve the name of each employee who works on all the projects controlled by department number 5 (use NOT EXISTS operator).
5. For each department that has more than five employees, retrieve the department number and the number of its employees who are making more than Rs. 6,00,000.
"""
    print("""
create table DEPARTMENT
(
	DNo varchar(5),
	DName varchar(15),
	MgrSSN varchar(5),
	MgrStartDate date,
	primary key(DNo)
);
create table EMPLOYEE
(
	SSN varchar(5),
	Name varchar(15),
	Address varchar(15),
	Sex varchar(6),
	Salary int,
	SuperSSN varchar(5),
	DNo varchar(5),
	primary key(SSN)
);

create table DLOCATION
(
	DNo varchar(5),
	DLoc varchar(15),
	primary key (DNo,DLoc)
);
create table PROJECT
(
	PNo varchar(5),
	PName varchar(10),
	PLocation varchar(10),
	DNo varchar(5),
	primary key(PNo)
);
create table WORKS_ON
(
	SSN varchar(5),
	PNo varchar(5),
	Hours int,
	primary key(SSN,PNo)
);

insert into DEPARTMENT values('1','Account','E107','2015-01-10');
insert into DEPARTMENT values('2','Research','E103','2016-07-13');
insert into DEPARTMENT values('3','Administration','E102','2017-07-20');
insert into DEPARTMENT values('4','Headquarters','E104','2016-08-16');
insert into DEPARTMENT values('5','Marketing','E106','2016-04-16');

insert into EMPLOYEE values('E101','Allan Scott','Bengaluru','m',500000,'E103','3');
insert into EMPLOYEE values('E102','Kishore','Bengaluru','m',620000,NULL,'1');
insert into EMPLOYEE values('E103','Jimmy Scott','Mumbai','m',630000,NULL,'2');
insert into EMPLOYEE values('E104','Leo','Delhi','m',650000,'E107','3');
insert into EMPLOYEE values('E105','Joseph','Bengaluru','m',500000,'E102','3');
insert into EMPLOYEE values('E106','Somashekhar','Chennai','m',550000,'E107','3');
insert into EMPLOYEE values('E107','Rajkumar','Bengaluru','m',700000,NULL,'1');
insert into EMPLOYEE values('E108','Kajal','Delhi','f',650000,NULL,'3');
insert into EMPLOYEE values('E109','Smrithi','Bengaluru','f',620000,'E108','3');

insert into DLOCATION values('1','Bengaluru');
insert into DLOCATION values('2','Bengaluru');
insert into DLOCATION values('3','Chennai');
insert into DLOCATION values('4','Hyderabad');
insert into DLOCATION values('5','Bengaluru');
insert into DLOCATION values('3','Bengaluru');

insert into PROJECT values('P1','IoT','Bengaluru','5');
insert into PROJECT values('P2','Android','Bengaluru','5');
insert into PROJECT values('P3','Web','Chennai','3');
insert into PROJECT values('P4','HTML','Hyderabad','2');
insert into PROJECT values('P5','Medical','Hyderabad','2');

insert into WORKS_ON values('E101','P1',5);
insert into WORKS_ON values('E104','P1',6);
insert into WORKS_ON values('E108','P1',7);
insert into WORKS_ON values('E105','P3',6);
insert into WORKS_ON values('E105','P1',4);
insert into WORKS_ON values('E104','P2',5);

alter table DEPARTMENT add foreign key(MgrSSN) references EMPLOYEE(SSN) on delete cascade;
alter table EMPLOYEE add foreign key(SuperSSN) references EMPLOYEE(SSN) on delete cascade;
alter table EMPLOYEE add foreign key(DNo) references DEPARTMENT(DNo) on delete cascade;
alter table WORKS_ON add foreign key(SSN) references EMPLOYEE(SSN) on delete cascade;
alter table WORKS_ON add foreign key(PNo) references PROJECT(PNo) on delete cascade;
alter table PROJECT add foreign key(DNo) references DEPARTMENT(DNo) on delete cascade;
alter table DLOCATION add foreign key(DNo) references DEPARTMENT(DNo) on delete cascade;


select * from DEPARTMENT;
select * from EMPLOYEE;
select * from DLOCATION;
select * from PROJECT;
select * from WORKS_ON;

/* 1. Make a list of all project numbers for projects that involve an employee whose last name is 'Scott',
 either as a worker or as a manager of the department that controls the project.
*/

select distinct PNo from PROJECT where PNo in (select PNo
from PROJECT p,DEPARTMENT d,EMPLOYEE e 
where p.DNo = d.DNo and d.MgrSSN = e.SSN and Name like '%Scott') or PNo in
(select PNo from WORKS_ON w, EMPLOYEE e
where w.SSN = e.SSN and Name like '%Scott');

/*		OOORRRR
select distinct P.PNo from PROJECT P, DEPARTMENT D, EMPLOYEE E
where E.DNo=D.DNo and D.MgrSSN=E.SSN and E.Name like '%Scott'
UNION
select distinct P1.PNo from PROJECT P1, WORKS_ON W, EMPLOYEE E1
where P1.PNo=W.PNo and E1.SSN=W.SSN and E1.Name like '%Scott';
*/

/* 2. Show the resulting salaries if every employee working on the 'IoT' PROJECT is given a 10 percent raise. */

select e.Name, e.Salary*1.1 as new_salary from EMPLOYEE e, WORKS_ON w
where e.SSN = w.SSN and w.PNo in (select PNo from PROJECT where PName ='IoT');

/* ORRR
SELECT E.Name, 1.1*E.Salary AS INCR_SAL
FROM EMPLOYEE E, WORKS_ON W, PROJECT P
WHERE E.SSN=W.SSN
AND W.PNo=P.PNo
AND P.PName='IoT';
*/

/* 3. Find the sum of the salaries of all employees of the 'Accounts' department, as well 
as the maximum salary, the minimum salary, and the average salary in this department.*/


select sum(Salary), max(Salary), min(Salary), avg(Salary) 
from (EMPLOYEE e join DEPARTMENT d on d.DNo = e.DNo) where d.DName = 'Account';

/* 4. Retrieve the name of each employee who works on all the projects controlledby 
department number 5 (use NOT EXISTS operator).*/

select e.Name from EMPLOYEE e
where not exists(select PNo from PROJECT where DNo='5' and PNo not in (select PNo from WORKS_ON
where e.SSN=SSN));

/*   lab manual
select Name from EMPLOYEE e
where not exists ((select PNo from PROJECT where DNo=5) minus (select PNo from WORKS_ON where SSN = e.SSN));
*/

/* 5. For each department that has more than five employees, retrieve the department number and 
the number of its employees who are making more than Rs.6,00,000. */

select d.DNo,count(*) as count from DEPARTMENT d,EMPLOYEE e
where d.DNo= e.DNo and Salary >600000 and d.DNo in
(select DNo from EMPLOYEE
group by DNo having count(*)>5) group by d.DNo;

    """)

def g_library():
	print("""
--Create Table PUBLISHER with Primary Key as NAME

CREATE TABLE PUBLISHER
(NAME VARCHAR(20) PRIMARY KEY,
PHONE INTEGER,
ADDRESS VARCHAR(20));

DESC PUBLISHER;

--Create Table BOOK with Primary Key as BOOK_ID and Foreign Key PUB_NAME referring the PUBLISHER table

CREATE TABLE BOOK
(BOOK_ID INTEGER PRIMARY KEY,
TITLE VARCHAR(20),
PUB_YEAR VARCHAR(20),
PUB_NAME VARCHAR(20),
FOREIGN KEY (PUB_NAME) REFERENCES PUBLISHER(NAME) ON DELETE CASCADE);


DESC BOOK;

--Create Table BOOK_AUTHORS with Primary Key as BOOK_ID and AUTHOR_NAME and Foreign Key BOOK_ID referring the BOOK table

CREATE TABLE BOOK_AUTHORS
(AUTHOR_NAME VARCHAR(20),
BOOK_ID INTEGER,
FOREIGN KEY (BOOK_ID) REFERENCES BOOK(BOOK_ID) ON DELETE CASCADE,
PRIMARY KEY(BOOK_ID, AUTHOR_NAME));

DESC BOOK_AUTHORS;

--Create Table LIBRARY_PROGRAMME with Primary Key as PROGRAMME_ID

CREATE TABLE LIBRARY_PROGRAMME
(PROGRAMME_ID INTEGER PRIMARY KEY,
PROGRAMME_NAME VARCHAR(50),
ADDRESS VARCHAR(50));

DESC LIBRARY_PROGRAMME;

--Create Table as BOOK_COPIES with Primary Key as BOOK_ID and PROGRAMME_ID and Foreign Key BOOK_ID and PROGRAMME_ID referring the BOOK and LIBRARY_PROGRAMME tables respectively

CREATE TABLE BOOK_COPIES
(NO_OF_COPIES INTEGER,
BOOK_ID INTEGER,
PROGRAMME_ID INTEGER,
FOREIGN KEY (BOOK_ID) REFERENCES BOOK(BOOK_ID) ON DELETE CASCADE,
FOREIGN KEY(PROGRAMME_ID) REFERENCES LIBRARY_PROGRAMME(PROGRAMME_ID) ON DELETE CASCADE,
PRIMARY KEY (BOOK_ID,PROGRAMME_ID));

DESC BOOK_COPIES;

-- Create Table CARD with Primary Key as CARD_NO

CREATE TABLE CARD
(CARD_NO INTEGER PRIMARY KEY);

DESC CARD;

-- Create Table BOOK_LENDING With Primary Key as BOOK_ID, PROGRAMME_ID and CARD_NO and Foreign key as BOOK_ID, PROGRAMME_ID and CARD_NO referring the BOOK, LIBRARY_PROGRAMME and CARD tables respectively

CREATE TABLE BOOK_LENDING
(BOOK_ID INTEGER,
PROGRAMME_ID INTEGER,
CARD_NO INTEGER,
DATE_OUT DATE,
DUE_DATE DATE,
FOREIGN KEY (BOOK_ID) REFERENCES BOOK(BOOK_ID) ON DELETE CASCADE,
FOREIGN KEY (PROGRAMME_ID) REFERENCES LIBRARY_PROGRAMME(PROGRAMME_ID) ON DELETE CASCADE,
FOREIGN KEY (CARD_NO) REFERENCES CARD(CARD_NO) ON DELETE CASCADE,
PRIMARY KEY (BOOK_ID,PROGRAMME_ID,CARD_NO));

DESC BOOKLENDING;

--Inserting records into PUBLISHER table

INSERT INTO PUBLISHER VALUES('SAPNA',912121212,'BANGALORE');
INSERT INTO PUBLISHER VALUES('PENGUIN',921212121,'NEW YORK');
INSERT INTO PUBLISHER VALUES('PEARSON',913131313,'HYDERABAD');
INSERT INTO PUBLISHER VALUES('OZONE',931313131,'CHENNAI');
INSERT INTO PUBLISHER VALUES('PLANETZ',914141414,'BANGALORE');

SELECT * FROM PUBLISHER;

--------------------------

--Inserting records into BOOK table

INSERT INTO BOOK VALUES(1,'BASICS OF EXCEL','JAN-2017','SAPNA');
INSERT INTO BOOK VALUES(2,'PROGRAMMING MINDSET','JUN-2018','PLANETZ');
INSERT INTO BOOK VALUES(3,'BASICS OF SQL','SEP-2016','PEARSON');
INSERT INTO BOOK VALUES(4,'DBMS FOR BEGINNERS','SEP-2015','PLANETZ');
INSERT INTO BOOK VALUES(5,'WEB SERVICES','MAY-2017','OZONE');

SELECT * FROM BOOK;

--------------------------

--Inserting records into BOOK_AUTHORS table

INSERT INTO BOOK_AUTHORS VALUES('SRI DEVI',1);
INSERT INTO BOOK_AUTHORS VALUES('DEEPAK',2);
INSERT INTO BOOK_AUTHORS VALUES('PRAMOD',3);
INSERT INTO BOOK_AUTHORS VALUES('SWATHI',4);
INSERT INTO BOOK_AUTHORS VALUES('PRATHIMA',5);

SELECT * FROM BOOK_AUTHORS;

----------------------------

--Inserting records into LIBRARY_PROGRAMME table

INSERT INTO LIBRARY_PROGRAMME VALUES(100,'HSR LAYOUT','BANGALORE');
INSERT INTO LIBRARY_PROGRAMME VALUES(101,'KENGERI','BANGALORE');
INSERT INTO LIBRARY_PROGRAMME VALUES(102,'BANASHANKARI','BANGALORE');
INSERT INTO LIBRARY_PROGRAMME VALUES(103,'SHANKARA NAGAR','MANGALORE');
INSERT INTO LIBRARY_PROGRAMME VALUES(104,'MANIPAL','UDUPI');

SELECT * FROM LIBRARY_PROGRAMME;

-------------------------

--Inserting records into BOOK_COPIES table

INSERT INTO BOOK_COPIES VALUES(10,1,100);
INSERT INTO BOOK_COPIES VALUES(16,1,101);
INSERT INTO BOOK_COPIES VALUES(20,2,102);
INSERT INTO BOOK_COPIES VALUES(6,2,103);
INSERT INTO BOOK_COPIES VALUES(4,3,104);
INSERT INTO BOOK_COPIES VALUES(7,5,100);
INSERT INTO BOOK_COPIES VALUES(3,4,101);

SELECT * FROM BOOK_COPIES;

--------------------------

--Inserting records into BOOK_COPIES table

INSERT INTO CARD VALUES(500);
INSERT INTO CARD VALUES(501);
INSERT INTO CARD VALUES(502);
INSERT INTO CARD VALUES(503);
INSERT INTO CARD VALUES(504);

SELECT * FROM CARD;

--------------------------

--Inserting records into BOOK_LENDING table

INSERT INTO BOOK_LENDING VALUES(1, 100, 501, '2017-01-01','2017-01-31');
INSERT INTO BOOK_LENDING VALUES(3, 104, 501, '2017-01-11','2017-03-01');
INSERT INTO BOOK_LENDING VALUES(2, 103, 501, '2017-02-21','2017-04-21');
INSERT INTO BOOK_LENDING VALUES(4, 101, 501, '2017-03-11','2017-06-11');
INSERT INTO BOOK_LENDING VALUES(1, 101, 504, '2017-04-09','2017-07-08');

SELECT * FROM BOOK_LENDING;

--------------------------


--Retrieve details of all books in the library – id, title, name of publisher, authors,
--number of copies in each Programme, etc. 

SELECT B.BOOK_ID, B.TITLE, B.PUB_NAME, A.AUTHOR_NAME,C.NO_OF_COPIES,L.PROGRAMME_ID
FROM BOOK B, BOOK_AUTHORS A, BOOK_COPIES C, LIBRARY_PROGRAMME L
WHERE B.BOOK_ID=A.BOOK_ID
AND B.BOOK_ID=C.BOOK_ID
AND L.PROGRAMME_ID=C.PROGRAMME_ID;

---------------------------------------------

--Get the particulars of borrowers who have borrowed more than 3 books, but
--from Jan 2017 to Jun 2017. 

SELECT CARD_NO
FROM BOOK_LENDING
WHERE DATE_OUT BETWEEN '2017-01-01' AND '2017-06-01'
GROUP BY CARD_NO
HAVING COUNT(*)>3;

---------------------------------------------

--Delete a book in BOOK table. Update the contents of other tables to reflect this
--data manipulation operation. 

DELETE FROM BOOK
WHERE BOOK_ID=3; 

SELECT * FROM BOOK;

SELECT * FROM BOOK_AUTHORS;

---------------------------------------------

--Partition the BOOK table based on year of publication. Demonstrate its working
--with a simple query. 

CREATE VIEW V_PUBLICATION AS SELECT
PUB_YEAR
FROM BOOK; 

SELECT * FROM V_PUBLICATION;

---------------------------------------------

--Create a view of all books and its number of copies that are currently available
--in the Library.

CREATE VIEW V_BOOKS AS
SELECT B.BOOK_ID, B.TITLE, C.NO_OF_COPIES
FROM
BOOK B, BOOK_COPIES C, LIBRARY_PROGRAMME L
WHERE B.BOOK_ID=C.BOOK_ID
AND C.PROGRAMME_ID=L.PROGRAMME_ID;

SELECT * FROM V_BOOKS;	
	""")


def g_order():
	print("""
	--Create Table SALESMAN with Primary Key as SALESMAN_ID

CREATE TABLE SALESMAN(
SALESMAN_ID INTEGER PRIMARY KEY,
NAME VARCHAR(20),
CITY VARCHAR(20),
COMMISSION VARCHAR(20));

DESC SALESMAN;

--------------------------------------

--Create Table CUSTOMER with Primary Key as CUSTOMER_ID and Foreign Key SALESMAN_ID referring the SALESMAN table

CREATE TABLE CUSTOMER(
CUSTOMER_ID INTEGER PRIMARY KEY,
CUST_NAME VARCHAR(20),
CITY VARCHAR(20),
GRADE INTEGER,
SALESMAN_ID INTEGER,
FOREIGN KEY (SALESMAN_ID) REFERENCES SALESMAN(SALESMAN_ID) ON DELETE SET NULL);

DESC CUSTOMER;

--------------------------------------

--Create Table ORDERS with Primary Key as ORDER_NO and Foreign Key CUSTOMER_ID and SALESMAN_ID referring the CUSTOMER and SALESMAN tables respectively

CREATE TABLE ORDERS(
ORDER_NO INTEGER PRIMARY KEY,
PURCHASE_AMOUNT DECIMAL(10,2),
ORDER_DATE DATE,
CUSTOMER_ID INTEGER,
SALESMAN_ID INTEGER,
FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID)ON DELETE CASCADE,
FOREIGN KEY (SALESMAN_ID) REFERENCES SALESMAN(SALESMAN_ID) ON DELETE CASCADE);

DESC ORDERS;

--Inserting records into SALESMAN table

INSERT INTO SALESMAN VALUES(1000,'RAHUL','BANGALORE','20%');
INSERT INTO SALESMAN VALUES(2000,'ANKITA','BANGALORE','25%');
INSERT INTO SALESMAN VALUES(3000,'SHARMA','MYSORE','30%');
INSERT INTO SALESMAN VALUES(4000,'ANJALI','DELHI','15%');
INSERT INTO SALESMAN VALUES(5000,'RAJ','HYDERABAD','15%');

SELECT * FROM SALESMAN;

------------------------------------------

--Inserting records into CUSTOMER table

INSERT INTO CUSTOMER VALUES(1,'ADYA','BANGALORE',100,1000);
INSERT INTO CUSTOMER VALUES(2,'BANU','MANGALORE',300,1000);
INSERT INTO CUSTOMER VALUES(3,'CHETHAN','CHENNAI',400,2000);
INSERT INTO CUSTOMER VALUES(4,'DANISH','BANGALORE',200,2000);
INSERT INTO CUSTOMER VALUES(5,'ESHA','BANGALORE',400,3000);

SELECT * FROM CUSTOMER;

------------------------------------------

--Inserting records into ORDERS table

INSERT INTO ORDERS VALUES(201,5000,'2020-06-02',1,1000);
INSERT INTO ORDERS VALUES(202,450,'2020-04-09',1,2000);
INSERT INTO ORDERS VALUES(203,1000,'2020-03-15',3,2000);
INSERT INTO ORDERS VALUES(204,3500,'2020-07-09',4,3000);
INSERT INTO ORDERS VALUES(205,550,'2020-05-05',2,2000);

SELECT * FROM ORDERS;

-- Count the customers with grades above Bangalore's average

SELECT GRADE,COUNT(DISTINCT CUSTOMER_ID)
FROM CUSTOMER
GROUP BY GRADE
HAVING GRADE>(SELECT AVG(GRADE)
FROM CUSTOMER
WHERE CITY='BANGALORE');

----------------------------------

--Find the name and numbers of all salesman who had more than one customer

SELECT SALESMAN_ID, NAME
FROM SALESMAN S
WHERE (SELECT COUNT(*)
FROM CUSTOMER C
WHERE C.SALESMAN_ID=S.SALESMAN_ID) > 1;

----------------------------------

--List all the salesman and indicate those who have and don't have customers in their cities (Use UNION operation.)

SELECT S.SALESMAN_ID, S.NAME, C.CUST_NAME, S.COMMISSION
FROM SALESMAN S, CUSTOMER C
WHERE S.CITY=C.CITY
UNION
SELECT S.SALESMAN_ID,S.NAME,'NO MATCH',S.COMMISSION
FROM SALESMAN S
WHERE CITY NOT IN 
(SELECT CITY
FROM CUSTOMER)
ORDER BY 1 ASC;

-----------------------------------

--Create a view that finds the salesman who has the customer with the highest order of a day.

CREATE VIEW V_SALESMAN AS
SELECT O.ORDER_DATE, S.SALESMAN_ID, S.NAME
FROM SALESMAN S,ORDERS O
WHERE S.SALESMAN_ID = O.SALESMAN_ID
AND O.PURCHASE_AMOUNT= (SELECT MAX(PURCHASE_AMOUNT)
FROM ORDERS C
WHERE C.ORDER_DATE=O.ORDER_DATE);

SELECT * FROM V_SALESMAN;

-----------------------------------

--Demonstrate the DELETE operation by removing salesman with id 1000. All his orders must also be deleted.

DELETE FROM SALESMAN
WHERE SALESMAN_ID=1000;

SELECT * FROM SALESMAN;

SELECT * FROM ORDERS;
	""")

def g_movie():
	print("""

--Create Table ACTOR with Primary Key as ACT_ID

CREATE TABLE ACTOR (
ACT_ID INTEGER PRIMARY KEY,
ACT_NAME VARCHAR(20),
ACT_GENDER CHAR(1));

DESC ACTOR;

----------------------------

--Create Table DIRECTOR with Primary Key as DIR_ID

CREATE TABLE DIRECTOR(
DIR_ID INTEGER PRIMARY KEY,
DIR_NAME VARCHAR(20),
DIR_PHONE INTEGER);

DESC DIRECTOR;

----------------------------

--Create Table MOVIES with Primary Key as MOV_ID and Foreign Key DIR_ID referring DIRECTOR table

CREATE TABLE MOVIES(
MOV_ID INTEGER PRIMARY KEY,
MOV_TITLE VARCHAR(25),
MOV_YEAR INTEGER,
MOV_LANG VARCHAR(15),
DIR_ID INTEGER,
FOREIGN KEY (DIR_ID) REFERENCES DIRECTOR(DIR_ID));

DESC MOVIES;

----------------------------

--Create Table MOVIE_CAST with Primary Key as MOV_ID and ACT_ID and Foreign Key ACT_ID and MOV_ID referring ACTOR and MOVIES tables respectively

CREATE TABLE MOVIE_CAST(
ACT_ID INTEGER,
MOV_ID INTEGER,
ROLE VARCHAR(10),
PRIMARY KEY (ACT_ID,MOV_ID),
FOREIGN KEY (ACT_ID) REFERENCES ACTOR(ACT_ID),
FOREIGN KEY (MOV_ID) REFERENCES MOVIES(MOV_ID));

DESC MOVIE_CAST;

----------------------------

--Create Table RATING with Primary Key as MOV_ID and Foreign Key MOV_ID referring MOVIES table

CREATE TABLE RATING(
MOV_ID INTEGER PRIMARY KEY,
REV_STARS VARCHAR(25),
FOREIGN KEY (MOV_ID) REFERENCES MOVIES(MOV_ID));


DESC RATING;
--Inserting records into ACTOR table

INSERT INTO ACTOR VALUES(101,'RAHUL','M');
INSERT INTO ACTOR VALUES(102,'ANKITHA','F');
INSERT INTO ACTOR VALUES(103,'RADHIKA','F');
INSERT INTO ACTOR VALUES(104,'CHETHAN','M');
INSERT INTO ACTOR VALUES(105,'VIVAN','M');

SELECT * FROM ACTOR;

-----------------------------

--Inserting records into DIRECTOR table

INSERT INTO DIRECTOR VALUES(201,'ANUP',918181818);
INSERT INTO DIRECTOR VALUES(202,'HITCHCOCK',918181812);
INSERT INTO DIRECTOR VALUES(203,'SHASHANK',918181813);
INSERT INTO DIRECTOR VALUES(204,'STEVEN SPIELBERG',918181814);
INSERT INTO DIRECTOR VALUES(205,'ANAND',918181815);

SELECT * FROM DIRECTOR;

------------------------------

--Inserting records into MOVIES table

INSERT INTO MOVIES VALUES(1001,'MANASU',2017,'KANNADA',201);
INSERT INTO MOVIES VALUES(1002,'AAKASHAM',2015,'TELUGU',202);
INSERT INTO MOVIES VALUES(1003,'KALIYONA',2008,'KANNADA',201);
INSERT INTO MOVIES VALUES(1004,'WAR HORSE',2011,'ENGLISH',204);
INSERT INTO MOVIES VALUES(1005,'HOME',2012,'ENGLISH',205);

SELECT * FROM MOVIES;

-----------------------------

--Inserting records into MOVIE_CAST table

INSERT INTO MOVIE_CAST VALUES(101,1002,'HERO');
INSERT INTO MOVIE_CAST VALUES(101,1001,'HERO');
INSERT INTO MOVIE_CAST VALUES(103,1003,'HEROINE');
INSERT INTO MOVIE_CAST VALUES(103,1002,'GUEST');
INSERT INTO MOVIE_CAST VALUES(104,1004,'HERO');

SELECT * FROM MOVIE_CAST;

-----------------------------

--Inserting records into RATING table

INSERT INTO RATING VALUES(1001,4);
INSERT INTO RATING VALUES(1002,2);
INSERT INTO RATING VALUES(1003,5);
INSERT INTO RATING VALUES(1004,4);
INSERT INTO RATING VALUES(1005,3);

SELECT * FROM RATING;


--List the titles of all movies directed by 'Hitchcock'.

SELECT MOV_TITLE
FROM MOVIES
WHERE DIR_ID = (SELECT DIR_ID
FROM DIRECTOR
WHERE DIR_NAME='HITCHCOCK');

---------------------------------

--Find the movie names where one or more actors acted in two or more movies.

SELECT MOV_TITLE
FROM MOVIES M,MOVIE_CAST MC
WHERE M.MOV_ID=MC.MOV_ID AND ACT_ID IN (SELECT ACT_ID
FROM MOVIE_CAST GROUP BY ACT_ID
HAVING COUNT(ACT_ID)>1)
GROUP BY MOV_TITLE
HAVING COUNT(*)>1;

--------------------------------

--List all actors who acted in a movie before 2000 and also in a movie after 2015 (use JOIN operation).

SELECT ACT_NAME
FROM ACTOR A
JOIN MOVIE_CAST C
ON A.ACT_ID=C.ACT_ID
JOIN MOVIES M
ON C.MOV_ID=M.MOV_ID
WHERE M.MOV_YEAR NOT BETWEEN 2000 AND 2015;

--------------------------------

--Find the title of movies and number of stars for each movie that has at least one rating 
--and find the highest number of stars that movie received. Sort the result by
--movie title.

SELECT MOV_TITLE,MAX(REV_STARS)
FROM MOVIES
INNER JOIN RATING USING (MOV_ID)
GROUP BY MOV_TITLE
HAVING MAX(REV_STARS)>0
ORDER BY MOV_TITLE;

---------------------------------

--Update rating of all movies directed by 'Steven Spielberg' to 5.

UPDATE RATING
SET REV_STARS=5
WHERE MOV_ID IN (SELECT MOV_ID FROM MOVIES
WHERE DIR_ID IN (SELECT DIR_ID
FROM DIRECTOR
WHERE DIR_NAME='STEVEN SPIELBERG'));

	""")


def g_college():
	print("""
	--Create table STUDENT with PRIMARY KEY as USN

CREATE TABLE STUDENT(
USN VARCHAR(10) PRIMARY KEY,
SNAME VARCHAR(25),
ADDRESS VARCHAR(25),
PHONE INTEGER,
GENDER CHAR(1));

DESC STUDENT;

-----------------------------------

--Create table SEMSEC with PRIMARY KEY as SSID

CREATE TABLE SEMSEC(
SSID VARCHAR(5) PRIMARY KEY,
SEM INTEGER,
SEC CHAR(1));

DESC SEMSEC;

-----------------------------------

--Create table CLASS with PRIMARY KEY as USN and FOREIGN KEY USN, SSID

CREATE TABLE CLASS(
USN VARCHAR(10) PRIMARY KEY,
SSID VARCHAR(5),
FOREIGN KEY(USN) REFERENCES STUDENT(USN),
FOREIGN KEY(SSID) REFERENCES SEMSEC(SSID));

DESC CLASS;

------------------------------------

--Create table SUBJECT with PRIMARY KEY as SUBCODE

CREATE TABLE SUBJECT(
SUBCODE VARCHAR(8) PRIMARY KEY,
TITLE VARCHAR(20),
SEM INTEGER,
CREDITS INTEGER);

DESC SUBJECT;

--------------------------------------

--Create table IAMARKS with PRIMARY KEY as SUBCODE,USN,SSID and FOREIGN KEY SUBCODE, SSID

CREATE TABLE IAMARKS(
USN VARCHAR(10),
SUBCODE VARCHAR(8),
SSID VARCHAR(5),
TEST1 INTEGER,
TEST2 INTEGER,
TEST3 INTEGER,
FINALIA INTEGER,
PRIMARY KEY(SUBCODE,USN,SSID),
FOREIGN KEY(USN) REFERENCES STUDENT(USN),
FOREIGN KEY(SUBCODE) REFERENCES SUBJECT(SUBCODE),
FOREIGN KEY(SSID) REFERENCES SEMSEC(SSID));

DESC IAMARKS;

--Inserting records into STUDENT table

INSERT INTO STUDENT VALUES ('1BI13CS020','ANAND','BELAGAVI', 1233423,'M');
INSERT INTO STUDENT VALUES ('1BI13CS062','BABIITHA','BENGALURU',43123,'F');
INSERT INTO STUDENT VALUES ('1BI15CS101','CHETHAN','BENGALURU', 534234,'M');
INSERT INTO STUDENT VALUES ('1BI13CS066','DIVYA','MANGALURU',534432,'F');
INSERT INTO STUDENT VALUES ('1BI14CS010','EESHA','BENGALURU', 345456,'F');
INSERT INTO STUDENT VALUES ('1BI14CS032','GANESH','BENGALURU',574532,'M');
INSERT INTO STUDENT VALUES ('1BI14CS025','HARISH','BENGALURU', 235464,'M');
INSERT INTO STUDENT VALUES ('1BI15CS011','ISHA','TUMKUR', 764343,'F');
INSERT INTO STUDENT VALUES ('1BI15CS029','JOEY','DAVANGERE', 235653,'M');
INSERT INTO STUDENT VALUES ('1BI15CS045','KAVYA','BELLARY', 865434,'F');
INSERT INTO STUDENT VALUES ('1BI15CS091','MALINI','MANGALURU',235464,'F');
INSERT INTO STUDENT VALUES ('1BI16CS045','NEEL','KALBURGI', 856453,'M');
INSERT INTO STUDENT VALUES ('1BI16CS088','PARTHA','SHIMOGA', 234546,'M');
INSERT INTO STUDENT VALUES ('1BI16CS122','REEMA','CHIKAMAGALUR', 853333,'F');

SELECT * FROM STUDENT;

------------------------------------

--Inserting records into SEMSEC table

INSERT INTO SEMSEC VALUES ('CSE8A', 8,'A');
INSERT INTO SEMSEC VALUES ('CSE8B', 8,'B');
INSERT INTO SEMSEC VALUES ('CSE8C', 8,'C');
INSERT INTO SEMSEC VALUES ('CSE7A', 7,'A');
INSERT INTO SEMSEC VALUES ('CSE7B', 7,'B');
INSERT INTO SEMSEC VALUES ('CSE7C', 7,'C');
INSERT INTO SEMSEC VALUES ('CSE6A', 6,'A');
INSERT INTO SEMSEC VALUES ('CSE6B', 6,'B');
INSERT INTO SEMSEC VALUES ('CSE6C', 6,'C');
INSERT INTO SEMSEC VALUES ('CSE5A', 5,'A');
INSERT INTO SEMSEC VALUES ('CSE5B', 5,'B');
INSERT INTO SEMSEC VALUES ('CSE5C', 5,'C');
INSERT INTO SEMSEC VALUES ('CSE4A', 4,'A');
INSERT INTO SEMSEC VALUES ('CSE4B', 4,'B');
INSERT INTO SEMSEC VALUES ('CSE4C', 4,'C');
INSERT INTO SEMSEC VALUES ('CSE3A', 3,'A');
INSERT INTO SEMSEC VALUES ('CSE3B', 3,'B');
INSERT INTO SEMSEC VALUES ('CSE3C', 3,'C');
INSERT INTO SEMSEC VALUES ('CSE2A', 2,'A');
INSERT INTO SEMSEC VALUES ('CSE2B', 2,'B');
INSERT INTO SEMSEC VALUES ('CSE2C', 2,'C');
INSERT INTO SEMSEC VALUES ('CSE1A', 1,'A');
INSERT INTO SEMSEC VALUES ('CSE1B', 1,'B');
INSERT INTO SEMSEC VALUES ('CSE1C', 1,'C');

SELECT * FROM SEMSEC;

---------------------------------------

--Inserting records into CLASS table

INSERT INTO CLASS VALUES ('1BI13CS020','CSE8A');
INSERT INTO CLASS VALUES ('1BI13CS062','CSE8A');
INSERT INTO CLASS VALUES ('1BI13CS066','CSE8B');
INSERT INTO CLASS VALUES ('1BI15CS101','CSE8C');
INSERT INTO CLASS VALUES ('1BI14CS010','CSE7A');
INSERT INTO CLASS VALUES ('1BI14CS025','CSE7A');
INSERT INTO CLASS VALUES ('1BI14CS032','CSE7A');
INSERT INTO CLASS VALUES ('1BI15CS011','CSE4A');
INSERT INTO CLASS VALUES ('1BI15CS029','CSE4A');
INSERT INTO CLASS VALUES ('1BI15CS045','CSE4B');
INSERT INTO CLASS VALUES ('1BI15CS091','CSE4C');
INSERT INTO CLASS VALUES ('1BI16CS045','CSE3A');
INSERT INTO CLASS VALUES ('1BI16CS088','CSE3B');
INSERT INTO CLASS VALUES ('1BI16CS122','CSE3C');

SELECT * FROM CLASS;

-------------------------------------

--Inserting records into SUBJECT table

INSERT INTO SUBJECT VALUES ('10CS81','ACA', 8, 4);
INSERT INTO SUBJECT VALUES ('10CS82','SSM', 8, 4);
INSERT INTO SUBJECT VALUES ('10CS83','NM', 8, 4);
INSERT INTO SUBJECT VALUES ('10CS84','CC', 8, 4);
INSERT INTO SUBJECT VALUES ('10CS85','PW', 8, 4);
INSERT INTO SUBJECT VALUES ('10CS71','OOAD', 7, 4);
INSERT INTO SUBJECT VALUES ('10CS72','ECS', 7, 4);
INSERT INTO SUBJECT VALUES ('10CS73','PTW', 7, 4);
INSERT INTO SUBJECT VALUES ('10CS74','DWDM', 7, 4);
INSERT INTO SUBJECT VALUES ('10CS75','JAVA', 7, 4);
INSERT INTO SUBJECT VALUES ('10CS76','SAN', 7, 4);
INSERT INTO SUBJECT VALUES ('15CS51','ME', 5, 4);
INSERT INTO SUBJECT VALUES ('15CS52','CN', 5, 4);
INSERT INTO SUBJECT VALUES ('15CS53','DBMS', 5, 4);
INSERT INTO SUBJECT VALUES ('15CS54','ATC', 5, 4);
INSERT INTO SUBJECT VALUES ('15CS55','JAVA', 5, 3);
INSERT INTO SUBJECT VALUES ('15CS56','AI', 5, 3);
INSERT INTO SUBJECT VALUES ('15CS41','M4', 4, 4);
INSERT INTO SUBJECT VALUES ('15CS42','SE', 4, 4);
INSERT INTO SUBJECT VALUES ('15CS43','DAA', 4, 4);
INSERT INTO SUBJECT VALUES ('15CS44','MPMC', 4, 4);
INSERT INTO SUBJECT VALUES ('15CS45','OOC', 4, 3);
INSERT INTO SUBJECT VALUES ('15CS46','DC', 4, 3);
INSERT INTO SUBJECT VALUES ('15CS31','M3', 3, 4);
INSERT INTO SUBJECT VALUES ('15CS32','ADE', 3, 4);
INSERT INTO SUBJECT VALUES ('15CS33','DSA', 3, 4);
INSERT INTO SUBJECT VALUES ('15CS34','CO', 3, 4);
INSERT INTO SUBJECT VALUES ('15CS35','USP', 3, 3);
INSERT INTO SUBJECT VALUES ('15CS36','DMS', 3, 3);

SELECT * FROM SUBJECT;

----------------------------------------

--Inserting records into IAMARKS table

INSERT INTO IAMARKS (USN, SUBCODE, SSID, TEST1, TEST2, TEST3) VALUES ('1BI15CS101','10CS81','CSE8C', 15, 16, 18);
INSERT INTO IAMARKS (USN, SUBCODE, SSID, TEST1, TEST2, TEST3) VALUES ('1BI15CS101','10CS82','CSE8C', 12, 19, 14);
INSERT INTO IAMARKS (USN, SUBCODE, SSID, TEST1, TEST2, TEST3) VALUES ('1BI15CS101','10CS83','CSE8C', 19, 15, 20);
INSERT INTO IAMARKS (USN, SUBCODE, SSID, TEST1, TEST2, TEST3) VALUES ('1BI15CS101','10CS84','CSE8C', 20, 16, 19);
INSERT INTO IAMARKS (USN, SUBCODE, SSID, TEST1, TEST2, TEST3) VALUES ('1BI15CS101','10CS85','CSE8C', 15, 15, 12);

SELECT * FROM IAMARKS;




--List all the student details studying in fourth semester 'C' section.

SELECT S.*, SS.SEM, SS.SEC
FROM STUDENT S, SEMSEC SS, CLASS C
WHERE S.USN = C.USN AND
SS.SSID = C.SSID AND
SS.SEM = 4 AND SS.SEC='C';

----------------------------------------

--Compute the total number of male and female students in each semester and in each section.

SELECT SS.SEM, SS.SEC, S.GENDER, COUNT(S.GENDER) AS COUNT
FROM STUDENT S, SEMSEC SS, CLASS C
WHERE S.USN = C.USN AND
SS.SSID = C.SSID
GROUP BY SS.SEM, SS.SEC, S.GENDER
ORDER BY SEM;

----------------------------------------

--Create a view of Test1 marks of student USN '1BI15CS101' in all Courses.

CREATE VIEW STUDENT_TEST1_MARKS_V
AS
SELECT TEST1, SUBCODE
FROM IAMARKS
WHERE USN = '1BI15CS101';

SELECT * FROM STUDENT_TEST1_MARKS_V;

----------------------------------------

--Calculate the FinalIA (average of best two test marks) and update the corresponding table for all students.

DELIMITER //
CREATE PROCEDURE AVG_MARKS()
BEGIN
DECLARE C_A INTEGER;
DECLARE C_B INTEGER;
DECLARE C_C INTEGER;
DECLARE C_SUM INTEGER;
DECLARE C_AVG INTEGER;
DECLARE C_USN VARCHAR(10);
DECLARE C_SUBCODE VARCHAR(8);
DECLARE C_SSID VARCHAR(5);

DECLARE C_IAMARKS CURSOR FOR
SELECT GREATEST(TEST1,TEST2) AS A, GREATEST(TEST1,TEST3) AS B, GREATEST(TEST3,TEST2) AS C, USN, SUBCODE, SSID
FROM IAMARKS
WHERE FINALIA IS NULL
FOR UPDATE;

OPEN C_IAMARKS;
LOOP

FETCH C_IAMARKS INTO C_A, C_B, C_C, C_USN, C_SUBCODE, C_SSID;

IF (C_A != C_B) THEN
	SET C_SUM=C_A+C_B;
ELSE
	SET C_SUM=C_A+C_C;
END IF;

SET C_AVG=C_SUM/2;

UPDATE IAMARKS SET FINALIA = C_AVG 
WHERE USN = C_USN AND SUBCODE = C_SUBCODE AND SSID = C_SSID;

END LOOP;
CLOSE C_IAMARKS;
END;
//


CALL AVG_MARKS();

SELECT * FROM IAMARKS;

--------------------------------------------

-- Categorize students based on the following criterion:
-- If FinalIA = 17 to 20 then CAT = 'Outstanding'
-- If FinalIA = 12 to 16 then CAT = 'Average'
-- If FinalIA< 12 then CAT = 'Weak'
-- Give these details only for 8th semester A, B, and C section students.

SELECT S.USN,S.SNAME,S.ADDRESS,S.PHONE,S.GENDER, IA.SUBCODE,
(CASE
WHEN IA.FINALIA BETWEEN 17 AND 20 THEN 'OUTSTANDING'
WHEN IA.FINALIA BETWEEN 12 AND 16 THEN 'AVERAGE'
ELSE 'WEAK'
END) AS CAT
FROM STUDENT S, SEMSEC SS, IAMARKS IA, SUBJECT SUB
WHERE S.USN = IA.USN AND
SS.SSID = IA.SSID AND
SUB.SUBCODE = IA.SUBCODE AND
SUB.SEM = 8;


	""")

def g_company():
	print("""
	--Create Table DEPARTMENT with PRIMARY KEY as DNO

CREATE TABLE DEPARTMENT
(DNO VARCHAR(20) PRIMARY KEY,
DNAME VARCHAR(20),
MGR_SSN VARCHAR(20),
MGR_START_DATE DATE);

DESC DEPARTMENT;

----------------------------------

--Create Table EMPLOYEE with PRIMARY KEY as SSN

CREATE TABLE EMPLOYEE
(SSN VARCHAR(20) PRIMARY KEY,
NAME VARCHAR(20),
ADDRESS VARCHAR(20),
SEX CHAR(1),
SALARY INTEGER,
SUPERSSN VARCHAR(20),
DNO VARCHAR(20),
FOREIGN KEY (SUPERSSN) REFERENCES EMPLOYEE (SSN),
FOREIGN KEY (DNO) REFERENCES DEPARTMENT (DNO));

DESC EMPLOYEE;

----------------------------------

-- ADD FOREIGN KEY Constraint to DEPARTMENT table

ALTER TABLE DEPARTMENT
ADD FOREIGN KEY (MGR_SSN) REFERENCES EMPLOYEE(SSN);

----------------------------------

--Create Table DLOCATION with PRIMARY KEY as DNO and DLOC and FOREIGN KEY DNO referring DEPARTMENT table

CREATE TABLE DLOCATION
(DLOC VARCHAR(20),
DNO VARCHAR(20),
FOREIGN KEY (DNO) REFERENCES DEPARTMENT(DNO),
PRIMARY KEY (DNO, DLOC));

DESC DLOCATION;

----------------------------------

--Create Table PROJECT with PRIMARY KEY as PNO and FOREIGN KEY DNO referring DEPARTMENT table

CREATE TABLE PROJECT
(PNO INTEGER PRIMARY KEY,
PNAME VARCHAR(20),
PLOCATION VARCHAR(20),
DNO VARCHAR(20),
FOREIGN KEY (DNO) REFERENCES DEPARTMENT(DNO));

DESC PROJECT;

----------------------------------

--Create Table WORKS_ON with PRIMARY KEY as PNO and SSN and FOREIGN KEY SSN and PNO referring EMPLOYEE and PROJECT table

CREATE TABLE WORKS_ON
(HOURS INTEGER,
SSN VARCHAR(20),
PNO INTEGER,
FOREIGN KEY (SSN) REFERENCES EMPLOYEE(SSN),
FOREIGN KEY (PNO) REFERENCES PROJECT(PNO),
PRIMARY KEY (SSN, PNO));

DESC WORKS_ON;

----------------------------------

--Inserting records into EMPLOYEE table

INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC01','BEN SCOTT','BANGALORE','M', 450000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC02','HARRY SMITH','BANGALORE','M', 500000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC03','LEAN BAKER','BANGALORE','M', 700000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC04','MARTIN SCOTT','MYSORE','M', 500000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC05','RAVAN HEGDE','MANGALORE','M', 650000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC06','GIRISH HOSUR','MYSORE','M', 450000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC07','NEELA SHARMA','BANGALORE','F', 800000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC08','ADYA KOLAR','MANGALORE','F', 350000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC09','PRASANNA KUMAR','MANGALORE','M', 300000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC10','VEENA KUMARI','MYSORE','M', 600000);
INSERT INTO EMPLOYEE (SSN, NAME, ADDRESS, SEX, SALARY) VALUES
 ('ABC11','DEEPAK RAJ','BANGALORE','M', 500000);

 SELECT * FROM EMPLOYEE;

----------------------------------

--Inserting records into DEPARTMENT table

INSERT INTO DEPARTMENT VALUES ('1','ACCOUNTS','ABC09', '2016-01-03');
INSERT INTO DEPARTMENT VALUES ('2','IT','ABC11', '2017-02-04');
INSERT INTO DEPARTMENT VALUES ('3','HR','ABC01', '2016-04-05');
INSERT INTO DEPARTMENT VALUES ('4','HELPDESK', 'ABC10', '2017-06-03');
INSERT INTO DEPARTMENT VALUES ('5','SALES','ABC06', '2017-01-08');

SELECT * FROM DEPARTMENT;

----------------------------------

--Updating EMPLOYEE records

UPDATE EMPLOYEE SET
SUPERSSN=NULL, DNO='3'
WHERE SSN='ABC01';

UPDATE EMPLOYEE SET
SUPERSSN='ABC03', DNO='5'
WHERE SSN='ABC02';

UPDATE EMPLOYEE SET
SUPERSSN='ABC04', DNO='5'
WHERE SSN='ABC03';

UPDATE EMPLOYEE SET
SUPERSSN='ABC06', DNO='5'
WHERE SSN='ABC04';

UPDATE EMPLOYEE SET
DNO='5', SUPERSSN='ABC06'
WHERE SSN='ABC05';

UPDATE EMPLOYEE SET
DNO='5', SUPERSSN='ABC07'
WHERE SSN='ABC06';

UPDATE EMPLOYEE SET
DNO='5', SUPERSSN=NULL
WHERE SSN='ABC07';

UPDATE EMPLOYEE SET
DNO='1', SUPERSSN='ABC09'
WHERE SSN='ABC08';

UPDATE EMPLOYEE SET
DNO='1', SUPERSSN=NULL
WHERE SSN='ABC09';

UPDATE EMPLOYEE SET
DNO='4', SUPERSSN=NULL
WHERE SSN='ABC10';

UPDATE EMPLOYEE SET
DNO='2', SUPERSSN=NULL
WHERE SSN='ABC11';

SELECT * FROM EMPLOYEE;

-------------------------------

--Inserting records into DLOCATION table

INSERT INTO DLOCATION VALUES ('BENGALURU', '1');
INSERT INTO DLOCATION VALUES ('BENGALURU', '2');
INSERT INTO DLOCATION VALUES ('BENGALURU', '3');
INSERT INTO DLOCATION VALUES ('MYSORE', '4');
INSERT INTO DLOCATION VALUES ('MYSORE', '5');

SELECT * FROM DLOCATION;

--------------------------------

--Inserting records into PROJECT table

INSERT INTO PROJECT VALUES (1000,'IOT','BENGALURU','5');
INSERT INTO PROJECT VALUES (1001,'CLOUD','BENGALURU','5');
INSERT INTO PROJECT VALUES (1002,'BIGDATA','BENGALURU','5');
INSERT INTO PROJECT VALUES (1003,'SENSORS','BENGALURU','3');
INSERT INTO PROJECT VALUES (1004,'BANK MANAGEMENT','BENGALURU','1');
INSERT INTO PROJECT VALUES (1005,'SALARY MANAGEMENT','BANGALORE','1');
INSERT INTO PROJECT VALUES (1006,'OPENSTACK','BENGALURU','4');
INSERT INTO PROJECT VALUES (1007,'SMART CITY','BENGALURU','2');

SELECT * FROM PROJECT;

------------------------------

--Inserting records into WORKS_ON table

INSERT INTO WORKS_ON VALUES (4, 'ABC02', 1000);
INSERT INTO WORKS_ON VALUES (6, 'ABC02', 1001);
INSERT INTO WORKS_ON VALUES (8, 'ABC02', 1002);
INSERT INTO WORKS_ON VALUES (10,'ABC03', 1000);
INSERT INTO WORKS_ON VALUES (3, 'ABC05', 1000);
INSERT INTO WORKS_ON VALUES (4, 'ABC06', 1001);
INSERT INTO WORKS_ON VALUES (5, 'ABC07', 1002);
INSERT INTO WORKS_ON VALUES (6, 'ABC04', 1002);
INSERT INTO WORKS_ON VALUES (7, 'ABC01', 1003);
INSERT INTO WORKS_ON VALUES (5, 'ABC08', 1004);
INSERT INTO WORKS_ON VALUES (6, 'ABC09', 1005);
INSERT INTO WORKS_ON VALUES (4, 'ABC10', 1006);
INSERT INTO WORKS_ON VALUES (10,'ABC11', 1007);

SELECT * FROM WORKS_ON;


--Make a list of all project numbers for projects that involve an employee whose last name is 'Scott', either as a worker or as a manager of the department that controls the project.

SELECT DISTINCT P.PNO
FROM PROJECT P, DEPARTMENT D, EMPLOYEE E
WHERE E.DNO=D.DNO
AND D.MGR_SSN=E.SSN
AND E.NAME LIKE '%SCOTT'
UNION
SELECT DISTINCT P1.PNO
FROM PROJECT P1, WORKS_ON W, EMPLOYEE E1
WHERE P1.PNO=W.PNO
AND E1.SSN=W.SSN
AND E1.NAME LIKE '%SCOTT';

--Show the resulting salaries if every employee working on the 'IoT' project is given a 10 percent raise.

SELECT E.NAME, 1.1*E.SALARY AS INCR_SAL
FROM EMPLOYEE E, WORKS_ON W, PROJECT P
WHERE E.SSN=W.SSN
AND W.PNO=P.PNO
AND P.PNAME='IOT';

--Find the sum of the salaries of all employees of the 'Accounts' department, as well as the maximum salary, the minimum salary, and the average salary in this department

SELECT SUM(E.SALARY), MAX(E.SALARY), MIN(E.SALARY), AVG(E.SALARY)
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DNO=D.DNO
AND D.DNAME='ACCOUNTS';

--Retrieve the name of each employee who works on all the projects controlled by department number 5 (use NOT EXISTS operator).

SELECT E.NAME
FROM EMPLOYEE E
WHERE NOT EXISTS(SELECT PNO FROM PROJECT WHERE DNO='5' AND PNO NOT IN (SELECT
PNO FROM WORKS_ON
WHERE E.SSN=SSN));

--For each department that has more than five employees, retrieve the department number and the number of its employees who are making more than Rs. 6,00,000.

SELECT D.DNO, COUNT(*)
FROM DEPARTMENT D, EMPLOYEE E
WHERE D.DNO=E.DNO
AND E.SALARY > 600000
AND D.DNO IN (SELECT E1.DNO
FROM EMPLOYEE E1
GROUP BY E1.DNO
HAVING COUNT(*)>5)
GROUP BY D.DNO;
	""")
    
