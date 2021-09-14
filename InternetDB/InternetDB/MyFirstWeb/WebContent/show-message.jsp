<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<%-- src.package.class �̸����� ��ο� �ִ� class import ���� --%>
<%@ page import = "pknu.it.*" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

This is a demo of Java Bean

<%-- Bean���� Java class �о���� --%>
<jsp:useBean id="msg" class="pknu.it.Message" />

<ul>
<li> �ʱⰪ(Bean): <jsp:getProperty name="msg" property="message" /> </li>
<li> �ʱⰪ(Jsp tag): <%= msg.getMessage() %> </li>

<%-- 1. �⺻�� ���� --%>
<%-- <jsp:setProperty name="msg" property="message" value="Hello World" /> --%>

<%-- 2. param(�Ķ����)���� ���� �������� ���� --%>
<%-- ex) http://localhost:8080/MyServlet/show-message.jsp?greeting=hello --%>
<jsp:setProperty name="msg" property="message" param="greeting" /> 


<li> ����� ��(Bean): <jsp:getProperty name="msg" property="message" /> </li>
<li> ����� ��(EL): ${msg.message} </li>
</ul>

</body>
</html>