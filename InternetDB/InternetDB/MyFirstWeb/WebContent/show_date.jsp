<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<%-- src.package.class �̸����� ��ο� �ִ� class import ���� --%>
<%@ page import = "pknu.it.DateUtil" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

<%-- import �س��� java class �� �żҵ� ����ϱ� --%>
Hi There! Today is <%= DateUtil.getToday() %>

</body>
</html>