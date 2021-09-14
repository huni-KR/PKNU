<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<%@ page import="java.sql.*" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
Class.forName("oracle.jdbc.OracleDriver");

Connection conn = DriverManager.getConnection(
		"jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "db201612009", "201612009");

%>
</body>
</html>