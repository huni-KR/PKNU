package pknu.it;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HttpRequestHeaderPrinter_5
 */
@WebServlet(description = "Print HTTP Request Headers", urlPatterns = { "/show-request-headers" })
public class HttpRequestHeaderPrinter_5 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HttpRequestHeaderPrinter_5() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		PrintWriter out = response.getWriter();
		
		out.println("<html> <head> <title> Print Request Headers </title> </head>");
		
		out.println("<body bgcolor=pink>");		
		out.println("<h2> Servlet Example : Showing Request Headers </h2>");
		out.println("Request Method : " + request.getMethod() + "<br>");		
		out.println("Request URL : " + request.getRequestURL() + "<br>");
		out.println("Request Protocol : " + request.getProtocol() + "<br>");
		
		// border=1 : 테이블 선 굵기 설정
		out.println("<table border=1>");
		
		// 테이블 맨 윗줄 작성
		out.println("<tr bgcolor=orange> <th> Field <th> Value </tr>");
		
		// request.getHeaderNames() 데이터 형식
		java.util.Enumeration<String> names = request.getHeaderNames();
		
		while( names.hasMoreElements() ) {
			String fieldName = names.nextElement();
			String value = request.getHeader(fieldName);
			
			// 테이블에 데이터 넣기
			out.println("<tr> <td>" + fieldName + "<td>" + value + "</tr>");					
		}
		
		out.println("</table>");
		
		out.println("</body>");
		out.println("</html>");

	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
