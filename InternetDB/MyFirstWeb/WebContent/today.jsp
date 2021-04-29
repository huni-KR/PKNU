<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>Integers from 1 to 100</h1>
<ui>
   <%for(int i=0;i<=100;i++){ %>
   <li><%= i %>
   <%} %>
</ui>
</body>
</html>