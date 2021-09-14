<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

<a href="list-course.jsp"> 여기 </a>를 누르면 모든 과목정보를 볼 수 있습니다.

<table border=1>
<tr> <th> 학번 <th> 이름 <th> 학년 </tr>

<%@ include file = "connect-DB.jsp" %>

<%
	/*
	Statement / PreparedStatement 차이
	Statement에서 조건(Where 등) 사용시 특정 값만 가능
	PreparedStatement에서 조건(Where 등) 사용시 변수로 활용 가능
	
	Statement 사용시 sql Injection 해킹에 취약
	PreparedStatement가 성능 / 보안에서 더 좋음	
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