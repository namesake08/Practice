package com.accessor;

import java.io.IOException;
import static java.lang.System.out;

public class Main {

    public static void main(String[] args) throws IOException {
        Book b;
        Book b2 = new Book();

        b = new Book("Bible","the prophets", 100);
        out.println(b.toString());
        out.println(b2);

        new SimpleFrame();
        new TeamFrame();
    }
}
