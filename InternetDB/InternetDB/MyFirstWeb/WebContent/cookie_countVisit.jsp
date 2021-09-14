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

Cookie[] cookies = request.getCookies();

int visitCount = 0;

if( cookies != null ){
	for( Cookie c : cookies ){
		if( "visit_count".equals(c.getName()) && c.getValue() != null ){
			visitCount = Integer.parseInt(c.getValue());
			break;
		}
	}
}

Cookie c = new Cookie("visit_count", Integer.toString(++visitCount) );
response.addCookie(c);

%>

<%= visitCount %> ��° �湮�Դϴ�.
<br><br>

</body>
</html>