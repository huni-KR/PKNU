<%@page import="java.sql.*"%>
<%@page import="javax.sql.*"%>
<%@page import="javax.naming.*"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

<%
	Connection conn = DriverManager.getConnection(
			"jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "db201612009", "201612009");

	PreparedStatement st = conn.prepareStatement( "update IDOL set LIKE_CNT = LIKE_CNT +1 where INO = ?" );
	String ino = request.getParameter("ino");
	String gno = request.getParameter("gno");
	
	
	st.setString(1, ino);
	
	ResultSet rs = st.executeQuery();

	RequestDispatcher rd = request.getRequestDispatcher("idol-like.jsp?gno=" + gno);
	rd.forward(request,response);
%>

</body>
</html>