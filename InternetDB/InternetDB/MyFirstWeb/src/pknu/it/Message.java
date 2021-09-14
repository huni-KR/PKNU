package pknu.it;


// Java Beans
// 조건을 만족하는 객체
public class Message {
	private String message;
	
	public Message() {	//	Property
		this.message = "NONE";
	}
	
	public String getMessage() {	// Property getter
		return message;
	}
	
	public void setMessage(String message) {	// Property setter
		this.message = message;	
	}
}