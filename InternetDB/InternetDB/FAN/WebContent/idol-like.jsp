<%@page import="java.sql.*"%>
<%@page import="javax.sql.*"%>
<%@page import="javax.naming.*"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>���̵� �һ���Ʈ�� ���� ���� ȯ���մϴ�.</title>
</head>
<body>

<table border=1>
<tr> <th> �׷��ȣ <th> �׷��̸� <th> �Ҽӻ� <th> ���ƿ� </tr>

�ɹ� ����
<br>

<%
	Connection conn = DriverManager.getConnection(
			"jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "db201612009", "201612009");
	
	PreparedStatement st = conn.prepareStatement( "select * from idol where gno = ?" );
	
	
	String gno = request.getParameter("gno");
	st.setString(1, gno);
	ResultSet rs = st.executeQuery();
	
	while( rs.next() ){
		String ino = rs.getString("ino");
		String name = rs.getString("name");
		String gender = rs.getString("gender");
		int year = rs.getInt("year");
		int like_cnt = rs.getInt("like_cnt");
				
		%>
		<tr> <td> <%= name %> <td> <%= gender %> <td> <%= year %> <td> <a href="inc-like.jsp?gno=<%=gno%>&ino=<%=ino%>"> <%=like_cnt%> </tr>
		<% 	
	}
%>

</body>
</html>
