package com.accessor;

import java.awt.FlowLayout;
import javax.swing.JFrame;
import javax.swing.JButton;

/**Иногда при создании объекта нужно выполнить ряд операций, таких как
* конфигурирование объекта, его подготовка к работе, создание образа объекта
 * в базе данных, установка сетевого соединения для связи объекта с сервером и т.д.
 * Все это обычно делатся в конструкторе.
 * */
//@SuppressWarnings("serial")
public class SimpleFrame extends JFrame{
    public SimpleFrame(){
        setTitle ("Не щелкате на кнопке");
        setLayout (new FlowLayout());
        setDefaultCloseOperation (EXIT_ON_CLOSE);
        add (new JButton("Щелкни на мне!"));
        setSize (310, 100);
        setVisible(true);
    }
}
