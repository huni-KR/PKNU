<%@page import="java.sql.*"%>
<%@page import="javax.sql.*"%>
<%@page import="javax.naming.*"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>�л�����</title>
</head>
<body>

<table border=1>
<tr> <th> �����ȣ <th> �����̸� <th> ���� <th> �а� <th> ��米�� </tr>

<h1> �л� ���� </h1>

<%
	Context ctx = new InitialContext();
	DataSource ds = (DataSource)ctx.lookup("java:comp/env/jdbc/xe");
	
	Connection conn = ds.getConnection();
	PreparedStatement st = conn.prepareStatement(
			"select * from enrol natural join course where sno = ?" );
	
	String sno = request.getParameter("sno");
	st.setString(1, sno);
	ResultSet rs = st.executeQuery();
		
	while( rs.next() ){
		String cno = rs.getString("cno");
		String cname = rs.getString("cname");
		int credit = rs.getInt("credit");
		String dept = rs.getString("dept");
		String professor = rs.getString("professor");
				
		%>
		<tr> <td> <%= cno %> <td> <%= cname %> <td> <%= credit %> <td> <%= dept %> <td> <%= professor %> </tr>
		<% 	
	}
	
	
	st.close();
	rs.close();
	conn.close();
%>

</body>
</html>