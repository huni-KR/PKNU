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
Integer visitCount = null;
synchronized(session){
	visitCount = (Integer)session.getAttribute("visitCount");
	if (visitCount == null){
		visitCount = new Integer(0);
	}
	
	visitCount++;
	
	session.setAttribute("visitCount", visitCount);
}
%>

Visit Count : <%= visitCount %>

</body>
</html>