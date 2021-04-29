package pknu.it;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.Servlet;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class Elvariables
 */
@WebServlet("/show-elvariables")
public class Elvariables extends HttpServlet implements Servlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Elvariables() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setAttribute("attr1", "EL_value1");
		
		HttpSession session = request.getSession();
		session.setAttribute("attr2", "EL_value2");
		
		ServletContext application = request.getServletContext();
		application.setAttribute("attr3", "EL_value3");
		
		request.setAttribute("dupname", "value_request");
		session.setAttribute("dupname", "value_session");
		application.setAttribute("dupname", "value_application");
		
		RequestDispatcher dispatcher =
				request.getRequestDispatcher("/show-elvariables.jsp");
		dispatcher.forward(request, response);

	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
