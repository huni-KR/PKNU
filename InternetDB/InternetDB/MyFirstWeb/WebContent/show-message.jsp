<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<%-- src.package.class 이름으로 경로에 있는 class import 가능 --%>
<%@ page import = "pknu.it.*" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

This is a demo of Java Bean

<%-- Bean으로 Java class 읽어오기 --%>
<jsp:useBean id="msg" class="pknu.it.Message" />

<ul>
<li> 초기값(Bean): <jsp:getProperty name="msg" property="message" /> </li>
<li> 초기값(Jsp tag): <%= msg.getMessage() %> </li>

<%-- 1. 기본값 변경 --%>
<%-- <jsp:setProperty name="msg" property="message" value="Hello World" /> --%>

<%-- 2. param(파라미터)에서 받은 내용으로 변경 --%>
<%-- ex) http://localhost:8080/MyServlet/show-message.jsp?greeting=hello --%>
<jsp:setProperty name="msg" property="message" param="greeting" /> 


<li> 변경된 값(Bean): <jsp:getProperty name="msg" property="message" /> </li>
<li> 변경된 값(EL): ${msg.message} </li>
</ul>

</body>
</html>