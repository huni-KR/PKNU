package pknu.it;


// Java Beans
// ������ �����ϴ� ��ü
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