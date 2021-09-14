package pknu.it;

import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.ParseException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Servlet implementation class Query Student
 */
@WebServlet("/student/*")
public class QueryStudents extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/** * @see HttpServlet#HttpServlet() */
	public QueryStudents() {
		super();
	}
	
	/**
	 * Extract ID from the request URL
	 * 
	 * @param request
	 *            Servlet request parameter
	 * @return integer representation of ID in URL
	 */
	private int getId(HttpServletRequest request) {
		String uri = request.getRequestURI();
		log("Request URI:"+uri);
		
		Pattern reId = Pattern.compile("/student/([0-9]+)");
		Matcher matcher = reId.matcher(uri);

		if (matcher.find()) {
			return Integer.parseInt(matcher.group(1));
		} else {
			return -1;
		}
	}	
	
	/**
	 * * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 * * response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		log("doGet");
		
		int sno = getId(request);
		log(String.format(" ID=%d \n", sno));
		
		try {
			Class.forName("oracle.jdbc.OracleDriver");
			Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "demo", "db123");
			
			PreparedStatement st;
			
			if (sno > 0) {
				st = conn.prepareStatement("select * from student where sno = ?");
				st.setInt(1, sno);
			} else {
				st = conn.prepareStatement("select * from student");
			}
			
			ResultSet rs = st.executeQuery();
			
			JSONArray arr = new JSONArray(); // [ { }, {  }, { }, { }, { }  ]
			
			while (rs.next()) {
				JSONObject o = new JSONObject();
				
				o.put("SNO", rs.getInt("SNO")); // "SNO" : 100
				o.put("SNAME", rs.getString("SNAME")); // "SNAME" : "ȫ�浿"
				o.put("YEAR", rs.getInt("YEAR"));
				o.put("DEPT", rs.getString("DEPT"));
					// { "SNO": 100, "SNAME": "ȫ�浿", "DEPT": "IT", "YEAR": 4}
				
				arr.put(o);
			}
			
			rs.close();
			st.close();
			conn.close();
			
			log(arr.toString());
			
			PrintWriter out = response.getWriter();
			out.print(arr);
			out.flush();
			
		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
	}	

	/**
	 * Read the content of the HTTP request and convert it into a string
	 * 
	 * @param is
	 * @return String representation of the HTTP request content
	 * @throws IOException
	 *             thrown when any error occurs while I/O operations
	 */
	private String convertInputStreamToString(InputStream is) throws IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(is));
		String line;
		StringBuffer result = new StringBuffer();
		while ((line = bufferedReader.readLine()) != null)
			result.append(line);

		return result.toString();
	}

	protected void doPut(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		log("doPut");

		JSONObject obj=null;
		try {
			obj = new JSONObject(convertInputStreamToString(request.getInputStream()));
			
			System.out.println("HTTP Body: "+obj.toString());
			
		} catch (ParseException e) {
			e.printStackTrace();
		}
		
		String sql = "insert into STUDENT(SNO,SNAME,YEAR,DEPT) values (?, ?, ?, ?)";
		
		try {
			Class.forName("oracle.jdbc.OracleDriver");
			Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "demo", "db123");
			
			PreparedStatement st = conn.prepareStatement(sql);

			st.setInt(1, obj.getInt("SNO"));
			st.setString(2, obj.getString("SNAME"));
			st.setInt(3, obj.getInt("YEAR"));
			st.setString(4, obj.getString("DEPT"));
			
			st.executeUpdate();
			
			conn.close();

		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}	

	}

	// FOR Student delete
	protected void doDelete(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		int sno = getId(request);
		
		log("DELETE: SNO = "+sno);
		
		String sql = "delete from STUDENT where sno=?";
		
		try {
			Class.forName("oracle.jdbc.OracleDriver");
			Connection conn = DriverManager.getConnection("jdbc.oracle:thin:@db.pknu.ac.kr:1521:xe\", \"db201612009\", \"201612009\"");
			
			PreparedStatement st = conn.prepareStatement(sql);
			st.setInt(1, sno);
			
			int rc = st.executeUpdate();
			
			conn.close();
			
		}catch(ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
		
		// Delete tuple from STUDENT table

	}
	
	// FOR Student update
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		
		log("doPost");	
		
		JSONObject obj=null;
		try {
			obj = new JSONObject(convertInputStreamToString(request.getInputStream()));
			
			System.out.println("HTTP Body: "+obj.toString());
			
		} catch (ParseException e) {
			e.printStackTrace();
		}
		
		String sql = "update STUDENT set sname=?, year=?, dept=? where sno=?";
		
		try {
			Class.forName("oracle.jdbc.OracleDriver");
			Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@db.pknu.ac.kr:1521:xe", "demo", "db123");
			
			PreparedStatement st = conn.prepareStatement(sql);

			st.setString(1, obj.getString("SNAME"));
			st.setInt(2, obj.getInt("YEAR"));
			st.setString(3, obj.getString("DEPT"));
			st.setInt(4, obj.getInt("SNO"));			
			
			st.executeUpdate();
			
			conn.close();

		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}			
	}
}
