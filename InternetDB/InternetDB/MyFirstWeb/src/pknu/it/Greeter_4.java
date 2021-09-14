package pknu.it;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Greeter_4
 */
@WebServlet(name = "GreeterServlet", description = "Servlet that create greeting message", urlPatterns = { "/greeting" })
public class Greeter_4 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Greeter_4() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		PrintWriter out = response.getWriter();
		
		out.println("<html>");
		out.println("<title> Greeting </title>");
		
		out.println("<body>");
		
		// Post로 받아오는 데이터 가지고 오기
		String userName = request.getParameter("name");
		String userDept = request.getParameter("dept");

		// url에 데이터 직접 입력하기 url?type1=data1&type2=data2
		// http://localhost:8080/MyFirstWeb/greeting?name=kim&dept=it
		out.println("<h1> " + userName + " from " + userDept + " </h1>");
		
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
