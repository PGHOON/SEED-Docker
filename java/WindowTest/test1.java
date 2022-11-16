import javax.swing.*;

public class test1 extends JFrame {
	test1()
	{
		JPanel pan1 = new JPanel();	//pan1이라는 패널 생성
		JButton btn1 = new JButton("button message");	//btn1이라는 버튼 생성

		add(pan1);  //pan1을 추가
		pan1.add(btn1);	//pan1안에 btn1을 추가

		setTitle("frame test");	//window name
		setSize(600,400);	//window size
		setVisible(true);	//makes the frame appear on screen
		setLocationRelativeTo(null);		//window appears in the middle
		setDefaultCloseOperation(EXIT_ON_CLOSE);	//exit program when the window closes
	}

	public static void main(String[] args) {
		new test1();
	}
}