<%@page import="java.sql.*"%>
<%@page import="javax.sql.*"%>
<%@page import="javax.naming.*"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>아이돌 팬사이트에 오신 것을 환영합니다.</title>
</head>
<body>

<table border=1>
<tr> <th> 그룹번호 <th> 그룹이름 <th> 소속사 </tr>

아이돌 팬사이트에 오신 것을 환영합니다.
<br>

<%
	
	
	Connection conn = DriverManager.getConnection(
			"jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "db201612009", "201612009");
	
	PreparedStatement st = conn.prepareStatement( "select * from IGRP" );
	ResultSet rs = st.executeQuery();

	while( rs.next() ){
		String gno = rs.getString("gno");
		String gname = rs.getString("gname");
		String company = rs.getString("company");
				
		%>
		<tr> <td> <%= gno %> <td> <%= gname %> <td> <%= company %> </tr>
		<% 	
	}
		
	st.close();
	rs.close();
	conn.close();
%>

</body>
</html>