<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

<a href="list-course.jsp"> ���� </a>�� ������ ��� ���������� �� �� �ֽ��ϴ�.

<table border=1>
<tr> <th> �й� <th> �̸� <th> �г� </tr>

<%@ include file = "connect-DB.jsp" %>

<%
	/*
	Statement / PreparedStatement ����
	Statement���� ����(Where ��) ���� Ư�� ���� ����
	PreparedStatement���� ����(Where ��) ���� ������ Ȱ�� ����
	
	Statement ���� sql Injection ��ŷ�� ���
	PreparedStatement�� ���� / ���ȿ��� �� ����	
	*/
	
	String searchSno = request.getParameter("sno");
	
	/*
	Statement st = conn.createStatement();
	ResultSet rs = st.executeQuery("select * from student where year = "+ searchYear);
	*/
	
	String sqlStr = "select * from student";	

	PreparedStatement st;
	if( searchSno != null && searchSno.length() > 0 ) {
		sqlStr += " where sno = ?";		
		st = conn.prepareStatement(sqlStr);		
		st.setString(1, searchSno);		
	}else{
		st = conn.prepareStatement(sqlStr);
	}

	ResultSet rs = st.executeQuery();

	while( rs.next() ){
		String sname = rs.getString("sname");
		int year = rs.getInt("year");
		String sno = rs.getString("sno");		
		
		System.out.println( sno + "\t" + sname + "\t" + year );
		
		%> <tr> <td> <%=sno %> <td> <a href="list-course2.jsp?sno=<%=sno%>"><%=sname %></a> <td> <%=year %> </tr>
		<% 	
	}
	
	System.out.println( "------------------------------" );
	
	rs.close();
	st.close();
	conn.close();	
%>

</table>

</body>
</html>