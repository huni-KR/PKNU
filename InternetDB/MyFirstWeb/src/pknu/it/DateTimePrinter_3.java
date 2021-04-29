package pknu.it;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class DateTimePrinter_3
 */
@WebServlet(description = "Print Date & Time", urlPatterns = { "/currenttime" })
public class DateTimePrinter_3 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public DateTimePrinter_3() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		PrintWriter out = response.getWriter();
		
		DateFormat dateFormat =	new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
		Date date = new Date();
//		System.out.println (dateFormat.format(date));
		
		String dateNtime = dateFormat.format(date);
		
		out.println("<html>");
		out.println("<title> Date and Time </title>");
		out.println("<body>");
		out.println("<h1> Current date and time is </h1>");
		out.println("<h1> " + dateNtime + " </h1>");		
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
