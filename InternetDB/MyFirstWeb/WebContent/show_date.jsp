<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<%-- src.package.class 이름으로 경로에 있는 class import 가능 --%>
<%@ page import = "pknu.it.DateUtil" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

<%-- import 해놓은 java class 내 매소드 사용하기 --%>
Hi There! Today is <%= DateUtil.getToday() %>

</body>
</html>