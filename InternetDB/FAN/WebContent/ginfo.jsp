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

맴버 정보

<br>

<%
	Connection conn = DriverManager.getConnection(
			"jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "db201612009", "201612009");
	
	PreparedStatement st = conn.prepareStatement( "select * from idol where gno = ?" );
	
	
	String gno = request.getParameter("gno");
	st.setString(1, gno);
	ResultSet rs = st.executeQuery();
	
	while( rs.next() ){
		String name = rs.getString("name");
		String gender = rs.getString("gender");
		int year = rs.getInt("year");
				
		%>
		<tr> <td> <%= name %> <td> <%= gender %> <td> <%= year %> </tr>
		<% 	
	}
%>

</table>

<br>

발표곡 정보
<br>

<table border=1>
<tr> <th> 곡명 <th> 발표년도 </tr>

<%
	st = conn.prepareStatement( "select * from song where gno = ?" );

	gno = request.getParameter("gno");
	st.setString(1, gno);
	rs = st.executeQuery();

	while( rs.next() ){
		String title = rs.getString("title");
		int year = rs.getInt("year");
				
		%>
		<tr> <td> <%= title %> <td> <%= year %> </tr>
		<% 	
	}
%>

</table>


</body>
</html>
