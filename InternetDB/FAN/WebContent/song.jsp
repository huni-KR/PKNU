<%@page import="java.sql.*"%>
<%@page import="javax.sql.*"%>
<%@page import="javax.naming.*"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>발표곡 정보</title>
</head>
<body>

<table border=1>
<tr> <th> 곡명 <th> 발표년도 </tr>

발표곡 정보
<br>

<%		
	Connection conn = DriverManager.getConnection(
			"jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "db201612009", "201612009");
	
	PreparedStatement st = conn.prepareStatement( "select * from song where gno = ?" );


	String gno = request.getParameter("gno");
	st.setString(1, gno);
	ResultSet rs = st.executeQuery();

	while( rs.next() ){
		String title = rs.getString("title");
		int year = rs.getInt("year");
				
		%>
		<tr> <td> <%= title %> <td> <%= year %> </tr>
		<% 	
	}
		
	st.close();
	rs.close();
	conn.close();
%>

</body>
</html>
