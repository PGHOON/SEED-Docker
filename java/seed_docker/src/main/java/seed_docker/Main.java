package seed_docker;

import javax.swing.*;

public class Main extends JFrame{
	public Main() {
		JPanel pan1 = new JPanel();	//pan1이라는 패널 생성
		JButton btn1 = new JButton("Ubuntu");	//btn1이라는 버튼 생성

		add(pan1);  //pan1을 추가
		pan1.add(btn1);	//pan1안에 btn1을 추가

		setTitle("SEED_Docker");	//window name
		setSize(600,400);	//window size
		setVisible(true);	//makes the frame appear on screen
		setLocationRelativeTo(null);		//window appears in the middle
		setDefaultCloseOperation(EXIT_ON_CLOSE);	//exit program when the window closes
		
	}

}
