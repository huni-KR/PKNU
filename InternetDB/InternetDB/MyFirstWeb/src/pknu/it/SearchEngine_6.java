package pknu.it;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class SearchEngine
 */
@WebServlet(description = "Forwarding to Search Engine", urlPatterns = { "/search" })
public class SearchEngine_6 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public SearchEngine_6() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		PrintWriter out = response.getWriter();
		
		String userAgent = request.getHeader("User-Agent");
		
		// 브라우저가 크롬인지 판별
		if( userAgent != null && userAgent.indexOf("Chrome") >= 0
				&& userAgent.indexOf("Edg/") < 0 ) {
			// sendRedirect 리다이렉트
			response.sendRedirect("http://www.google.com");
		}else {
			response.sendRedirect("http://www.naver.com");
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
