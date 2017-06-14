package com.accessor;

public class Book{

    public String name;
    public String author;
    public int year;
    private static int counter;

    static {
        counter = 1;
        System.out.println("Вызов статического метода");
    }

    Book(){
        name = "неизвестно";
        author = "неизвестно";
        year = 0;
    }

    Book(String name, String author, int year){
        this.name = name;
        this.author = author;
        this.year = year;
    }

    public String toString(){
        return String.format("Книга '%s' (автор %s) была издана в %d году \n", name, author, year);
    }
}
